from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from src.workflow.state import ResearchState
from src.agents.triage_agent import TriageAgent
from src.agents.research_agent import ResearchAgent
from src.agents.editor_agent import EditorAgent

class ResearchWorkflow:
    """Main workflow orchestrator for the research process."""
    
    def __init__(self):
        self.triage_agent = TriageAgent()
        self.research_agent = ResearchAgent()
        self.editor_agent = EditorAgent()
        self.workflow = None
        self.app = None
    
    def create_workflow(self):
        """Create and compile the research workflow graph."""
        workflow = StateGraph(ResearchState)
        
        # Add nodes
        workflow.add_node("triage", self._triage_node)
        workflow.add_node("research", self._research_node)
        workflow.add_node("editor", self._editor_node)
        
        # Add edges
        workflow.set_entry_point("triage")
        workflow.add_edge("triage", "research")
        workflow.add_edge("research", "editor")
        workflow.add_edge("editor", END)
        
        # Compile the graph
        memory = MemorySaver()
        self.app = workflow.compile(checkpointer=memory)
        
        return self.app
    
    def _triage_node(self, state: ResearchState):
        """Triage agent node wrapper."""
        return self.triage_agent.execute(state)
    
    def _research_node(self, state: ResearchState):
        """Research agent node wrapper."""
        return self.research_agent.execute(state)
    
    def _editor_node(self, state: ResearchState):
        """Editor agent node wrapper."""
        return self.editor_agent.execute(state)
    
    def run_research(self, topic: str, config: dict = None):
        """Run the complete research workflow."""
        if not self.app:
            self.create_workflow()
        
        initial_state = {
            "messages": [],
            "research_topic": topic,
            "search_queries": [],
            "collected_facts": [],
            "research_summary": "",
            "final_report": "",
            "current_agent": "triage",
            "error_count": 0,
            "progress": 0
        }
        
        if config is None:
            config = {"configurable": {"thread_id": "research_thread"}}
        
        return self.app.stream(initial_state, config)
