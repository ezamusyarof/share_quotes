from collections import OrderedDict
import requests, json
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    global dataquote
    get_data = requests.get("http://127.0.0.1:2000/api_quote")
    data_str = ""
    for i in get_data:
        i = i.decode('utf-8')
        data_str = data_str + str(i)
    data = json.loads(data_str)
    new_data = OrderedDict(reversed(list(data.items())))
    return render_template('index.html',data=new_data)

if __name__ == '__main__':
    app.run(debug=True)
