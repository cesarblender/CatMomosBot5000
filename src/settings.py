import os

BOT_POST_FREQUENCY = 120 * 3 # Each 3 hours

FB_SDK_TOKEN = os.getenv("TOKEN")
FIREBASE_ADMIN_CERT = os.getenv("FIREBASE_ADMIN_CERT")
FIREBASE_STORAGE_LINK = os.getenv("STORAGE_LINK")
HUGGINGFACE_API_KEY = os.getenv("HF_API_KEY")