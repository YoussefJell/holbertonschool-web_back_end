#!/usr/bin/env python3
""" Updates a document """


def update_topics(mongo_collection, name, topics):
    """ updates a document """
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
