"""可行性研究 Task"""
from crewai import Task
from agents import FeasibilityExpert


def create_feasibility_task(expert: FeasibilityExpert, requirements_output: str) -> Task:
    """创建可行性研究任务

    Args:
        expert: 可行性专家 Agent 实例
        requirements_output: 需求分析输出结果

    Returns:
        Task: 可行性研究任务
    """
    return Task(
        description=f"""基于以下需求，进行可行性研究：

        需求分析结果：{requirements_output}

        研究维度：
        1. 技术可行性：现有技术栈能否支持？
        2. 成本效益：投入产出比是否合理？
        3. 时间可行性：工期是否可控？

        输出三维度评分（1-10 分）和综合建议""",
        agent=expert.agent,
        expected_output="可行性报告，包含技术、成本、时间三个维度的评分和建议"
    )
