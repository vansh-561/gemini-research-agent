import streamlit as st
from config.settings import settings
from ui.components.sidebar import Sidebar
from ui.components.research_tab import ResearchTab
from ui.components.report_tab import ReportTab
from src.tools.fact_saver import FactManager

class ResearchApp:
    """Main research application."""
    
    def __init__(self):
        self.sidebar = Sidebar()
        self.research_tab = ResearchTab()
        self.report_tab = ReportTab()
        self.fact_manager = FactManager()
        self._setup_page()
        self._initialize_session_state()
    
    def _setup_page(self):
        """Setup page configuration."""
        st.set_page_config(
            page_title=settings.PAGE_TITLE,
            page_icon=settings.PAGE_ICON,
            layout=settings.LAYOUT,
            initial_sidebar_state="expanded"
        )
    
    def _initialize_session_state(self):
        """Initialize session state variables."""
        if "research_facts" not in st.session_state:
            st.session_state.research_facts = []
        if "research_complete" not in st.session_state:
            st.session_state.research_complete = False
        if "final_report" not in st.session_state:
            st.session_state.final_report = None
    
    def _check_api_keys(self):
        """Check if required API keys are present."""
        missing_keys = settings.get_missing_keys()
        if missing_keys:
            st.error(f"Please set the following environment variables: {', '.join(missing_keys)}")
            st.stop()
    
    def run(self):
        """Run the main application."""
        # Check API keys
        self._check_api_keys()
        
        # App title and description
        st.title(f"{settings.PAGE_ICON} {settings.PAGE_TITLE} with Tavily")
        st.subheader("Powered by Google Gemini, Tavily Search & LangGraph")
        st.markdown("Multi-agent research system using LangChain and LangGraph with Tavily Search")
        
        # Render sidebar
        user_topic, start_button, selected_example = self.sidebar.render()
        
        # Handle example selection
        if selected_example:
            user_topic = selected_example
            start_button = True
        
        # Main content tabs
        tab1, tab2 = st.tabs(["Research Process", "Final Report"])
        
        # Research execution
        if start_button and user_topic:
            # Reset session state
            self.fact_manager.clear_facts()
            st.session_state.research_complete = False
            st.session_state.final_report = None
            
            with tab1:
                self.research_tab.render(user_topic)
        
        # Display final report
        with tab2:
            self.report_tab.render(user_topic if user_topic else "")
        
        # Footer
        st.markdown("---")
        st.markdown("Built with 🔍 Google Gemini, 🌐 Tavily Search, 🦜 LangChain, and 📊 Streamlit")
