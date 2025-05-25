import streamlit as st
from src.tools.fact_saver import FactManager

class ReportTab:
    """Final report tab component."""
    
    def __init__(self):
        self.fact_manager = FactManager()
    
    def render(self, topic: str = ""):
        """Render the final report tab."""
        if st.session_state.get("research_complete") and st.session_state.get("final_report"):
            st.markdown(st.session_state.final_report)
            
            # Download button
            st.download_button(
                label="📄 Download Report",
                data=st.session_state.final_report,
                file_name=f"research_report_{topic.replace(' ', '_')}.md",
                mime="text/markdown"
            )
            
            # Display collected facts
            facts = self.fact_manager.get_facts()
            if facts:
                with st.expander("📋 All Collected Facts"):
                    for i, fact in enumerate(facts, 1):
                        st.write(f"**{i}.** {fact['fact']}")
                        st.caption(f"Source: {fact['source']} | Time: {fact['timestamp']}")
        
        elif not st.session_state.get("research_complete"):
            st.info("👆 Start a research topic from the sidebar to see results here")
        
        else:
            st.warning("No report available. Please try running the research again.")
