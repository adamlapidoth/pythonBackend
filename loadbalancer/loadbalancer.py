import argparse
import os

import tornado.web

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", help="Port number for app to run on")


class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(f"Served from {os.getpid()}")


if __name__ == "__main__":
    app = tornado.web.Application([("/basic", BasicRequestHandler)])

    port = int(parser.parse_args().port)
    app.listen(port)
    print(f"listening on port {port}")

    tornado.ioloop.IOLoop.current().start()
