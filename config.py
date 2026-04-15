# SDD Workflow 配置
import os

# LLM 配置
LLM_MODEL = os.getenv("LLM_MODEL", "deepseek-chat")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://api.deepseek.com")
VERBOSE = os.getenv("VERBOSE", "True").lower() in ("true", "1", "yes")

# 输出目录
PROJECT_ROOT = os.path.dirname(__file__)
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output", "snakegame")

# API Key (从环境变量读取，兼容多种 provider)
# 优先读取 LLM_API_KEY，其次兼容 OPENAI_API_KEY / DEEPSEEK_API_KEY
LLM_API_KEY = os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY") or os.getenv("DEEPSEEK_API_KEY") or ""
