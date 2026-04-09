"""SDD Workflow Agents - 测试 Agent"""
from crewai import Agent
from langchain_openai import ChatOpenAI

class QAEngineer:
    """测试工程师 Agent"""
    
    def __init__(self, llm=None):
        self.llm = llm or ChatOpenAI(model="gpt-4o")
    
    def create_agent(self):
        return Agent(
            role="测试工程师",
            goal="编写全面的单元测试和集成测试，确保代码质量",
            backstory="你是一位严谨的 QA 工程师，追求零缺陷交付。",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
