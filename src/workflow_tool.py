from dotenv import load_dotenv
from strands import Agent
from strands_tools import workflow

load_dotenv()

# Create an agent with workflow capability
agent = Agent(tools=[workflow])

# Create a multi-agent workflow
agent.tool.workflow(
    action="create",
    workflow_id="data_analysis",
    tasks=[
        {
            "task_id": "data_extraction",
            "description": "四半期レポートから主要な財務データを抽出する",
            "system_prompt": "あなたはレポートから財務データを抽出して構造化します。",
            "priority": 5,
        },
        {
            "task_id": "trend_analysis",
            "description": "前四半期と比較してデータのトレンドを分析する",
            "dependencies": ["data_extraction"],
            "system_prompt": "あなたは財務時系列データのトレンドを特定します。",
            "priority": 3,
        },
        {
            "task_id": "report_generation",
            "description": "包括的な分析レポートを生成する",
            "dependencies": ["trend_analysis"],
            "system_prompt": "あなたは明確な財務分析レポートを作成します。",
            "priority": 2,
        },
    ],
)

# Execute workflow (parallel processing where possible)
agent.tool.workflow(action="start", workflow_id="data_analysis")

# Check results
status = agent.tool.workflow(action="status", workflow_id="data_analysis")
