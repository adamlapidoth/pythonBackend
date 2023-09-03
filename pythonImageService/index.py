import tornado.web
import tornado.ioloop


class UploadHandler:
    pass


if __name__ == '__main__':
    app = tornado.web.Application([
        ("/img/(.*)", tornado.web.StaticFileHandler, {"path": "img"})
    ])

    port = 8080
    app.listen(port)
    print(f"Listening on port {port}")

    tornado.ioloop.IOLoop.instance().start()