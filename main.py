from pymongo import MongoClient

mongo_uri = "mongodb+srv://layzjesussantana28:12160612l@cluster0.fil2klk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo_client = MongoClient(mongo_uri)

database = mongo_client['database_test']
test_collection = database['test_collection']

person = {"name": "Lucca de Enzo", "age": 12}
test_collection = database["test_collection"]