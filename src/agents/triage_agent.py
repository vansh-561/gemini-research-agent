from src.agents.base_agent import BaseAgent
from src.workflow.state import ResearchState
from langchain_core.messages import AIMessage
from config.settings import settings

class TriageAgent(BaseAgent):
    """Agent responsible for planning research approach and creating search queries."""
    
    def execute(self, state: ResearchState) -> dict:
        """Plans the research approach and creates search queries."""
        topic = state["research_topic"]
        
        prompt = f"""Create a research plan for: "{topic}"
        
        Generate 3 specific search queries for comprehensive information.
        Focus on different aspects of the topic.
        
        Respond with ONLY the search queries, one per line.
        Keep each query under 8 words.
        """
        
        response_content = self.invoke_llm(prompt)
        queries = [q.strip() for q in response_content.split('\n') if q.strip()]
        
        # Limit queries based on settings
        limited_queries = queries[:3]
        
        return self.create_response_dict(
            search_queries=limited_queries,
            current_agent="research",
            messages=[AIMessage(content=f"Created {len(limited_queries)} search queries")],
            progress=25
        )
