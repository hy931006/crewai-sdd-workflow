"""需求分析 Task"""
from crewai import Task
from agents import RequirementsAnalyst


def create_requirement_task(analyst: RequirementsAnalyst, requirement: str) -> Task:
    """创建需求分析任务

    Args:
        analyst: 需求分析师 Agent 实例
        requirement: 用户需求描述

    Returns:
        Task: 需求分析任务
    """
    return Task(
        description=f"""分析以下需求，输出结构化需求规格说明书：

        需求：{requirement}

        要求：
        1. 识别核心功能和边界条件
        2. 定义数据模型和接口
        3. 列出非功能性需求（性能、安全等）
        4. 识别潜在风险点

        输出格式：
        - 功能需求清单（带优先级）
        - 数据字典
        - API 接口设计
        - 风险评估""",
        agent=analyst.agent,
        expected_output="结构化需求规格说明书，包含功能清单、数据模型、接口定义"
    )
