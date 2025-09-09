from autogen_agentchat.agents import AssistantAgent
from prompts.data_preparer import DATA_PREPARER_SYSTEM_MESSAGE
from schemas.prepared_log import PreparedLog

def getDataPreparerAgent(model_client):
    data_preparer_agent = AssistantAgent(
        name='Data_Preparer_Agent',
        model_client=model_client,
        description='An Agent that collects raw PPE compliance log files and produce clean prepared log',
        system_message=DATA_PREPARER_SYSTEM_MESSAGE,
        #output_content_type=PreparedLog
    )
    return data_preparer_agent