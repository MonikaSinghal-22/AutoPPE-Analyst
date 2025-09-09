from autogen_agentchat.agents import UserProxyAgent

def getUserProxyAgent(model_client):
    user_proxy_agent = UserProxyAgent(
        name='UserProxy',
        description='You are a user proxy agent',
        input_func=input
    )
    return user_proxy_agent