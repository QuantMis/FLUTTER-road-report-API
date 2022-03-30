from apps import db

class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class Aduan(Base):

    __tablename__ = 'aduan'  
    image_path = db.Column(db.String(256), nullable=False)
    latitude = db.Column(db.String(256), nullable=False)
    longitude = db.Column(db.String(256), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    status = db.Column(db.String(256), nullable=False)

    def __init__(self, image_path, latitude, longitude, address, status):
        self.image_path = image_path
        self.latitude = latitude
        self.longitude = longitude
        self.address = address
        self.status = status