from typing import TypedDict, List, Annotated
import operator

class ResearchState(TypedDict):
    """State structure for the research workflow."""
    messages: Annotated[List, operator.add]
    research_topic: str
    search_queries: List[str]
    collected_facts: List[dict]
    research_summary: str
    final_report: str
    current_agent: str
    error_count: int
    progress: int
