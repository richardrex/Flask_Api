import requests
import pandas as pd
BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "/books")

print(response.json())



