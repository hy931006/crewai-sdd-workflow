#!/usr/bin/env python3
"""SDD Workflow CLI 入口"""
import sys
from workflow import SDDWorkflow


def main():
    """CLI 入口函数"""
    requirement = sys.argv[1] if len(sys.argv) > 1 else "实现一个待办事项管理应用"

    workflow = SDDWorkflow()
    try:
        results = workflow.run(requirement)
        print("\n执行结果:")
        print(results)
    except KeyboardInterrupt:
        print("\n用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"执行失败：{e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
