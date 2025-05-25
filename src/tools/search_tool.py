from langchain_community.tools import TavilySearchResults
from config.settings import settings
from typing import Dict, Any, List

class SearchTool:
    """Wrapper for Tavily search functionality."""
    
    def __init__(self):
        self.tool = TavilySearchResults(
            max_results=settings.MAX_SEARCH_RESULTS,
            include_answer=True,
            include_raw_content=False,
            include_images=False,
            search_depth=settings.SEARCH_DEPTH
        )
    
    def search(self, query: str) -> List[Dict[str, Any]]:
        """Perform search and return results."""
        try:
            results = self.tool.invoke({"query": query})
            if isinstance(results, list):
                return results
            return []
        except Exception as e:
            print(f"Search error for query '{query}': {str(e)}")
            return []
    
    def extract_content(self, results: List[Dict[str, Any]], max_chars: int = 600) -> str:
        """Extract and combine content from search results."""
        combined_content = ""
        for result in results[:2]:
            if isinstance(result, dict):
                content = result.get('content', '')
                if content:
                    combined_content += content + " "
        
        return combined_content[:max_chars] if combined_content else ""
