"""
HTMX Test
"""

import json
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index() ->str:
    """
    index
    """
    return render_template("index.html")

@app.route("/artists")
def artists() -> str:
    """
    Billboard 100 artists
    """
    data_path = Path(r"data/artists.json")
    with open(data_path, encoding="utf-8") as file:
        data = json.load(file)
    return render_template("artists.html", data=data["artists"])

@app.route("/main")
def main() -> str:
    """
    main
    """
    return render_template("main.html")
