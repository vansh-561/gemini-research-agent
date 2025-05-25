import streamlit as st
from src.workflow.graph import ResearchWorkflow
from src.tools.fact_saver import FactManager

class ResearchTab:
    """Research process tab component."""
    
    def __init__(self):
        self.workflow = ResearchWorkflow()
        self.fact_manager = FactManager()
    
    def render(self, topic: str):
        """Render the research process tab."""
        st.write(f"🔍 **Starting research on:** {topic}")
        
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        facts_container = st.container()
        
        try:
            # Run the workflow
            config = {"configurable": {"thread_id": "research_thread"}}
            
            step = 0
            for state in self.workflow.run_research(topic, config):
                step += 1
                current_state = list(state.values())[0]
                
                # Update progress
                progress = current_state.get("progress", min(step * 33, 100))
                progress_bar.progress(progress)
                
                # Update status
                agent = current_state.get("current_agent", "unknown")
                status_text.write(f"**Current Step:** {agent.title()} Agent")
                
                # Display facts as they're collected
                facts = self.fact_manager.get_facts()
                if facts:
                    with facts_container:
                        st.write("📚 **Collected Facts:**")
                        for fact in facts[-3:]:  # Show last 3 facts
                            st.info(f"**{fact['source']}**: {fact['fact']}")
                
                # Store final report
                if current_state.get("final_report"):
                    st.session_state.final_report = current_state["final_report"]
                    st.session_state.research_complete = True
            
            progress_bar.progress(100)
            status_text.write("✅ **Research Complete!**")
            
        except Exception as e:
            st.error(f"Error during research: {str(e)}")
            st.info("This might be due to API rate limits. Try again in a moment.")
