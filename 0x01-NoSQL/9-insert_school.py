#!/usr/bin/env python3
'''
This module inserts a new document in a collection based on kwargs
'''

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    '''
    Inserts a new document into a collection

    Parameters:
    mongo_collection (pymongo.collection.Collection): The collection object to
    query

    kwargs: allows for variable number of argument

    Returns:
    A new _id
    '''

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
