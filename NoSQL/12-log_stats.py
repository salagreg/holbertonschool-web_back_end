#!/usr/bin/env python3
"""Module qui affiche des statistiques sur les logs stockés dans MongoDB"""


from pymongo import MongoClient


client = MongoClient()
db = client.logs
collection = db.nginx

total_logs = collection.count_documents({})

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({
    "method": method}) for method in methods}

get_status_count = collection.count_documents({
    "method": "GET", "path": "/status"
    })

print(f"{total_logs} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{get_status_count} status check")
