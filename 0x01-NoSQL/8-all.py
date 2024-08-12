#!/usr/bin/env python3
'''
This module lists all documents ina collection
'''

from pymongo import MongoClient


def list_all(mongo_collection):
    '''
    Lists all collections in a Mongodb collection

    Parameters:
    mongo_collection (pymongo.collection.Collection): The collection object to
    query.

    Returns:
    list: A list of documents in the collection. Returns an empty list if no
    documents exist.
    '''
    docs = list(mongo_collection.find())

    return docs
