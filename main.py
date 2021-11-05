from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)



class BookApi(Resource):
    def get(self, table_name):
        return {"data": table_name}
    def post(self):
        return {"data": "Posted"}

api.add_resource(BookApi, "/helloworld/<string:table_name>")

if __name__ == "__main__":
    app.run(debug=True)
