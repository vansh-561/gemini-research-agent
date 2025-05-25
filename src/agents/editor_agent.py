from src.agents.base_agent import BaseAgent
from src.workflow.state import ResearchState
from langchain_core.messages import AIMessage

class EditorAgent(BaseAgent):
    """Agent responsible for creating the final research report."""
    
    def execute(self, state: ResearchState) -> dict:
        """Creates the final research report."""
        topic = state["research_topic"]
        summary = state["research_summary"]
        facts = state["collected_facts"]
        
        prompt = f"""Create a research report about "{topic}".

Summary: {summary}

Facts:
{chr(10).join([f"- {f['fact']}" for f in facts[:6]])}

Write a 250-word report with:
1. Title
2. Introduction (40 words)
3. Key Findings (120 words)
4. Conclusion (40 words)

Use markdown. Be concise."""
        
        final_report = self.invoke_llm(prompt)
        
        return self.create_response_dict(
            final_report=final_report,
            current_agent="complete",
            messages=[AIMessage(content="Research report completed")],
            progress=100
        )
