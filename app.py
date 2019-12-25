from tornado import web
from sqlalchemy.orm import sessionmaker


from db import engine
from models import Artist


class Index(web.RequestHandler):

    def get(self):
        session = sessionmaker(bind=engine)()
        context = {
            'tracks': session.query(Artist).all(),
            'error': None,
            'artist': session.query(Artist).artist_name(),
            'time': session.query(Artist).track_time(),

        }
        self.render('templates/index.html', **context)

    def post(self):
        session = sessionmaker(bind=engine)()
        session.add(Artist(
            track_name=self.get_body_argument('track-text'),
            artist_name=self.get_body_argument('artist-text'),
            track_time=float(self.get_body_argument('time_text')),
        ))
        session.commit()

        context = {
            'tracks': session.query(Artist).all(),
            'error': None,

        }
        self.render('templates/index.html', **context)


class Delete(web.RequestHandler):

    def post(self):
        session = sessionmaker(bind=engine)()
        music = session.query(Artist).filter_by(
            id=int(self.get_body_argument('id'))
        ).first()
        session.delete(music)
        session.commit()
        self.redirect('/')


