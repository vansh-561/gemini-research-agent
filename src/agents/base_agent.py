from abc import ABC, abstractmethod
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from config.settings import settings
from src.workflow.state import ResearchState

class BaseAgent(ABC):
    """Base class for all research agents."""
    
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=settings.MODEL_NAME,
            temperature=settings.MODEL_TEMPERATURE,
            max_tokens=settings.MAX_TOKENS
        )
    
    @abstractmethod
    def execute(self, state: ResearchState) -> dict:
        """Execute the agent's main functionality."""
        pass
    
    def invoke_llm(self, prompt: str) -> str:
        """Invoke the LLM with a prompt."""
        try:
            response = self.llm.invoke([HumanMessage(content=prompt)])
            return response.content
        except Exception as e:
            print(f"LLM invocation error: {str(e)}")
            return f"Error processing request: {str(e)}"
    
    def create_response_dict(self, **kwargs) -> dict:
        """Create a standardized response dictionary."""
        response = {}
        for key, value in kwargs.items():
            response[key] = value
        return response
