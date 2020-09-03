from flask import Flask, request, render_template
import urlToText

app = Flask(__name__)


@app.route('/')
def home():
    return "Service is up!"


def get_text(url):
    return urlToText.get_text_data(url)


@app.route('/predict', methods=['POST'])
def predict():
    import tagger
    url = request.form['search']
    text = get_text(url)
    prediction = tagger.getKeyTerms(text)
    return prediction


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
