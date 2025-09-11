from autogen_agentchat.agents import AssistantAgent
from prompts.reporter import REPORTER_SYSTEM_MESSAGE


def getReporterAgent(model_client):
    reporter_agent = AssistantAgent(
        name='Reporter_Agent',
        model_client=model_client,
        description='An Agent to take structured insights from AnalystAgent (AnalysisReport) and produce a stakeholder-ready summary',  # noqa: E501
        system_message=REPORTER_SYSTEM_MESSAGE,
    )
    return reporter_agent
