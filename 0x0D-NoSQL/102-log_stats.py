#!/usr/bin/env python3
""" provides some log data """
from pymongo import MongoClient

if __name__ == "__main__":
    """ logs db and nginx collection hence client.logs.nginx """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f'{status_check} status check')

    ips = nginx_collection.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": 1,
            "count": 1
        }}
    ])

    print("IPs:")
    for top_ips in ips:
        print(f'\t{top_ips.get("ip")}: {top_ips.get("count")}')
