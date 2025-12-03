#!/usr/bin/env python3
""" Module qui liste tous les documents
              d'une collection MongoDB. """


from pymongo import MongoClient


def list_all(mongo_collection):
    """Liste tous les documents d'une collection."""

    return list(mongo_collection.find())
