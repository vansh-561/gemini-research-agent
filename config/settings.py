import os
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Application settings and configuration."""
    
    # API Keys
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY", "")
    
    # Model Configuration
    MODEL_NAME: str = "gemini-2.0-flash"
    MODEL_TEMPERATURE: float = 0.3
    MAX_TOKENS: int = 800
    
    # Search Configuration
    MAX_SEARCH_RESULTS: int = 3
    SEARCH_DEPTH: str = "basic"
    MAX_QUERIES_PER_RESEARCH: int = 2
    MAX_FACTS_PER_QUERY: int = 2
    
    # UI Configuration
    PAGE_TITLE: str = "Gemini Research Agent"
    PAGE_ICON: str = "🔍"
    LAYOUT: str = "wide"
    
    # Example Topics
    EXAMPLE_TOPICS: list = [
        "AI trends 2024",
        "Electric vehicle market",
        "Remote work benefits",
        "Sustainable energy solutions",
        "Digital transformation"
    ]
    
    @classmethod
    def validate_api_keys(cls) -> Dict[str, bool]:
        """Validate that required API keys are present."""
        return {
            "google_api_key": bool(cls.GOOGLE_API_KEY),
            "tavily_api_key": bool(cls.TAVILY_API_KEY)
        }
    
    @classmethod
    def get_missing_keys(cls) -> list:
        """Get list of missing API keys."""
        validation = cls.validate_api_keys()
        return [key for key, valid in validation.items() if not valid]

settings = Settings()
