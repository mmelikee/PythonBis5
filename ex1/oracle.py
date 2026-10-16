import os

from dotenv import load_dotenv

load_dotenv()

mode = os.getenv("MATRIX_MODE", "development")
database_url = os.getenv("DATABASE_URL", "localhost")
api_key = os.getenv("API_KEY", "")
log_level = os.getenv("Log_LEVEL", "INFO")
zion_endpoint = os.getenv("ZION_ENDPOINT", "")

print("ORACLE STATUS: Consulting the configuration...")
print()
print("Configuration loaded:")
print(f"Mode: {mode}")
print(f"Database: {database_url}")
print(f"API Access: {'Authenticated' if api_key else 'Not authenticated'}")
print(f"Log Level: {log_level}")
print(f"Remote Network: {'Online' if zion_endpoint else 'Offline'}")
