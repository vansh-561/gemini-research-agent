#!/usr/bin/env python3
"""
Gemini Research Agent - Main Entry Point
Multi-agent research system using Google Gemini, Tavily Search, LangChain, and LangGraph
"""

from ui.app import ResearchApp

def main():
    """Main application entry point."""
    app = ResearchApp()
    app.run()

if __name__ == "__main__":
    main()
