#!/usr/bin/env python3
'''
provides some stats about Nginx logs stored in MongoDB:

Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it’s a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
'''

from pymongo import MongoClient


def main():
    '''
    lists the number of logs
    '''

    client = MongoClient('mongodb://127.0.0.1:27017')
    database = client.logs
    collection = database.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    method_counts = {}
    for method in methods:
        method_counts[method] = collection.count_documents({"method": method})
    
    stat_count = collection.count_documents({"method": "GET", "path": "/status"})
    
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")

    print(f"{stat_count} status check")

    pipeline = [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
    ]
    top_ips = collection.aggregate(pipeline)

    print("IPs:")
    for ip_doc in top_ips:
        print(f"\tip {ip_doc['_id']}: {ip_doc['count']}")


if __name__ == "__main__":
    main()
