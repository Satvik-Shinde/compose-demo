
from flask import Flask
import mysql.connector
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "Python Flask app running with Docker Compose!"


@app.route("/db")
def database():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "db"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "example"),
            database="appdb"
        )

        connection.close()
        return "Successfully connected to MySQL!"

    except mysql.connector.Error as error:
        return f"Database connection failed: {error}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

