"""SDD Workflow Agents - 计划员 Agent"""
from crewai import Agent
from langchain_openai import ChatOpenAI

class ProjectPlanner:
    """项目计划 Agent"""
    
    def __init__(self, llm=None):
        self.llm = llm or ChatOpenAI(model="gpt-4o")
    
    def create_agent(self):
        return Agent(
            role="项目计划师",
            goal="制定详细的项目计划和任务拆解",
            backstory="你是一位经验丰富的项目经理，擅长将复杂任务拆解为可执行的小任务。",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
