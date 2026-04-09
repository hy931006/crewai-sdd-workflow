"""代码检视 Task"""
from crewai import Task
from agents import CodeReviewer


def create_review_task(reviewer: CodeReviewer, development_output: str) -> Task:
    """创建代码检视任务

    Args:
        reviewer: 代码检视员 Agent 实例
        development_output: 开发产出结果

    Returns:
        Task: 代码检视任务
    """
    return Task(
        description=f"""检视已开发的代码：

        代码内容：{development_output}

        检视维度：
        1. 代码质量（可读性、可维护性）
        2. 安全性（注入、认证、授权）
        3. 性能问题
        4. 设计模式应用

        输出：问题清单和改进建议""",
        agent=reviewer.agent,
        expected_output="代码检视报告，列出发现的问题和优先级"
    )
