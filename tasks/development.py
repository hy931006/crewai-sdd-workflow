"""代码实现 Task"""
from crewai import Task


def create_development_task(agent, planning_output: str, project_name: str) -> Task:
    """创建代码实现任务

    Args:
        agent: CrewAI Agent 实例
        planning_output: 项目计划输出结果
        project_name: 项目名称

    Returns:
        Task: 代码实现任务
    """
    return Task(
        description=f"""基于项目计划，实现代码：

        项目计划：{planning_output}
        项目名称：{project_name}

        要求：
        1. 遵循项目计划的任务顺序
        2. 代码结构清晰，注释完善
        3. 包含基础的错误处理
        4. 创建项目目录和必要文件

        输出：创建完整的项目代码文件""",
        agent=agent,
        expected_output="完整的项目代码文件，包含所有必要模块"
    )
