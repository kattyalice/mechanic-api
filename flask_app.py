import os
from app import create_app
from flask import redirect

configure_name = os.environ.get("FLASK_CONFIG",  "DevelopmentConfig")
app = create_app(configure_name)

@app.route("/", methods=["GET"])
def index():
    return redirect("/api/docs")

if __name__ == "__main__":
    app.run(debug=True)