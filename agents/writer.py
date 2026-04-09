"""SDD Workflow Agents - 文档 Agent"""
from crewai import Agent
from langchain_openai import ChatOpenAI

class TechnicalWriter:
    """技术文档 Agent"""
    
    def __init__(self, llm=None):
        self.llm = llm or ChatOpenAI(model="gpt-4o")
    
    def create_agent(self):
        return Agent(
            role="技术文档工程师",
            goal="编写清晰、完整的项目文档",
            backstory="你是一位专业的技术写作者，擅长用简洁的语言解释复杂的技术概念。",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
