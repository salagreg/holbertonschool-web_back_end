#!/usr/bin/env python3
""" Insérer un nouveau document dans une collection MongoDB """


from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """ Insère un nouveau document dans une collection MongoDB """

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
