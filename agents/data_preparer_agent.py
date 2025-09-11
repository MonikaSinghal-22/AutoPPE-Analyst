from autogen_agentchat.agents import AssistantAgent
from prompts.data_preparer import DATA_PREPARER_SYSTEM_MESSAGE


def getDataPreparerAgent(model_client):
    data_preparer_agent = AssistantAgent(
        name='Data_Preparer_Agent',
        model_client=model_client,
        description='An Agent that collects raw PPE compliance log files and produce clean prepared log',  # noqa: E501
        system_message=DATA_PREPARER_SYSTEM_MESSAGE
    )
    return data_preparer_agent
