import json

from config import config

from langchain.schema.language_model import BaseLanguageModel

prompt = """
Translate the following json map to {language}. Keep the keys unchanged.
{messages}

RESULT:

"""

system_messages = {
    "welcome": "Appilot: What can I help?",
    "ai_reasoning": "Appilot reasoning:",
    "response_prefix": "Appilot:",
    "ask_approval":"""
The following action requires approval:

Input:
{input}

Action: 
{tool_name}
 
Do you approve the above action?
Anything except 'Y'/'Yes' (case-insensitive) will be treated as a no.
""",
}

def init_system_messages(llm:BaseLanguageModel):
    language = config.CONFIG.natural_language
    if language.lower() in ("en", "english"):
        return
    
    global system_messages
    system_messages_string = json.dumps(system_messages, ensure_ascii=False)
    result = llm.predict(prompt.format(language=language,messages=system_messages_string))
    translated = json.loads(result)
    system_messages = translated

def get(key):
    return system_messages[key]