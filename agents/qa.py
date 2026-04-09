"""SDD Workflow Agents - 测试工程师 Agent"""
from crewai import Agent, LLM

class QAEngineer:
    """测试工程师 Agent"""

    def __init__(self, llm: LLM):
        self.llm = llm
        self.agent = Agent(
            role="测试工程师",
            goal="设计并编写全面的测试用例，确保代码质量",
            backstory="""你是一位资深 QA 工程师，精通测试金字塔策略。
你编写的测试覆盖边界条件和异常场景。""",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
