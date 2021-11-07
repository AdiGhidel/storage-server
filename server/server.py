import logging
from flask import Flask, json, request
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
    success = state.add_file(name, data)
    if success:
        return json.dumps("ok"), 200
    else:
        return json.dumps("not added"), 500


@api.route('/files/<name>', methods=['DELETE'])
def delete(name):
    success = state.remove_file(name)
    if success:
        return json.dumps("ok"), 200
    else:
        return json.dumps("not added"), 500


@api.route('/files', methods=['GET'])
def list():
    return json.dumps(state.list_files()), 200

if __name__ == '__main__':
    api.run()
