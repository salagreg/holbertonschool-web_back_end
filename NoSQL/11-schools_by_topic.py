#!/usr/bin/env python3
""" Module qui renvoie la liste des écoles
            ayant un sujet particulier. """


from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """ Retourne la liste des écoles ayant un sujet particulier."""

    return mongo_collection.find({'topics': topic})
