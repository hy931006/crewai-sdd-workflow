"""SDD Workflow Agents - 技术文档 Agent"""
from crewai import Agent
from langchain_openai import ChatOpenAI

class TechnicalWriter:
    """技术文档 Agent"""

    def __init__(self, llm: ChatOpenAI):
        self.llm = llm
        self.agent = Agent(
            role="技术文档工程师",
            goal="编写清晰、完整的项目文档和技术规格说明",
            backstory="""你是一位专业的技术写作者。
你的文档简洁明了，易于理解和维护。""",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
