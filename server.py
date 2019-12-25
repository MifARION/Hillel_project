from tornado import web, ioloop

from app import Index, Delete


def make_app():
    return web.Application([
        (r'/', Index),
        (r'/delete-music/', Delete)
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    ioloop.IOLoop.current().start()
