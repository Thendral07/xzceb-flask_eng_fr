from machinetranslation import translator
from flask import Flask, render_template, request, machinetranslation
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "Translated text to English"

@app.route("/index.html")
def renderIndexPage():
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
