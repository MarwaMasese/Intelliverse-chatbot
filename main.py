from flask import Flask, request
import openai


app = Flask(__name__)

@app.route('/')
def incoming_call():
   return "Just a demo"
if __name__ == '__main__':
    app.run(debug=True)