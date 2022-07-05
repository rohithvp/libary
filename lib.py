from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.HTML")


@app.route("/Book")
def Book():
    return render_template("desc.HTML")


if __name__ == "__main__":
    app.run()
