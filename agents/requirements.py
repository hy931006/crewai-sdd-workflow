"""SDD Workflow Agents - 需求分析 Agent"""
from crewai import Agent, LLM

class RequirementsAnalyst:
    """需求分析 Agent"""

    def __init__(self, llm: LLM):
        self.llm = llm
        self.agent = Agent(
            role="需求分析师",
            goal="深入分析用户需求，输出结构化、无歧义的需求规格说明书",
            backstory="""你是一位资深需求分析师，在软件行业有 10 年经验。
你擅长将模糊的业务需求转化为清晰的技术规格，
能够识别潜在风险并提出建设性建议。""",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
