import os

import openai
from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv

app = Flask(__name__)
openai.api_key = os.getenv(
    "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")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        iceCream = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(iceCream),
            temperature=0,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(iceCream):
    return """Suggest three names for an Weed to sell in our store depending on the flavour.
Flavour: {}
Name:""".format(
        iceCream.capitalize()
    )
