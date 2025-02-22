"""
Resource: Brevet
"""
from flask import Response, request
from flask_restful import Resource

from database.models import Brevet

class BrevetResource(Resource):
    
    def get(self, id):
        brevet = Brevet.objects.get(id = id).to_json() # Get brevet by id
        return Response(brevet, mimetype = "application/json", status = 200) # Return brevet as JSON and status code 200 (OK)
    

    def put(self, id):
        input_json = request.json # Get JSON payload 
        Brevet.objects.get(id = id).update(**input_json)
        return "", 200 # Return empty body and status code 200 (OK)
    
    def delete(self, id):
        Brevet.objects.get(id = id).delete() # Delete brevet by id
        return "", 200 # Return empty body and status code 200 (OK)



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
