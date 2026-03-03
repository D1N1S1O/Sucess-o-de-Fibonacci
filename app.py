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
    #coelhos_visiveis = min(session["current"], 55)
    #limitado = session["current"] > 55
    coelhos_visiveis = session["current"]

    return render_template(
        "index.html",
        mes=session["mes"],
        coelhos=session["current"],
        coelhos_visiveis=coelhos_visiveis,
    )

@app.route("/avancar", methods=["POST"])
def avancar():
    prev = session.get("prev", 0)
    current = session.get("current", 1)
    next_value = prev + current
    session["prev"] = current
    session["current"] = next_value
    session["mes"] = session.get("mes", 1) + 1
    #coelhos_visiveis = min(session["current"], 55)
    #limitado = session["current"] > 55
    coelhos_visiveis = session["current"]

    return render_template(
        "index.html",
        mes=session["mes"],
        coelhos=session["current"],
        coelhos_visiveis=coelhos_visiveis,
    )


@app.route("/recuar", methods=["POST"])
def recuar():
    if session["mes"] > 1:
        prev = session.get("prev", 0)
        current = session.get("current", 1)
        session["prev"] = current - prev
        session["current"] = prev
        session["mes"] -= 1
        #coelhos_visiveis = min(session["current"], 55)
        #limitado = session["current"] > 55
        coelhos_visiveis = session["current"]
        limitado = False;

    return render_template(
        "index.html",
        mes=session["mes"],
        coelhos=session["current"],
        coelhos_visiveis=coelhos_visiveis,
    )

@app.route("/voltar", methods=["POST"])
def voltar():
    session["mes"] = 1
    session["prev"] = 0
    session["current"] = 1
    #coelhos_visiveis = min(session["current"], 55) para limitar os coelhos visiveis
    #limitado = session["current"] > 55
    coelhos_visiveis = session["current"]

    return render_template(
        "index.html",
        mes=session["mes"],
        coelhos=session["current"],
        coelhos_visiveis=coelhos_visiveis,
    )



if __name__ == "__main__":
    app.run()
