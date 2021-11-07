import logging
from flask import Flask, json, request, Response
api = Flask(__name__)


class State:
    def __init__(self) -> None:
        self.files = dict()

    def file_exists(self, f):
        return f in self.files

    def add_file(self, f, data):
        if not self.file_exists(f):
            self.files[f] = data
            logging.info(f"file {f} added")
        else:
            logging.info(f"file {f} already exists")
            return False
        return True

    def remove_file(self, f):
        if self.file_exists(f):
            del self.files[f]
            logging.info(f"file {f} removed")
        else:
            logging.info(f"file {f} was missing")
            return False
        return True

    def list_files(self):
        return [f for f in self.files]


state = State()


@api.route('/files/<name>', methods=['POST'])
def upload(name):
    data = request.values
    print(data)
    success = state.add_file(name, data)
    response = Response()
    response.headers.add('Access-Control-Allow-Origin', '*')
    if success:
        response.data = json.dumps("ok")
        ret_code = 200
    else:
       response.data = json.dumps("not added")
       ret_code = 500
    return response, ret_code

@api.route('/files/<name>', methods=['OPTIONS'])
def options(name):
    response = Response()
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'DELETE')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Max-Age', 86400)
    return response, 200

@api.route('/files/<name>', methods=['DELETE'])
def delete(name):
    success = state.remove_file(name)
    response = Response()
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000/')
    if success:
        response.data = json.dumps("ok")
        ret_code = 200
    else:
       response.data = json.dumps("not deleted")
       ret_code = 500
    return response, ret_code

@api.route('/files', methods=['GET'])
def list():
    response = Response()
    response.data = json.dumps(state.list_files())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200

if __name__ == '__main__':
    api.run()
