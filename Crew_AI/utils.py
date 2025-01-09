import os
from dotenv import load_dotenv

def load_env(file_path='/content/.env'):
    """
    Load environment variables from a specified .env file.

    Args:
        file_path (str): The path to the .env file. Defaults to '/content/.env'.
    """
    load_dotenv(file_path)

def get_openai_api_key():
    """
    Retrieves the OpenAI API key from environment variables.
    
    Returns:
        str: The OpenAI API key if set, otherwise None.
    """
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key:
        return openai_api_key
    else:
        print("OpenAI API key not found")
    return ""


def get_hf_token():
    """
    Retrieves the HF TOKEN from environment variables.
    
    Returns:
        str: The HF TOKEN  if set, otherwise None.
    """
    hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    if hf_token:
        return hf_token
    else:
        print("HF TOKEN not found")
    return ""


def get_serper_key():
    """
    Retrieves the Serper API Key from environment variables.
    
    Returns:
        str: The Serper API Key  if set, otherwise None.
    """
    serper_api_key = os.getenv("SERPER_API_KEY")
    if serper_api_key:
        return serper_api_key
    else:
        print("Serper API Key not found")
    return ""