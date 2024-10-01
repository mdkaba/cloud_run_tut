import os, json, time

from flask import Flask, request

app = Flask(__name__)

from google.cloud import bigquery



@app.route("/user", methods=['GET'])
def user_resource():
    """Example Hello World route."""

    return json.dumps({'id': 123, "name: "Mamadou"})
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
