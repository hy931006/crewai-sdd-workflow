"""SDD Workflow Agents - 代码检视 Agent"""
from crewai import Agent
from langchain_openai import ChatOpenAI

class CodeReviewer:
    """代码检视 Agent"""
    
    def __init__(self, llm=None):
        self.llm = llm or ChatOpenAI(model="gpt-4o")
    
    def create_agent(self):
        return Agent(
            role="代码检视员",
            goal="发现代码缺陷和安全问题，提出改进建议",
            backstory="你是一位资深的代码审计专家，对代码质量和安全性有极高的要求。",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
