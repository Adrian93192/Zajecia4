from flask import Flask
from sqlalchemy import create_engine

app = Flask(__name__)
engine = create_engine("sqlite:///:memory:")

@app.route("/")
def hello():
    return "Test aplikacji Flask + SQLAlchemy!"

if __name__ == "__main__":
    app.run(debug=True)
