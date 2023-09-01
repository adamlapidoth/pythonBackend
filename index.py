import json

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


class FruitRequestHandler(tornado.web.RequestHandler):
    def get(self):
        with open("fruits.txt") as f:
            fruits = f.read().splitlines()
            self.write(json.dumps(fruits))

    def post(self):
        fruit = self.get_argument("fruit")
        with open("fruits.txt", "a") as f:
            f.write(f"{fruit}\n")
        self.write(json.dumps({"message": "fruit added successfully"}))


if __name__ == "__main__":
    app = tornado.web.Application(
        [
            ("/", BasicRequestHandler),
            ("/animal", ListRequestHandler),
            ("/isEven", QueryParamRequestHandler),
            ("/students/([a-z]+)/([0-9]+)", ResourceParamRequestHandler),
            ("/fruits", FruitRequestHandler),
        ]
    )

    port = 8882
    app.listen(port)
    print(f"Application is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
