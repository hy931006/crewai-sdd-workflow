"""SDD Workflow Agents - 开发工程师 Agent"""
from crewai import Agent
from langchain_openai import ChatOpenAI

class SeniorDeveloper:
    """开发工程师 Agent"""

    def __init__(self, llm: ChatOpenAI):
        self.llm = llm
        self.agent = Agent(
            role="高级开发工程师",
            goal="编写高质量、可维护的生产级代码",
            backstory="""你是一位全栈开发工程师，精通 Python/JavaScript/Go 等语言。
你编写的代码遵循最佳实践，注重性能和安全性。""",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
