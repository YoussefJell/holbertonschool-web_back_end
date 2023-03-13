#!/usr/bin/env python3
""" list all collections """


def list_all(mongo_collection):
    """ lists all docs """
    if mongo_collection is not None:
        return []
    return list(mongo_collection.find())
