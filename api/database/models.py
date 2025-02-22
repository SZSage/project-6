from mongoengine import *

class Checkpoint(EmbeddedDocument):
    """
    A MongoEngine EmbeddedDocument containing:
        distance: MongoEngine float field, required, (checkpoint distance in kilometers),
		location: MongoEngine string field, optional, (checkpoint location name),
		open_time: MongoEngine datetime field, required, (checkpoint opening time),
		close_time: MongoEngine datetime field, required, (checkpoint closing time).
    """
    miles = FloatField() # checkpoint distance in miles
    km = FloatField(required = True) # checkpoint distance in km
    location = StringField() # checkpoint location name
    open = StringField(required = True) # Used StringField instead of DateTimeField because of the format of the time
    close = StringField(required = True) #  Used StringField instead of DateTimeField because of the format of the time


class Brevet(Document):
    """
    A MongoEngine document containing:
		length: MongoEngine float field, required
		start_time: MongoEngine datetime field, required
		checkpoints: MongoEngine list field of Checkpoints, required
    """
    
    brevet_dist = FloatField(required = True) # brevet distance in km
    begin_date = StringField(required = True) # brevet start time
    checkpoints = EmbeddedDocumentListField(Checkpoint, required = True) # brevet checkpoints
  