# SDD Workflow 配置
import os

# LLM 配置
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o")
MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", "10"))
VERBOSE = os.getenv("VERBOSE", "True").lower() in ("true", "1", "yes")

# 项目配置
PROJECT_NAME = "SnakeGame"
PROJECT_ROOT = os.path.dirname(__file__)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output", PROJECT_NAME.lower())

# API Keys (从环境变量读取)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
