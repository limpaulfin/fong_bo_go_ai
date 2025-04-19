"""
Module chứa các cấu hình và hằng số của ứng dụng.
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
DOUBLE_SPACE_THRESHOLD = 0.2
TEMPERATURE = 0.5
LOG_FOLDER = "logs"
RAG_CONTEXT_FOLDER = "rag_context"
MY_PROMPT = "my_prompt.md"
API_LOG_FILE = os.path.join(LOG_FOLDER, "api_responses.jsonl")
TOKEN_STATS_FILE = os.path.join(LOG_FOLDER, "token_stats.json")

# API Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
MODEL_NAME = "gpt-4o-mini"

# Đảm bảo các thư mục tồn tại
os.makedirs(LOG_FOLDER, exist_ok=True)
os.makedirs(RAG_CONTEXT_FOLDER, exist_ok=True)

# Application Info
APP_NAME = "Bộ Gõ AI"
APP_VERSION = "1.0.0"
APP_AUTHOR = "IRONTAN Vietnam Limited"
ICON_PATH = "icon.png"
