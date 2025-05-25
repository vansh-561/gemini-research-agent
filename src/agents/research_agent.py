from src.agents.base_agent import BaseAgent
from src.workflow.state import ResearchState
from src.tools.search_tool import SearchTool
from src.tools.fact_saver import FactManager
from langchain_core.messages import AIMessage
from config.settings import settings
from datetime import datetime

class ResearchAgent(BaseAgent):
    """Agent responsible for conducting web searches and collecting information."""
    
    def __init__(self):
        super().__init__()
        self.search_tool = SearchTool()
        self.fact_manager = FactManager()
    
    def execute(self, state: ResearchState) -> dict:
        """Conducts web searches using Tavily and collects information."""
        queries = state["search_queries"]
        collected_facts = []
        
        # Process searches with Tavily
        for query in queries[:settings.MAX_QUERIES_PER_RESEARCH]:
            try:
                search_results = self.search_tool.search(query)
                
                if search_results:
                    combined_content = self.search_tool.extract_content(search_results)
                    
                    if combined_content:
                        facts = self._extract_facts_from_content(query, combined_content)
                        collected_facts.extend(facts)
                else:
                    self._add_fallback_fact(query, collected_facts)
                        
            except Exception as e:
                print(f"Search error for '{query}': {str(e)}")
                self._add_fallback_fact(query, collected_facts)
        
        # Create research summary
        research_summary = self._create_research_summary(state["research_topic"], collected_facts)
        
        return self.create_response_dict(
            collected_facts=collected_facts,
            research_summary=research_summary,
            current_agent="editor",
            messages=[AIMessage(content=f"Collected {len(collected_facts)} facts")],
            progress=75
        )
    
    def _extract_facts_from_content(self, query: str, content: str) -> list:
        """Extract facts from search content using LLM."""
        prompt = f"""Extract 2 key facts from this search about "{query}":

{content}

Respond with facts only, one per line. Each fact under 40 words.
Focus on most important information."""
        
        response_content = self.invoke_llm(prompt)
        facts = [f.strip() for f in response_content.split('\n') if f.strip()]
        
        collected_facts = []
        for fact in facts[:settings.MAX_FACTS_PER_QUERY]:
            if fact and len(fact) > 10:
                fact_entry = self.fact_manager.add_fact(fact, query)
                collected_facts.append(fact_entry)
        
        return collected_facts
    
    def _add_fallback_fact(self, query: str, collected_facts: list):
        """Add a fallback fact when search fails."""
        fallback_fact = f"Unable to retrieve information for query: {query}"
        fact_entry = {
            "fact": fallback_fact,
            "source": "error",
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        collected_facts.append(fact_entry)
    
    def _create_research_summary(self, topic: str, facts: list) -> str:
        """Create a research summary from collected facts."""
        if not facts:
            return f"Limited information found about {topic}"
        
        all_facts = [f["fact"] for f in facts]
        summary_prompt = f"""Summarize research findings about "{topic}":

{chr(10).join(all_facts[:6])}

Create a 100-word summary covering main points."""
        
        return self.invoke_llm(summary_prompt)
