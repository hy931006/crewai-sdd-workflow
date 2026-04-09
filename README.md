# CrewAI SDD Workflow

基于 CrewAI 的多 Agent 协同软件开发生命周期 (SDD) 框架。

## 特性

- 🤖 **8 个专业 Agent**: 需求分析、可行性研究、计划拆解、代码实现、单元测试、代码检视、端到端测试、文档编写
- 🔄 **自动化工作流**: 从需求到文档的全流程自动化
- 🎮 **示例项目**: 包含贪吃蛇游戏作为示例

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行 SDD 工作流

```bash
python workflow.py
```

### 运行示例游戏

```bash
cd output/snakegame
pip install -r requirements.txt
python main.py
```

## Agent 角色

| Agent | 职责 |
|-------|------|
| Requirements Analyst | 需求分析 |
| Feasibility Expert | 可行性研究 |
| Project Planner | 计划拆解 |
| Senior Developer | 代码实现 |
| QA Engineer | 单元测试 |
| Code Reviewer | 代码检视 |
| E2E Tester | 端到端测试 |
| Technical Writer | 文档编写 |

## 工作流程

```
需求输入 → 需求分析 → 可行性研究 → 计划拆解
                                            ↓
                         ← 单元测试 ← 代码实现 ←
                              ↓           ↓
                         代码检视    端到端测试
                                      ↓
                                 文档编写
```

## 配置

在运行前设置环境变量：

```bash
export OPENAI_API_KEY="your-api-key"
# 或
export ANTHROPIC_API_KEY="your-api-key"
```

## License

MIT License - see [LICENSE](LICENSE) 文件
