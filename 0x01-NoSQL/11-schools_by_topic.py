#!/usr/bin/env python3
'''
This module returns the list of school having a specific topic
'''

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    '''
    Lists schools by topic

    Parameters:
    mongo_collection: a mongo collection object

    topic: topic to display

    Returns:
    A list of schools with specific topics
    '''
    return list(mongo_collection.find({"topic": topic}))
