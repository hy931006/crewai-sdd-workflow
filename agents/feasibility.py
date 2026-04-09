"""SDD Workflow Agents - 可行性研究 Agent"""
from crewai import Agent, LLM

class FeasibilityExpert:
    """可行性研究 Agent"""

    def __init__(self, llm: LLM):
        self.llm = llm
        self.agent = Agent(
            role="可行性研究专家",
            goal="从技术、成本、时间三个维度评估项目可行性",
            backstory="""你是一位技术架构师，精通各种技术栈。
你能够快速评估技术方案的可行性和风险，
给出切实可行的替代方案。""",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
