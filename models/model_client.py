from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constants import MODEL_GEMINI
from autogen_core.models import ModelInfo
import os

def get_model_client():
    gemini_model_client = OpenAIChatCompletionClient(
        model="gemini-2.5-pro",
        model_info=ModelInfo(vision=True, function_calling=True, json_output=True, family="unknown", structured_output=True),
        api_key=os.getenv('GEMINI_API_KEY')
    )
    return gemini_model_client