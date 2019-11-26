from . import db
import uuid as uid

class Geneset(db.Model):
    db.Column(UUID(as_uuid=True), primary_key=True)
    geneset = db.Column(db.String())

    def __repr__(self):
        return '<Geneset %r>' % self.geneset
    
    def __init__(self, meta, uuid):
        self.uuid = uuid
        self.meta = meta