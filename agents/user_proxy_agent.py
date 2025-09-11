from autogen_agentchat.agents import UserProxyAgent


def getUserProxyAgent(model_client, input_func=None):
    user_proxy_agent = UserProxyAgent(
        name='UserProxy',
        description='You are a user proxy agent',
        input_func=input_func
    )
    return user_proxy_agent
