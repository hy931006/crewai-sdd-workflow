# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CrewAI SDD Workflow - A multi-agent collaborative software development lifecycle (SDD) framework based on CrewAI. It automates the full software development process from requirements analysis to documentation generation.

## Architecture

### Core Components

```
main.py              # CLI entry point with argparse
workflow.py          # Main workflow orchestration - defines 8 agents and their task sequence
config.py            # Centralized LLM config (LLM_API_KEY, LLM_MODEL, LLM_BASE_URL) and paths
agents/              # Modular agent definitions (one file per agent type)
  ├── __init__.py
  ├── requirements.py
  ├── feasibility.py
  ├── planner.py
  ├── developer.py
  ├── qa.py
  ├── reviewer.py
  ├── e2e_tester.py
  └── writer.py
tasks/               # Task factory functions (one file per stage)
  ├── __init__.py
  ├── requirement.py
  ├── feasibility.py
  ├── planning.py
  ├── development.py
  ├── testing.py
  ├── review.py
  ├── e2e.py
  └── documentation.py
output/              # Generated projects from workflow execution
```

### Agent Team (8 specialists)

| Agent | Responsibility |
|-------|----------------|
| 需求分析师 (Requirements Analyst) | Requirements analysis, specification documents |
| 可行性专家 (Feasibility Expert) | Technical/cost/time assessment |
| 项目计划师 (Project Planner) | WBS breakdown, task planning |
| 开发工程师 (Developer) | Code implementation |
| 测试工程师 (QA Engineer) | Unit test creation |
| 代码检视员 (Code Reviewer) | Code audit |
| E2E 测试师 (E2E Tester) | End-to-end testing |
| 文档工程师 (Technical Writer) | Documentation |

### Workflow Pipeline

```
Requirements → Feasibility → Planning → Development → Testing → Review → E2E Test → Documentation
```

The workflow uses `Process.sequential` execution in CrewAI to ensure proper task dependencies.

## Commands

### Setup
```bash
pip install -r requirements.txt
```

### Environment
```bash
export LLM_API_KEY="your-api-key"
# Optional provider overrides:
# export LLM_BASE_URL="https://api.openai.com"
# export LLM_MODEL="gpt-4o"  # Default: deepseek-chat
```

### Run Full Workflow
```bash
# CLI (recommended)
python main.py "实现一个博客系统"
python main.py "实现一个博客系统" --model gpt-4o --base-url https://api.openai.com
python main.py "实现一个博客系统" --simple  # 仅需求分析+可行性+计划
python main.py "实现一个博客系统" --output ./my-project
python main.py --help
python main.py --version
```

### Python API
```python
from workflow import SDDWorkflow

workflow = SDDWorkflow()
results = workflow.run("实现一个博客系统")

# Simplified mode
result = workflow.run_simple("实现一个待办事项应用")
```

### Run Tests
```bash
pytest                                    # Run all tests
pytest -v                                 # Verbose output
pytest --cov=. --cov-report=html          # With coverage report
```

## Key Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `LLM_API_KEY` | (空) | API Key，兼容 OpenAI/DeepSeek/其他 |
| `LLM_MODEL` | `deepseek-chat` | 模型名称 |
| `LLM_BASE_URL` | `https://api.deepseek.com` | API 端点 |
| `VERBOSE` | `True` | 详细日志 |

## Development Notes

- `config.py` 中 `LLM_API_KEY` 按优先级回退读取：`LLM_API_KEY` → `OPENAI_API_KEY` → `DEEPSEEK_API_KEY`
- 所有 Agent 通过 `agents/__init__.py` 集中导出
- 所有 Task 通过 `tasks/__init__.py` 集中导出
- `main.py` 为唯一 CLI 入口，`workflow.py` 仅保留 Python API
- `workflow.py` 的 `run()` 和 `run_simple()` 接受 `verbose` 参数覆盖 config 默认值
- 生成项目输出到 `output/{project_name}/`
