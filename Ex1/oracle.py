import os

from dotenv import load_dotenv

load_dotenv()

mode = os.getenv("MATRIX_MODE", "development")
database_url = os.getenv("DATABASE_URL", "localhost")
api_key = os.getenv("API_KEY", "")
log_level = os.getenv("Log_LEVEL", "INFO")
zion_endpoint = os.getenv("ZION_ENDPOINT", "")
     