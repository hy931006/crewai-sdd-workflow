"""单元测试 Task"""
from crewai import Task
from agents import QAEngineer


def create_unit_test_task(qa: QAEngineer, development_output: str) -> Task:
    """创建单元测试任务

    Args:
        qa: 测试工程师 Agent 实例
        development_output: 开发产出结果

    Returns:
        Task: 单元测试任务
    """
    return Task(
        description=f"""为已实现的代码编写单元测试：

        开发产出：{development_output}

        要求：
        1. 测试覆盖率 >= 80%
        2. 覆盖正常和异常场景
        3. 使用 pytest 框架
        4. 包含测试数据和预期结果

        输出：test_*.py 测试文件""",
        agent=qa.agent,
        expected_output="完整的单元测试文件，覆盖核心功能"
    )
