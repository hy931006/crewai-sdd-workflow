# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

CrewAI SDD Workflow - A multi-agent collaborative software development lifecycle (SDD) framework based on CrewAI. It automates the full software development process from requirements analysis to documentation generation.

## Architecture

### Core Components

```
workflow.py          # Main workflow orchestration - defines 8 agents and their task sequence
config.py            # Centralized configuration for LLM settings and project paths
agents/              # Modular agent definitions (one file per agent type)
  ├── developer.py   # Code implementation agent
  ├── planner.py     # Project planning and task breakdown
  ├── reviewer.py    # Code review and quality assurance
  ├── tester.py      # Unit and integration testing
  └── writer.py      # Technical documentation
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
export OPENAI_API_KEY="your-api-key"
# Optional: export LLM_MODEL="gpt-4o"  # Default
```

### Run Full Workflow
```bash
# Command line
python workflow.py "实现一个博客系统"

# Python API
from workflow import SDDWorkflow
workflow = SDDWorkflow()
results = workflow.run("实现一个博客系统")
```

### Run Simplified Mode (Requirements + Planning only)
```python
from workflow import SDDWorkflow
workflow = SDDWorkflow()
result = workflow.run_simple("实现一个待办事项应用")
```

### Run Tests
```bash
pytest                                    # Run all tests
pytest -v                                 # Verbose output
pytest --cov=. --cov-report=html          # With coverage report
pytest output/snakegame/test_game.py      # Run single test file
```

### Run Generated Projects
```bash
cd output/snakegame
python main.py                            # Run Snake game example
```

## Key Configuration

- **LLM_MODEL**: Model selection (default: gpt-4o)
- **MAX_ITERATIONS**: Maximum workflow iterations (default: 10)
- **VERBOSE**: Enable detailed logging (default: True)
- **PROJECT_NAME**: Name for generated projects
- **PROJECT_PATH**: Output directory for generated code

## Development Notes

- All agents are created via factory functions in `workflow.py` with shared LLM instance
- Agents module (`agents/`) provides reusable, class-based agent definitions
- Workflow supports both full SDD cycle and simplified (requirements-only) mode
- Generated projects are output to `output/{project_name}/` directory
