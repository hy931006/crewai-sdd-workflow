"""SDD Workflow Agents - 需求分析 Agent"""
from crewai import Agent
from langchain_openai import ChatOpenAI

class RequirementsAnalyst:
    """需求分析 Agent"""
    
    def __init__(self, llm=None):
        self.llm = llm or ChatOpenAI(model="gpt-4o")
    
    def create_agent(self):
        return Agent(
            role="需求分析师",
            goal="深入分析用户需求，输出结构化的需求文档",
            backstory="你是一位资深需求分析师，擅长将模糊的需求转化为清晰的功能描述。",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
