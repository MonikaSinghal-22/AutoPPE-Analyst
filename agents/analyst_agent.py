from autogen_agentchat.agents import AssistantAgent
from prompts.analyst import ANALYST_SYSTEM_PROMPT


def getAnalystAgent(model_client):
    analyst_agent = AssistantAgent(
        name='Analyst_Agent',
        model_client=model_client,
        description='An Agent that takes the cleaned dataset and generate analytical insights about PPE Compliance',  # noqa: E501
        system_message=ANALYST_SYSTEM_PROMPT
    )
    return analyst_agent
