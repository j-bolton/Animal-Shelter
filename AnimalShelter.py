from pymongo import MongoClient
from pymongo import ReturnDocument
from bson.json_util import dumps
#from bson.json_util import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:52802/AAC' % (username, password))
        self.database = self.client['AAC']

# Create method to implement the C in CRUD.
    def create(self, data = None):
        if data is not None:
            insert = self.database.animals.insert_one(data)  # Data should be dictionary
            if (insert.acknowledged == True):                # Return true if insert was successful, else return false
                return True             
            else:
                return False
                
        else:
            raise Exception('Error - No data entered.')       # Throws exception if no data is passed

# Read method to implement the R in CRUD.
    def read(self, query = None):
        if query is not None:
            cursor = self.database.animals.find(query, {'_id' : False})        # Data should be dictionary
            if (cursor.count() != 0):                        # Assumes a non-empty cursor means the search was successful
                return cursor
            else:
                raise Exception('Data not found.')
        
        else:
            raise Exception('Error - No data entered.')

# Update method to implement the U in CRUD
    def update(self, query = None, update = None):
        if query is not None and update is not None:
            cursor = self.database.animals.find_one_and_update(query, {'$set' : update},
                                                               return_document = ReturnDocument.AFTER)    # Returns the document after being updated
            if (dumps(cursor) == 'null'):
                raise Exception('Query not found.')
            else:
                return dumps(cursor)    # Returns JSON
           
        else:
            raise Exception('Error - No data entered.')
        
# Delete method to implement the D in CRUD
    def delete(self, query = None):
        if query is not None:
            cursor = self.database.animals.find_one_and_delete(query)
            return dumps(cursor)        # Returns JSON
           
        else:
            raise Exception('Error - No data entered.')