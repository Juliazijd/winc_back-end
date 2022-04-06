from flask import Flask, render_template, redirect, url_for

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)


@app.route("/home")
def home():
    return redirect(url_for("index"))


@app.route("/")
@app.route("/<path>")
def index(path=None):
    if path is not None:
        return render_template(f"{path}.html", title=path.capitalize())
    else:
        return render_template("index.html", title="Index")
