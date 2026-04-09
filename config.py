# SDD Workflow 配置
import os

# LLM 配置
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

# 工作流配置
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o")
MAX_ITERATIONS = 10
VERBOSE = True

# 项目配置
PROJECT_NAME = "SnakeGame"
PROJECT_PATH = os.path.join(os.path.dirname(__file__), "output", PROJECT_NAME.lower())
