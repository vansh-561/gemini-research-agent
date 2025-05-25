import streamlit as st
from config.settings import settings

class Sidebar:
    """Sidebar component for research topic input."""
    
    @staticmethod
    def render():
        """Render the sidebar with input controls."""
        with st.sidebar:
            st.header("Research Topic")
            user_topic = st.text_input("Enter a topic to research:")
            
            start_button = st.button(
                "Start Research", 
                type="primary", 
                disabled=not user_topic
            )
            
            st.divider()
            st.subheader("Example Topics")
            
            selected_example = None
            for example in settings.EXAMPLE_TOPICS:
                if st.button(example, key=f"ex_{example}"):
                    selected_example = example
            
            st.divider()
            st.info("💡 **Required API Keys:**\n- GOOGLE_API_KEY\n- TAVILY_API_KEY")
            
            # API key status
            missing_keys = settings.get_missing_keys()
            if missing_keys:
                st.error(f"Missing API keys: {', '.join(missing_keys)}")
            else:
                st.success("✅ All API keys configured")
        
        return user_topic, start_button, selected_example
