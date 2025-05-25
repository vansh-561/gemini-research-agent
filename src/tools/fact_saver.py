import streamlit as st
from datetime import datetime
from langchain_core.tools import tool
from typing import Dict, Any

@tool
def save_research_fact(fact: str, source: str = "web search") -> str:
    """Save an important research fact with its source."""
    fact_entry = {
        "fact": fact,
        "source": source,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    }
    
    if "research_facts" not in st.session_state:
        st.session_state.research_facts = []
    
    st.session_state.research_facts.append(fact_entry)
    return f"Saved fact: {fact[:50]}..."

class FactManager:
    """Manages research facts collection and storage."""
    
    @staticmethod
    def add_fact(fact: str, source: str) -> Dict[str, Any]:
        """Add a new fact to the collection."""
        fact_entry = {
            "fact": fact,
            "source": source,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        
        if "research_facts" not in st.session_state:
            st.session_state.research_facts = []
        
        st.session_state.research_facts.append(fact_entry)
        return fact_entry
    
    @staticmethod
    def get_facts() -> list:
        """Get all collected facts."""
        return st.session_state.get("research_facts", [])
    
    @staticmethod
    def clear_facts():
        """Clear all collected facts."""
        st.session_state.research_facts = []
    
    @staticmethod
    def get_facts_count() -> int:
        """Get count of collected facts."""
        return len(st.session_state.get("research_facts", []))
