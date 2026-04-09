"""SDD Workflow Agents - 项目计划 Agent"""
from crewai import Agent
from langchain_openai import ChatOpenAI

class ProjectPlanner:
    """项目计划 Agent"""

    def __init__(self, llm: ChatOpenAI):
        self.llm = llm
        self.agent = Agent(
            role="项目计划师",
            goal="制定详细、可执行的项目计划和任务拆解",
            backstory="""你是一位经验丰富的项目经理（PMP 认证）。
你擅长将复杂项目拆解为可管理的小任务，
准确评估工期和资源需求。""",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
