from pydantic import BaseSettings
from dotenv import load_dotenv
import os
print(os.getcwd())
load_dotenv()

class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str = "test@test.de"