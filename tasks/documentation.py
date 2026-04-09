"""文档编写 Task"""
from crewai import Task


def create_documentation_task(agent, all_outputs: str, project_name: str) -> Task:
    """创建文档编写任务

    Args:
        agent: CrewAI Agent 实例
        all_outputs: 所有阶段产出汇总
        project_name: 项目名称

    Returns:
        Task: 文档编写任务
    """
    return Task(
        description=f"""编写项目完整文档：

        项目名称：{project_name}
        所有阶段产出：{all_outputs}

        文档要求：
        1. README.md - 项目简介、快速开始
        2. DESIGN.md - 系统设计文档
        3. API.md - 接口文档（如适用）
        4. CHANGELOG.md - 变更记录

        输出：完整的项目文档""",
        agent=agent,
        expected_output="完整的项目文档集：README、DESIGN、API 等"
    )
