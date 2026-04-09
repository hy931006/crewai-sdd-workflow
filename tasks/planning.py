"""项目计划 Task"""
from crewai import Task


def create_planning_task(agent, feasibility_output: str) -> Task:
    """创建项目计划任务

    Args:
        agent: CrewAI Agent 实例
        feasibility_output: 可行性报告输出结果

    Returns:
        Task: 项目计划任务
    """
    return Task(
        description=f"""基于可行性研究结果，制定详细的项目计划：

        可行性报告：{feasibility_output}

        要求：
        1. WBS 工作分解结构
        2. 每个任务的工期估算
        3. 任务依赖关系
        4. 关键路径识别

        输出格式：任务列表，包含 ID、名称、工期、依赖""",
        agent=agent,
        expected_output="WBS 任务分解表，包含任务 ID、名称、工期和依赖关系"
    )
