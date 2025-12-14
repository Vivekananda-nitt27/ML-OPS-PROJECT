from pymongo import MongoClient
import os

# uri =  os.getenv("MONGODB_URL")
mongo_db_url = os.getenv(MONGODB_URL_KEY)

# "mongodb+srv://vivekkunal3432:Vivekananda1196@cluster0.mgprnqy.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(uri)
    client.admin.command("ping")
    print(uri)
    print("Login Success")
except Exception as e:
    print("Login Failed:", e)
    print(uri)
