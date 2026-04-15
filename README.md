# CrewAI SDD Workflow

🤖 基于 CrewAI 的多 Agent 协同软件开发生命周期 (SDD) 框架

## 特性

- **8 个专业 Agent** - 各司其职的 AI 开发团队
- **全流程自动化** - 从需求到文档一键完成
- **可扩展架构** - 轻松添加自定义 Agent 和工具
- **灵活执行** - 支持完整流程或简化模式

## Agent 团队

| Agent | 职责 | 输出 |
|-------|------|------|
| 需求分析师 | 需求分析、规格说明书 | 需求文档 |
| 可行性专家 | 技术/成本/时间评估 | 可行性报告 |
| 项目计划师 | WBS 分解、任务规划 | 项目计划 |
| 开发工程师 | 代码实现 | 项目代码 |
| 测试工程师 | 单元测试编写 | 测试文件 |
| 代码检视员 | 代码审计 | 检视报告 |
| E2E 测试师 | 端到端测试 | 测试报告 |
| 文档工程师 | 技术文档编写 | 完整文档 |

## 安装

```bash
pip install -r requirements.txt

# 设置 API Key（支持多种 provider）
export LLM_API_KEY="your-api-key"
# 可选：export LLM_BASE_URL="https://your-api-endpoint"
export LLM_MODEL="deepseek-chat"  # 可选，默认 deepseek-chat
```

## 快速开始

### 方式 1：Python API

```python
from workflow import SDDWorkflow

# 初始化工作流
workflow = SDDWorkflow()

# 运行完整 SDD 流程
results = workflow.run("实现一个博客系统")

# 或运行简化模式（仅需求分析和计划）
result = workflow.run_simple("实现一个待办事项应用")
```

### 方式 2：命令行

```bash
python workflow.py "实现一个电商网站"
```

## 工作流程

```
用户需求
    ↓
┌─────────────────────────────────────────────────────────────┐
│                     SDD Workflow                             │
│                                                              │
│  需求分析 → 可行性研究 → 计划拆解 → 代码实现                  │
│       ↑                                    ↓                  │
│       ←────── 测试失败 ─────── 代码检视 ←──                   │
│       ↓                                                      │
│    E2E 测试 → 文档编写                                        │
└─────────────────────────────────────────────────────────────┘
    ↓
项目产出
```

## 项目结构

```
crewai-sdd-workflow/
├── workflow.py              # SDD Workflow 主程序（通用）
├── config.py                # 配置文件
├── requirements.txt         # 依赖
├── agents/                  # Agent 定义
│   ├── __init__.py
│   ├── developer.py
│   ├── planner.py
│   ├── reviewer.py
│   ├── tester.py
│   └── writer.py
└── output/                  # 示例项目（可删除）
    └── snakegame/
```

## 工作流 vs 示例

- **`workflow.py`** - 通用框架，接收任意需求
- **`output/snakegame/`** - 仅作为功能示例，展示工作流能生成什么

你可以：
1. 直接运行 `workflow.py`，实现你自己的项目
2. 查看 `output/snakegame/` 了解工作流产出的样子

## 自定义 Agent

```python
from crewai import Agent
from langchain_openai import ChatOpenAI

def create_custom_agent():
    return Agent(
        role="你的角色",
        goal="你的目标",
        backstory="你的背景故事",
        verbose=True,
        llm=ChatOpenAI(model="gpt-4o")
    )
```

## 配置

在 `.env` 文件中配置：

```bash
LLM_API_KEY=your-api-key
LLM_MODEL=gpt-4o  # 可选，默认 deepseek-chat
LLM_BASE_URL=https://api.openai.com  # 可选，默认 https://api.deepseek.com
```

## License

MIT License
