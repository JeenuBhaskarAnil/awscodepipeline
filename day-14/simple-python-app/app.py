from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return ' bhaskaranil u sucessfully created  a cicd pipeline!'

if __name__ == '__main__':
    app.run()
    

