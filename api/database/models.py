from mongoengine import *


class Checkpoint(EmbeddedDocument):
    """
    A MongoEngine EmbeddedDocument containing:
        distance: MongoEngine float field, required, (checkpoint distance in kilometers),
		location: MongoEngine string field, optional, (checkpoint location name),
		open_time: MongoEngine datetime field, required, (checkpoint opening time),
		close_time: MongoEngine datetime field, required, (checkpoint closing time).
    """
    distance = FloatField(required = True) # checkpoint distance in km
    location = StringField # checkpoint location name
    open_time = DateTimeField(required = True) # checkpoint opening time
    close_time = DateTimeField(required = True) # checkpoint closing time


    



class Brevet(Document):
    """
    A MongoEngine document containing:
		length: MongoEngine float field, required
		start_time: MongoEngine datetime field, required
		checkpoints: MongoEngine list field of Checkpoints, required
    """
    
    length = FloatField(required = True) # brevet distance in km
    start_time = DateTimeField(required = True) # brevet start time
    checkpoints = ListField(EmbeddedDocumentField(Checkpoint), required = True) # brevet checkpoints
