import pandas as pd
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
df = pd.read_json("book.json")
df1 = pd.read_csv("book_similarity_df.csv")
df1
class booklist(Resource):
    def get(self):
        return df.to_json()
class recommendation(Resource):
    def get(self):
        return df1.to_json()
api.add_resource(booklist, '/books')
api.add_resource(recommendation, '/similarity')

if __name__ == '__main__':
    app.run(debug=True)
