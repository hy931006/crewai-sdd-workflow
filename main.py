#!/usr/bin/env python3
"""SDD Workflow CLI - 基于 CrewAI 的多 Agent 软件开发工作流工具"""

import argparse
import sys
import time

from config import LLM_MODEL, LLM_BASE_URL, LLM_API_KEY, VERBOSE, OUTPUT_DIR
from workflow import SDDWorkflow

__version__ = "0.1.0"


def build_parser():
    """构建并返回参数解析器"""
    parser = argparse.ArgumentParser(
        prog="sdd",
        description="基于 AI Agent 的软件开发工作流。输入需求描述，自动完成需求分析、"
                    "可行性评估、项目计划、代码生成、测试、代码审查和文档编写。",
        epilog="示例：\n"
               '  sdd "实现一个博客系统" --model gpt-4\n'
               '  sdd "实现一个计算器" --simple --quiet\n'
               '  sdd "实现一个 REST API" --output ./my-project\n',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "requirement",
        nargs="?",
        default="实现一个待办事项管理应用",
        help="需求描述 (默认: %(default)s)",
    )

    parser.add_argument(
        "--model",
        default=LLM_MODEL,
        help=f"LLM 模型名称 (默认: {LLM_MODEL})",
    )

    parser.add_argument(
        "--base-url",
        default=LLM_BASE_URL,
        help=f"LLM API 端点 (默认: {LLM_BASE_URL})",
    )

    parser.add_argument(
        "--output",
        default=OUTPUT_DIR,
        help=f"输出目录 (默认: {OUTPUT_DIR})",
    )

    parser.add_argument(
        "--simple",
        action="store_true",
        help="简化模式：仅需求分析 + 可行性 + 计划，不生成代码",
    )

    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument(
        "--verbose",
        action="store_true",
        help="显示详细输出",
    )
    verbosity.add_argument(
        "--quiet",
        action="store_true",
        help="抑制非必要的详细输出",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    # 校验需求
    if not args.requirement.strip():
        parser.error("需求描述不能为空")

    # 解析 verbose 设置：CLI 标志 > config 默认值
    if args.verbose:
        verbose = True
    elif args.quiet:
        verbose = False
    else:
        verbose = VERBOSE

    # --output 在 --simple 模式下无效
    if args.simple and args.output != OUTPUT_DIR:
        print("警告：--simple 模式下 --output 将被忽略", file=sys.stderr)

    # 初始化工作流
    workflow = SDDWorkflow(
        model=args.model,
        base_url=args.base_url,
        api_key=LLM_API_KEY,
    )

    # 执行
    start_time = time.time()
    try:
        if args.simple:
            print(f"\n运行 SDD Workflow（简化模式）...")
            print(f"模型：{args.model}")
            print(f"需求：{args.requirement}\n")

            result = workflow.run_simple(args.requirement, verbose=verbose)

            elapsed = time.time() - start_time
            print(f"\n完成，耗时 {elapsed:.1f}s")
            print(result)
        else:
            print(f"\n运行 SDD Workflow（完整模式）...")
            print(f"模型：  {args.model}")
            print(f"输出：  {args.output}")
            print(f"需求：  {args.requirement}\n")

            result = workflow.run(args.requirement, output_dir=args.output, verbose=verbose)

            elapsed = time.time() - start_time
            print(f"\n完成，耗时 {elapsed:.1f}s")
            print(f"输出目录：{args.output}")

    except KeyboardInterrupt:
        elapsed = time.time() - start_time
        print(f"\n已中断，已运行 {elapsed:.1f}s")
        sys.exit(1)
    except ValueError as e:
        print(f"参数错误：{e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"执行失败：{e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
