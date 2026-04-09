"""SDD Workflow Agents - 端到端测试 Agent"""
from crewai import Agent
from langchain_openai import ChatOpenAI

class E2ETester:
    """端到端测试 Agent"""

    def __init__(self, llm: ChatOpenAI):
        self.llm = llm
        self.agent = Agent(
            role="端到端测试工程师",
            goal="设计和执行端到端测试场景，验证系统完整性",
            backstory="""你是一位 E2E 测试专家，熟悉用户旅程测试。
你能够从用户角度设计测试场景。""",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
