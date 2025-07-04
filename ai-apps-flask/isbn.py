from flask import Flask, escape
import requests 

app = Flask(__name__)

@app.route("/book/<isbn>")
def get_book(isbn):
  res = requests.get("https://openlibrary.org/isbn/{escape(isbn)}.JSON")
  
  if res.status_code == 200:
    return {"message": res.JSON()}
  elif res.status_code == 404:
    return {"message": "Something went wrong!"}, 404
