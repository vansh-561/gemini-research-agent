# 🔍 Gemini Research Agent

A sophisticated multi-agent research application powered by Google Gemini, Tavily Search, LangChain, and LangGraph. This system enables users to conduct comprehensive research on any topic using specialized AI agents that work together to gather, analyze, and synthesize information.

## ✨ Features

- **🤖 Multi-Agent Architecture**: Three specialized agents working in harmony
  - **Triage Agent**: Plans research approach and coordinates workflow
  - **Research Agent**: Searches the web using Tavily and gathers information
  - **Editor Agent**: Compiles findings into comprehensive reports

- **🔍 Advanced Search**: Powered by Tavily Search for reliable, structured results
- **📊 Real-time Progress**: Live updates on research progress and fact collection
- **📄 Report Generation**: Creates well-structured markdown reports with citations for downloading
- **💾 Fact Management**: Automatic collection and organization of research facts
- **🎨 Interactive UI**: Clean Streamlit interface with tabbed navigation
- **⚡ Optimized Performance**: Token-efficient design for free-tier usage


## 🚀 Quick Start

### Prerequisites

- Python 3.13 or higher
- Poetry for dependency management
- Google API key (for Gemini)
- Tavily API key (for search)

### Installation

1. **Clone the repository**
- git clone <your-repository-url>
- cd gemini-research-agent

2. **Install Poetry** (if not already installed)
- curl -sSL https://install.python-poetry.org | python3 -

3. **Install dependencies**
- poetry install

4. **Set up environment variables in .env file**
- GOOGLE_API_KEY=your_google_api_key_here
- TAVILY_API_KEY=your_tavily_api_key_here

## 💻 Usage

1. **Start the application**

2. **Enter a research topic** in the sidebar or select from examples

3. **Click "Start Research"** to begin the multi-agent workflow

4. **Monitor progress** in the "Research Process" tab

5. **View results** in the "Final Report" tab

6. **Download** your research report as a markdown file

### Example Topics
- "AI trends 2024"
- "Electric vehicle market analysis"
- "Remote work benefits and challenges"
- "Sustainable energy solutions"
- "Digital transformation strategies"

