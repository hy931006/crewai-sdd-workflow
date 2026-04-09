"""端到端测试 Task"""
from crewai import Task


def create_e2e_test_task(agent, review_output: str) -> Task:
    """创建端到端测试任务

    Args:
        agent: CrewAI Agent 实例
        review_output: 代码检视输出结果

    Returns:
        Task: 端到端测试任务
    """
    return Task(
        description=f"""设计和执行端到端测试：

        代码检视图：{review_output}

        要求：
        1. 设计完整的用户旅程测试
        2. 测试正常流程和异常流程
        3. 验证各模块集成正确性

        输出：E2E 测试场景和结果报告""",
        agent=agent,
        expected_output="E2E 测试报告，包含测试场景和通过/失败状态"
    )
