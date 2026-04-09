"""
SDD Workflow - 多 Agent 协同软件开发生命周期
基于 CrewAI 的通用自动化软件开发框架

使用方法:
    from workflow import SDDWorkflow

    workflow = SDDWorkflow()
    results = workflow.run("实现一个博客系统")
"""
from crewai import Crew, Process
from langchain_openai import ChatOpenAI

from config import LLM_MODEL, VERBOSE, OUTPUT_DIR
from agents import (
    RequirementsAnalyst, FeasibilityExpert, ProjectPlanner,
    SeniorDeveloper, QAEngineer, CodeReviewer, E2ETester, TechnicalWriter
)
from tasks import (
    create_requirement_task, create_feasibility_task, create_planning_task,
    create_development_task, create_unit_test_task, create_review_task,
    create_e2e_test_task, create_documentation_task
)


class SDDWorkflow:
    """
    SDD (Software Design Document) 工作流程

    基于 CrewAI 的多 Agent 协同框架，
    自动化完成软件开发的全生命周期。

    使用示例:
        workflow = SDDWorkflow()
        results = workflow.run("实现一个博客系统")
    """

    def __init__(self, model: str = None):
        """
        初始化工作流程

        Args:
            model: 使用的 LLM 模型，默认从 config 读取
        """
        self.model = model or LLM_MODEL
        self.llm = ChatOpenAI(model=self.model)
        self.output_dir = None

    def run(self, requirement: str, output_dir: str = None) -> dict:
        """
        运行完整的 SDD 工作流程

        Args:
            requirement: 用户需求描述
            output_dir: 代码输出目录，默认使用 config 配置

        Returns:
            dict: 各阶段执行结果
        """
        self.output_dir = output_dir or OUTPUT_DIR

        print(f"\n{'='*60}")
        print(f"SDD Workflow 启动")
        print(f"{'='*60}")
        print(f"需求：{requirement}")
        print(f"{'='*60}\n")

        # 初始化 Agents
        print("[1/8] 初始化 Agent 团队...")
        agents = {
            'requirements': RequirementsAnalyst(self.llm).agent,
            'feasibility': FeasibilityExpert(self.llm).agent,
            'planning': ProjectPlanner(self.llm).agent,
            'development': SeniorDeveloper(self.llm).agent,
            'testing': QAEngineer(self.llm).agent,
            'review': CodeReviewer(self.llm).agent,
            'e2e': E2ETester(self.llm).agent,
            'documentation': TechnicalWriter(self.llm).agent,
        }
        print("[OK] Agent 团队就绪\n")

        # 创建 Crew
        print("[2/8] 配置工作流程...")
        crew = Crew(
            agents=list(agents.values()),
            tasks=[],
            verbose=VERBOSE,
            process=Process.sequential
        )

        # 动态构建 Tasks
        print("[3/8] 定义任务...")
        tasks = [
            create_requirement_task(agents['requirements'], requirement),
            create_feasibility_task(agents['feasibility'], "{requirements_output}"),
            create_planning_task(agents['planning'], "{feasibility_output}"),
            create_development_task(agents['development'], "{planning_output}", self.output_dir),
            create_unit_test_task(agents['testing'], "{development_output}"),
            create_review_task(agents['review'], "{development_output}"),
            create_e2e_test_task(agents['e2e'], "{review_output}"),
            create_documentation_task(agents['documentation'], "{all_outputs}", "Project"),
        ]

        crew.tasks = tasks

        # 执行工作流
        print("[4/8] 开始执行 SDD 工作流...\n")
        print(f"{'='*60}")

        result = crew.kickoff()

        print(f"{'='*60}")
        print(f"\nSDD Workflow 执行完成！")
        print(f"{'='*60}")

        return {
            "status": "completed",
            "requirement": requirement,
            "output_dir": self.output_dir,
            "result": result
        }

    def run_simple(self, requirement: str) -> str:
        """
        简化模式：仅运行需求分析 + 可行性 + 计划

        适合快速验证需求，不生成代码

        Returns:
            str: 工作流执行结果
        """
        print(f"\nSDD Workflow (简化模式)")
        print(f"需求：{requirement}\n")

        agents = [
            RequirementsAnalyst(self.llm).agent,
            FeasibilityExpert(self.llm).agent,
            ProjectPlanner(self.llm).agent,
        ]

        crew = Crew(
            agents=agents,
            tasks=[
                create_requirement_task(agents[0], requirement),
                create_feasibility_task(agents[1], "{requirements_output}"),
                create_planning_task(agents[2], "{feasibility_output}"),
            ],
            verbose=VERBOSE,
            process=Process.sequential
        )

        return crew.kickoff()


if __name__ == "__main__":
    import sys

    requirement = sys.argv[1] if len(sys.argv) > 1 else "实现一个待办事项管理应用"

    workflow = SDDWorkflow()
    results = workflow.run(requirement)

    print("\n执行结果:")
    print(results)
