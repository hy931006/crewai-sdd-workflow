"""
SDD Workflow - 多 Agent 协同软件开发生命周期
基于 CrewAI 的通用自动化软件开发框架

使用方法:
    from workflow import SDDWorkflow
    
    workflow = SDDWorkflow()
    results = workflow.run("实现一个博客系统")
"""
import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# ============== Agent 工厂函数 ==============

def create_requirements_analyst(llm):
    """创建需求分析 Agent"""
    return Agent(
        role="需求分析师",
        goal="深入分析用户需求，输出结构化、无歧义的需求规格说明书",
        backstory="""你是一位资深需求分析师，在软件行业有10年经验。
        你擅长将模糊的业务需求转化为清晰的技术规格，
        能够识别潜在风险并提出建设性建议。""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_feasibility_expert(llm):
    """创建可行性研究 Agent"""
    return Agent(
        role="可行性研究专家",
        goal="从技术、成本、时间三个维度评估项目可行性",
        backstory="""你是一位技术架构师，精通各种技术栈。
        你能够快速评估技术方案的可行性和风险，
        给出切实可行的替代方案。""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_project_planner(llm):
    """创建项目计划 Agent"""
    return Agent(
        role="项目计划师",
        goal="制定详细、可执行的项目计划和任务拆解",
        backstory="""你是一位经验丰富的项目经理（PMP认证）。
        你擅长将复杂项目拆解为可管理的小任务，
        准确评估工期和资源需求。""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_developer(llm):
    """创建开发者 Agent"""
    return Agent(
        role="高级开发工程师",
        goal="编写高质量、可维护的生产级代码",
        backstory="""你是一位全栈开发工程师，精通Python/JavaScript/Go等语言。
        你编写的代码遵循最佳实践，注重性能和安全性。""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_qa_engineer(llm):
    """创建测试工程师 Agent"""
    return Agent(
        role="测试工程师",
        goal="设计并编写全面的测试用例，确保代码质量",
        backstory="""你是一位资深QA工程师，精通测试金字塔策略。
        你编写的测试覆盖边界条件和异常场景。""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_code_reviewer(llm):
    """创建代码检视 Agent"""
    return Agent(
        role="代码检视员",
        goal="发现代码缺陷、安全漏洞和代码异味，提出改进建议",
        backstory="""你是一位代码审计专家，对代码质量有极高要求。
        你熟悉各种设计模式和重构技巧。""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_e2e_tester(llm):
    """创建端到端测试 Agent"""
    return Agent(
        role="端到端测试工程师",
        goal="设计和执行端到端测试场景，验证系统完整性",
        backstory="""你是一位E2E测试专家，熟悉用户旅程测试。
        你能够从用户角度设计测试场景。""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )

def create_technical_writer(llm):
    """创建技术文档 Agent"""
    return Agent(
        role="技术文档工程师",
        goal="编写清晰、完整的项目文档和技术规格说明",
        backstory="""你是一位专业的技术写作者。
        你的文档简洁明了，易于理解和维护。""",
        verbose=True,
        allow_delegation=False,
        llm=llm
    )


# ============== Task 工厂函数 ==============

def create_requirement_task(agent, requirement):
    """需求分析任务"""
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
        agent=agent,
        expected_output="结构化需求规格说明书，包含功能清单、数据模型、接口定义"
    )

def create_feasibility_task(agent, requirements_output):
    """可行性研究任务"""
    return Task(
        description=f"""基于以下需求，进行可行性研究：
        
        需求分析结果：{requirements_output}
        
        研究维度：
        1. 技术可行性：现有技术栈能否支持？
        2. 成本效益：投入产出比是否合理？
        3. 时间可行性：工期是否可控？
        
        输出三维度评分（1-10分）和综合建议""",
        agent=agent,
        expected_output="可行性报告，包含技术、成本、时间三个维度的评分和建议"
    )

def create_planning_task(agent, feasibility_output):
    """计划拆解任务"""
    return Task(
        description=f"""基于可行性研究结果，制定详细的项目计划：
        
        可行性报告：{feasibility_output}
        
        要求：
        1. WBS 工作分解结构
        2. 每个任务的工期估算
        3. 任务依赖关系
        4. 关键路径识别
        
        输出格式：任务列表，包含ID、名称、工期、依赖""",
        agent=agent,
        expected_output="WBS 任务分解表，包含任务ID、名称、工期和依赖关系"
    )

def create_development_task(agent, planning_output, project_name):
    """代码实现任务"""
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

def create_unit_test_task(agent, development_output):
    """单元测试任务"""
    return Task(
        description=f"""为已实现的代码编写单元测试：
        
        开发产出：{development_output}
        
        要求：
        1. 测试覆盖率 >= 80%
        2. 覆盖正常和异常场景
        3. 使用 pytest 框架
        4. 包含测试数据和预期结果
        
        输出：test_*.py 测试文件""",
        agent=agent,
        expected_output="完整的单元测试文件，覆盖核心功能"
    )

def create_review_task(agent, development_output):
    """代码检视任务"""
    return Task(
        description=f"""检视已开发的代码：
        
        代码内容：{development_output}
        
        检视维度：
        1. 代码质量（可读性、可维护性）
        2. 安全性（注入、认证、授权）
        3. 性能问题
        4. 设计模式应用
        
        输出：问题清单和改进建议""",
        agent=agent,
        expected_output="代码检视报告，列出发现的问题和优先级"
    )

def create_e2e_test_task(agent, review_output):
    """端到端测试任务"""
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

def create_documentation_task(agent, all_outputs, project_name):
    """文档编写任务"""
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
        expected_output="完整的项目文档集：README、DESIGN、API等"
    )


# ============== SDD Workflow 主类 ==============

class SDDWorkflow:
    """
    SDD (Software Design Document) 工作流程
    
    基于 CrewAI 的多 Agent 协同框架，
    自动化完成软件开发的全生命周期。
    
    使用示例:
        workflow = SDDWorkflow(api_key="your-openai-key")
        results = workflow.run("实现一个博客系统")
    """
    
    def __init__(self, model: str = "gpt-4o", api_key: str = None):
        """
        初始化工作流程
        
        Args:
            model: 使用的 LLM 模型，默认 gpt-4o
            api_key: OpenAI API Key，默认从环境变量读取
        """
        self.model = model
        self.llm = ChatOpenAI(model=model, api_key=api_key)
        self.phase_results = {}
        self.output_dir = None
    
    def run(self, requirement: str, output_dir: str = "./output") -> dict:
        """
        运行完整的 SDD 工作流程
        
        Args:
            requirement: 用户需求描述
            output_dir: 代码输出目录
            
        Returns:
            dict: 各阶段执行结果
        """
        self.output_dir = output_dir
        
        print(f"\n{'='*60}")
        print(f"🚀 SDD Workflow 启动")
        print(f"{'='*60}")
        print(f"📝 需求: {requirement}")
        print(f"{'='*60}\n")
        
        # 创建 Agents
        print("[1/8] 初始化 Agent 团队...")
        agents = {
            'requirements': create_requirements_analyst(self.llm),
            'feasibility': create_feasibility_expert(self.llm),
            'planning': create_project_planner(self.llm),
            'development': create_developer(self.llm),
            'testing': create_qa_engineer(self.llm),
            'review': create_code_reviewer(self.llm),
            'e2e': create_e2e_tester(self.llm),
            'documentation': create_technical_writer(self.llm),
        }
        print("[OK] Agent 团队就绪\n")
        
        # 创建 Crew（顺序执行）
        print("[2/8] 配置工作流程...")
        crew = Crew(
            agents=list(agents.values()),
            tasks=[],  # 动态添加 tasks
            verbose=True,
            process=Process.sequential  # 顺序执行，确保依赖关系
        )
        
        # 定义任务
        print("[3/8] 定义任务...")
        tasks = [
            Task(
                description=f"分析需求并输出规格说明书：{requirement}",
                agent=agents['requirements'],
                expected_output="结构化需求规格说明书"
            ),
            Task(
                description="评估项目可行性（技术/成本/时间）",
                agent=agents['feasibility'],
                expected_output="可行性报告，三维度评分"
            ),
            Task(
                description="制定详细的项目计划和工作分解",
                agent=agents['planning'],
                expected_output="WBS 任务分解表"
            ),
            Task(
                description="实现代码，输出到 {output_dir}",
                agent=agents['development'],
                expected_output="完整项目代码"
            ),
            Task(
                description="编写单元测试",
                agent=agents['testing'],
                expected_output="测试文件和覆盖率报告"
            ),
            Task(
                description="代码检视并提出改进建议",
                agent=agents['review'],
                expected_output="代码检视报告"
            ),
            Task(
                description="执行端到端测试",
                agent=agents['e2e'],
                expected_output="E2E 测试报告"
            ),
            Task(
                description="编写项目文档",
                agent=agents['documentation'],
                expected_output="README、设计文档等"
            ),
        ]
        
        crew.tasks = tasks
        
        # 执行工作流
        print("[4/8] 开始执行 SDD 工作流...\n")
        print(f"{'='*60}")
        
        result = crew.kickoff()
        
        print(f"{'='*60}")
        print(f"\n✅ SDD Workflow 执行完成！")
        print(f"{'='*60}")
        
        return {
            "status": "completed",
            "requirement": requirement,
            "output_dir": output_dir,
            "result": result
        }
    
    def run_simple(self, requirement: str) -> str:
        """
        简化模式：仅运行需求分析和计划
        
        适合快速验证需求，不生成代码
        
        Returns:
            str: 工作流执行结果
        """
        print(f"\n🚀 SDD Workflow (简化模式)")
        print(f"📝 需求: {requirement}\n")
        
        # 仅创建前 3 个 Agent
        agents = [
            create_requirements_analyst(self.llm),
            create_feasibility_expert(self.llm),
            create_project_planner(self.llm),
        ]
        
        crew = Crew(
            agents=agents,
            tasks=[
                Task(
                    description=f"分析需求：{requirement}",
                    agent=agents[0],
                    expected_output="需求规格说明书"
                ),
                Task(
                    description="可行性研究",
                    agent=agents[1],
                    expected_output="可行性报告"
                ),
                Task(
                    description="制定项目计划",
                    agent=agents[2],
                    expected_output="项目计划"
                ),
            ],
            verbose=True,
            process=Process.sequential
        )
        
        return crew.kickoff()


# ============== 命令行入口 ==============

if __name__ == "__main__":
    import sys
    
    requirement = sys.argv[1] if len(sys.argv) > 1 else "实现一个待办事项管理应用"
    
    workflow = SDDWorkflow()
    results = workflow.run(requirement)
    
    print("\n📊 执行结果:")
    print(results)
