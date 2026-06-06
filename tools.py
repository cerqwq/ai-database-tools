"""
AI Database Tools - AI数据库工具
支持数据库设计、查询优化、迁移
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIDatabaseTools:
    """
    AI数据库工具
    支持：设计、查询、迁移
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_schema(self, requirements: str, db_type: str = "PostgreSQL") -> Dict:
        """设计数据库Schema"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请设计{db_type}数据库Schema：

需求：{requirements}

请返回JSON格式：
{{
    "tables": [
        {{"name": "表名", "columns": [{{"name": "列", "type": "类型"}}], "indexes": ["索引"]}}
    ],
    "relationships": ["关系"],
    "sql": "DDL语句"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"schema": content}

    def optimize_query(self, query: str, schema: str = "") -> Dict:
        """优化查询"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请优化以下SQL查询：

Schema：{schema[:500]}
查询：{query}

请返回JSON格式：
{{
    "optimized_query": "优化后的查询",
    "issues": ["问题"],
    "indexes": ["建议索引"],
    "improvements": ["改进"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"optimization": content}

    def generate_migration(self, old_schema: str, new_schema: str, db_type: str = "PostgreSQL") -> str:
        """生成迁移"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{db_type}数据库迁移：

旧Schema：{old_schema[:500]}
新Schema：{new_schema[:500]}

要求：
1. 升级脚本
2. 降级脚本
3. 数据迁移"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_orm_models(self, schema: str, framework: str = "SQLAlchemy") -> str:
        """生成ORM模型"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{framework} ORM模型：

Schema：{schema[:1000]}

要求：
1. 完整模型
2. 关系映射
3. 类型提示"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_seed_data(self, schema: str, count: int = 10) -> str:
        """生成种子数据"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{count}条种子数据：

Schema：{schema[:1000]}

要求：
1. 真实感数据
2. 符合约束
3. SQL INSERT语句"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def analyze_performance(self, metrics: Dict) -> Dict:
        """分析性能"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        metrics_text = json.dumps(metrics, ensure_ascii=False)

        prompt = f"""请分析数据库性能：

{metrics_text}

请返回JSON格式：
{{
    "bottlenecks": ["瓶颈"],
    "recommendations": ["建议"],
    "index_suggestions": ["索引建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"performance": content}

    def compare_databases(self, requirements: List[str]) -> Dict:
        """比较数据库"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        req_text = ", ".join(requirements)

        prompt = f"""请比较数据库：

需求：{req_text}

请返回JSON格式：
{{
    "databases": [
        {{"name": "数据库", "strengths": ["优势"], "weaknesses": ["劣势"], "use_cases": ["适用场景"]}}
    ],
    "recommendation": "推荐"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"comparison": content}


def create_tools(**kwargs) -> AIDatabaseTools:
    """创建数据库工具"""
    return AIDatabaseTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Database Tools")
    print()

    # 测试
    schema = tools.design_schema("电商系统，用户、订单、商品", "PostgreSQL")
    print(json.dumps(schema, ensure_ascii=False, indent=2))
