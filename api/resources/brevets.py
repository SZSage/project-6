"""
Resource: Brevets
"""
from flask import Response, request
from flask_restful import Resource
import traceback # For debugging
from database.models import Brevet

class BrevetsResource(Resource):
    
    def get(self):
        # Get all brevets
        json_object = Brevet.objects().to_json() # Serialize MongoEngine query to JSON
        return Response(json_object, mimetype = "application/json", status = 200) # Return JSON and status code 200 (OK)
    
    def post(self):
        # Create new brevet
        try:
            input_json = request.json # Get JSON payload
            result = Brevet(**input_json).save() # Create new brevet and save to database 
            return {"_id": str(result.id)}, 200 # Return id of new brevet and status code 200 (OK)
        except Exception as e: 
            traceback.print_exc() # For debugging
            return {"error": str(e)}, 400 # Return error message and status code 400 (Bad Request)
        
# MongoEngine queries:
# Brevet.objects() : similar to find_all. Returns a MongoEngine query
# Brevet(...).save() : creates new brevet
# Brevet.objects.get(id=...) : similar to find_one

# Two options when returning responses:
#
# return Response(json_object, mimetype="application/json", status=200)
# return python_dict, 200
#
# Why would you need both?
# Flask-RESTful's default behavior:
# Return python dictionary and status code,
# it will serialize the dictionary as a JSON.
#
# MongoEngine's objects() has a .to_json() but not a .to_dict(),
# So when you're returning a brevet / brevets, you need to convert
# it from a MongoEngine query object to a JSON and send back the JSON
# directly instead of letting Flask-RESTful attempt to convert it to a
# JSON for you.
