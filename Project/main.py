import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
print(f"เชื่อมต่อด้วย Key: {api_key}") # สำหรับทดสอบ
