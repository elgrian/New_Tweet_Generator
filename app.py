
import sys, random
import sample
import dictionary_words

from flask import Flask, render_template
import markov_chain

app = Flask(__name__)

@app.route("/")

def main():

    sentence_string = markov_chain.main()

    return render_template("index.html", sentence = sentence_string)