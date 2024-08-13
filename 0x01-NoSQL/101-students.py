#!/usr/bin/env python3
'''
This module returns all students sorted by average score
'''

from pymongo import MongoClient


def top_students(mongo_collection):
    '''
    Lists stidents sorted by average score
    '''
    pipelines = [ 
            { "$addFields": { "averageScore": {"$avg": "$scores"} } },
            { "$sort": {"averageScore": -1} } ]

    return list(mongo_collection.aggregate(pipelines))
