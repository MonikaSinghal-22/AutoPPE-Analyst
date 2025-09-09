from autogen_agentchat.agents import AssistantAgent
from prompts.analyst import ANALYST_SYSTEM_PROMPT
from schemas.analysis_report import AnalysisReport

def getAnalystAgent(model_client):
    analyst_agent = AssistantAgent(
        name='Analyst_Agent',
        model_client=model_client,
        description='An Agent that takes the cleaned dataset and generate analytical insights about PPE Compliance',
        system_message=ANALYST_SYSTEM_PROMPT,
        #output_content_type=AnalysisReport
    )
    return analyst_agent