#!/usr/bin/env python3
""" school by topic """


def schools_by_topic(mongo_collection, topic):
    """ school topics by topic variable """
    return mongo_collection.find({"topics": topic})
