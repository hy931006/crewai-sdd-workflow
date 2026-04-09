"""SDD Workflow Agents - 开发者 Agent"""
from crewai import Agent
from langchain_openai import ChatOpenAI

class SeniorDeveloper:
    """高级开发工程师 Agent"""
    
    def __init__(self, llm=None):
        self.llm = llm or ChatOpenAI(model="gpt-4o")
    
    def create_agent(self):
        return Agent(
            role="高级开发工程师",
            goal="根据设计文档高质量实现代码",
            backstory="你是一位经验丰富的 Python 开发工程师，精通游戏开发和面向对象设计。",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
