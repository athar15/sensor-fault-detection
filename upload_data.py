from pymongo.mongo_client import MongoClient
import pandas as pd
import json


# uri
uri = "mongodb+srv://atharimam81:Athar123@cluster2.v1z74.mongodb.net/?retryWrites=true&w=majority&appName=Cluster2"

# create new client and connect to server
client = MongoClient(uri)

# create a database name and collection name

DATABASE_NAME = "sensor"
COLLECTION_NAME = "waferfault"


df = pd.read_csv("E:\SENSORPROJECT\notebooks\wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0", axis = 1)

json_record = list(json.loads(df.T.to_json()).values())


client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)