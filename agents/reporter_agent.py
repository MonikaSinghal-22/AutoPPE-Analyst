from autogen_agentchat.agents import AssistantAgent
from prompts.reporter import REPORTER_SYSTEM_MESSAGE
from schemas.report_summary import ReportSummary

def getReporterAgent(model_client):
    reporter_agent = AssistantAgent(
        name='Reporter_Agent',
        model_client=model_client,
        description='An Agent to take structured insights from AnalystAgent (AnalysisReport) and produce a stakeholder-ready summary',
        system_message=REPORTER_SYSTEM_MESSAGE,
        #output_content_type=ReportSummary
    )
    return reporter_agent