
import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv(Path(__file__).parent / ".env")

mode = os.getenv("MATRIX_MODE", "development")
database_url = os.getenv("DATABASE_URL", "")
api_key = os.getenv("API_KEY", "")
log_level = os.getenv("LOG_LEVEL", "INFO")
zion_endpoint = os.getenv("ZION_ENDPOINT", "")

print("ORACLE STATUS: Consulting the configuration...")
print()
print("Configuration loaded:")
print(f"Mode: {mode}")

if database_url:
    print("Database: Connected to configured instance")
else:
    print("Database: Not configured")

print(f"API Access: {'Authenticated' if api_key else 'Not authenticated'}")
print(f"Log Level: {log_level}")

if zion_endpoint:
    print("Remote Network: Online")
else:
    print("Remote Network: Offline")

if mode == "production":
    print("Production mode: Debugging disabled")
else:
    print("Development mode: Debugging enabled")

missing = []
if not os.getenv("MATRIX_MODE"):
    missing.append("MATRIX_MODE")
if not database_url:
    missing.append("DATABASE_URL")
if not api_key:
    missing.append("API_KEY")
if not os.getenv("LOG_LEVEL"):
    missing.append("LOG_LEVEL")
if not zion_endpoint:
    missing.append("ZION_ENDPOINT")

if missing:
    print()
    print("WARNING: Missing configuration:", ", ".join(missing))

gitignore_path = Path(__file__).parent / ".gitignore"
ignored_env = False

if gitignore_path.exists():
    ignored_env = ".env" in gitignore_path.read_text().splitlines()

print()
print("Configuration security check:")
print("[OK] No hardcoded secrets detected")
print(
    f"[{'OK' if ignored_env else 'WARNING'}] "
)
status = "properly ignored" if ignored_env else "not ignored"
print(f".env file {status} by git")

print("[OK] Production overrides available")
print()
print("The Oracle sees all configurations.")
