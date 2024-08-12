#!/usr/bin/env python3
'''
This module changes all topics of a school document based on the name.
'''

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    '''
    Update all topics of a school document based on the school name.

    Parameters:
    - mongo_collection: the pymongo collection object
    - name (str): the school name to update
    - topics (list of str): the list of topics to update in the school document
    '''
    mongo_collection.update_many(
            { "name" : name},
            { "$set": {"topics" : topics}}
        )
