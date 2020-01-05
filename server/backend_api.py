from parse_data import ParseData
from flask import Flask, request, jsonify, abort, render_template

app = Flask(__name__)


@app.route('/ner/predict', methods=['POST', 'GET'])
def predict():
    try:
        txt = request.args.get('comment', None)
        data = ParseData(txt)
        result = data.process()
        return render_template('result.html', list = result)

    except Exception as e:
        raise(e)
        abort(500, "Fail to recognite named entity !!!")

if __name__ == "__main__":
    app.run(debug=True, port='8888')