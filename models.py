from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True)
    artist_name = Column(String)
    track_name = Column(String)
    track_time = Column(Integer)

    def __repr__(self):
        return "{}".format(self.name)



