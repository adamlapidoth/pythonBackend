import tornado.ioloop


class UploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        files = self.request.files["imgFile"]
        for f in files:
            with open(f"img/{f.filename}", "wb") as fh:
                fh.write(f.body)
            self.write(f"http://localhost:8080/img/{f.filename}")


if __name__ == "__main__":
    app = tornado.web.Application(
        [
            ("/", UploadHandler),
            ("/img/(.*)", tornado.web.StaticFileHandler, {"path": "img"}),
        ]
    )

    port = 8080
    app.listen(port)
    print(f"Listening on port {port}")

    tornado.ioloop.IOLoop.instance().start()
