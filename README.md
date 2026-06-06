# 🗄️ AI Database Tools

AI数据库工具，支持数据库设计、查询优化、迁移。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ 数据库Schema设计
- ⚡ 查询优化
- 🔄 迁移生成
- 🏗️ ORM模型生成
- 🌱 种子数据生成
- 📊 性能分析

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_database_tools import create_tools

tools = create_tools()

# Schema设计
schema = tools.design_schema("电商系统", "PostgreSQL")

# 查询优化
optimized = tools.optimize_query(query, schema)

# 迁移生成
migration = tools.generate_migration(old_schema, new_schema)

# ORM模型
orm = tools.generate_orm_models(schema, "SQLAlchemy")

# 种子数据
seed = tools.generate_seed_data(schema, 100)

# 性能分析
performance = tools.analyze_performance(metrics)
```

## 📁 项目结构

```
ai-database-tools/
├── tools.py       # 数据库工具核心
└── README.md
```

## 📄 许可证

MIT License
