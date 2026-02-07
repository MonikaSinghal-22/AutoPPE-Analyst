from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from agents.data_preparer_agent import getDataPreparerAgent
from agents.analyst_agent import getAnalystAgent
from agents.reporter_agent import getReporterAgent


def getDocumentIntelligenceTeam(model_client):
    data_preparer_agent = getDataPreparerAgent(model_client)
    analyst_agent = getAnalystAgent(model_client)
    reporter_agent = getReporterAgent(model_client)
    text_mention_termination = TextMentionTermination('STOP')

    team = RoundRobinGroupChat(
        participants=[
            data_preparer_agent,
            analyst_agent,
            reporter_agent,
        ],
        max_turns=4,
        termination_condition=text_mention_termination,
        # custom_message_types = [
        #     StructuredMessage[PreparedLog],
        #     StructuredMessage[AnalysisReport],
        #     StructuredMessage[ReportSummary]
        # ]
    )
    return team
