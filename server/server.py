from flask import Flask, json
api = Flask(__name__)

class State:
    def __init__(self) -> None:
        files = []
    def file_exists(self, f):
        return f in self.files

state = State()

@api.route('/files/<name>', methods=['POST'])
def upload(name):
    print(name)
    return json.dumps("ok"), 200

@api.route('/files/<name>', methods=['DELETE'])
def delete(name):
    print(name)
    return json.dumps("ok"), 200

@api.route('/files', methods=['GET'])
def list(name):
    print(name)
    return json.dumps("ok"), 200


if __name__ == '__main__':

    api.run()
