from flask import Flask, render_template, session
from flask_session import Session

app = Flask(__name__)
app.config["SECRET_KEY"] = "segredo"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET"])
def index():
    if "mes" not in session:
        session["mes"] = 1
        session["prev"] = 0
        session["current"] = 1
    return render_template("index.html", mes=session["mes"], coelhos=session["current"])

@app.route("/avancar", methods=["POST"])
def avancar():
    prev = session.get("prev", 0)
    current = session.get("current", 1)
    next_value = prev + current
    session["prev"] = current
    session["current"] = next_value
    session["mes"] = session.get("mes", 1) + 1
    return render_template("index.html", mes=session["mes"], coelhos=session["current"])


@app.route("/recuar", methods=["POST"])
def recuar():
    if session["mes"] > 1:
        prev = session.get("prev", 0)
        current = session.get("current", 1)
        session["prev"] = current - prev
        session["current"] = prev
        session["mes"] -= 1
    return render_template("index.html", mes=session["mes"], coelhos=session["current"])

@app.route("/voltar", methods=["POST"])
def voltar():
    session["mes"] = 1
    session["prev"] = 0
    session["current"] = 1
    return render_template("index.html", mes=session["mes"], coelhos=session["current"])



if __name__ == "__main__":
    app.run()