#!./bin/python3
from pymongo import MongoClient
from random import randrange
import sys
import time

loops = int(sys.argv[1])

WEIGHT_RANGE = 4
POPULATION_RANGE = 10
TEMPERATURE_RANGE = 2
HUMIDITY_RANGE = 1


def makeReading(n):
    r = randrange(-10, 10) / 10
    weight = abs(n['weight'] + int(r * WEIGHT_RANGE +
                 randrange(int(-1 * WEIGHT_RANGE / 2), int(WEIGHT_RANGE / 2))))

    reading = {
        "weight": weight,
        "temperature": abs(n['temperature'] + int(r * TEMPERATURE_RANGE)),
        "population": abs(n['population'] + int(r * POPULATION_RANGE)),
        "date": n['date'] + 1,
        "humidity": abs(n['humidity'] + int(r * HUMIDITY_RANGE)),
        "uploaded": False
    }
    return reading


client = MongoClient()  # Establish db connection.
db = client.sensorData  # Create or access a database called sensorData.
data = db.data          # Create or access a collection called data.

reading = {
        'weight': 60,
        'temperature': 24,
        'population': 800,
        'date': int(time.time()),
        'humidity': 7,
        'uploaded': False
        }

for i in range(loops):
    # Insert a document into the collection.
    reading = makeReading(reading)
    insertedId = data.insert_one(reading).inserted_id

if loops == 0:
    data.remove({})

'''
CRUD reference:
    data.find_one(search_query) - search_query is a dictionary, and find_one
                                  returns the earliest match record containing
                                  that key/value pair. It's values can be
                                  accessed like an array.

    data.find(search_query)     - As above, but returns an iterable.

    data.count()                - Returns the number of records in collection.

    data.remove(search_query)   - Deletes any records that match the query.

    data.update(search_query,
                modification,
                multi=True)     - This finds records matching the search_query,
                                  then performs the modification. For example,
                                  if modification = {'$inc': {'count': 1}},
                                  then this will increment any fields called
                                  'count' by 1. The multi field says whether
                                  this update should be performed on EVERY
                                  record that matches the search query or just
                                  the first match.
'''
