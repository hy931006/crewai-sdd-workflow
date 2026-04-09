"""SDD Workflow Agents - 代码检视 Agent"""
from crewai import Agent
from langchain_openai import ChatOpenAI

class CodeReviewer:
    """代码检视 Agent"""

    def __init__(self, llm: ChatOpenAI):
        self.llm = llm
        self.agent = Agent(
            role="代码检视员",
            goal="发现代码缺陷、安全漏洞和代码异味，提出改进建议",
            backstory="""你是一位代码审计专家，对代码质量有极高要求。
你熟悉各种设计模式和重构技巧。""",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
