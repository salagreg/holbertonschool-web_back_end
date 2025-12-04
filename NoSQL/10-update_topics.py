#!/usr/bin/env python3
""" Met à jour le champ 'topics' d'un document
        dans une collection MongoDB """


from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """ Met à jour le champ 'topics' d'un document
            dans une collection MongoDB """

    if not isinstance(topics, list):
        raise TypeError("topics doit être une liste")

    result = mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
    return result.modified_count
