import os

from flask import Flask, request, jsonify
from flask_restx import Resource, Api, Namespace

from werkzeug.exceptions import BadRequest

from utils import get_result

perform_query_ns = Namespace("perform_query")

app = Flask(__name__)

api = Api(app)
api.add_namespace(perform_query_ns)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@perform_query_ns.route('/')
class PerformQuery(Resource):
    def post(self):
        rq = request.json
        print(rq)

        filename = rq["file_name"]

        if not os.path.exists(os.path.join(DATA_DIR, filename)):
            raise BadRequest

        with open(os.path.join(DATA_DIR, filename)) as f:
            file = [item.strip() for item in f.readlines()]

        result = get_result(rq, file)
        return jsonify(result)


if __name__ == "__main__":
    app.run()
