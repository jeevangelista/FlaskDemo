from . import db
from uuid import uuid4

class Geneset(db.Model):
    uuid = db.Column(db.String(35), primary_key=True)
    geneset = db.Column(db.String(), unique=True)

    def __repr__(self):
        return '<Geneset %r>' % self.geneset
    
    def __init__(self, geneset):
        self.uuid = str(uuid4())
        geneset = "\n".join(sorted(geneset.split()))
        self.geneset = geneset