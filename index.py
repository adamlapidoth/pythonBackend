import tornado.ioloop


class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World! this is a python command")


class ListRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class QueryParamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if num.isdigit():
            result = "odd" if int(num) % 2 else "even"
            self.write(f"The integer {num} is {result}")
        else:
            self.write(f"{num} is not a valid integer")


class ResourceParamRequestHandler(tornado.web.RequestHandler):
    def get(self, student_name, course_id):
        self.write(
            f"Welcome {student_name} "
            f"the course you are viewing is {course_id}"
        )


if __name__ == "__main__":
    app = tornado.web.Application(
        [
            ("/", BasicRequestHandler),
            ("/animal", ListRequestHandler),
            ("/isEven", QueryParamRequestHandler),
            ("/students/([a-z]+)/([0-9]+)", ResourceParamRequestHandler),
        ]
    )

    port = 8882
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
