from flask import Flask, jsonify, request

app = Flask(__name__)
dataquote = {}

@app.route('/')
@app.route('/api_quote', methods=['GET'])
def api_quote():
    global dataquote
    return jsonify(dataquote)

@app.route('/add_quote', methods=['POST'])
def add_quote():
    global dataquote
    try:
        if dataquote == {} : id = 0
        else : 
            for i in dataquote: id = i + 1
        quote_text = request.form['quote_text']
        your_name = request.form['quote_text']
        dataquote[id] = {'quote':quote_text,'name':your_name,'like':0}
        return jsonify({'msg':'add quote success', 'kode':'200'})
    except:
        return jsonify({'msg':'add quote failed', 'kode':'300'})

@app.route('/like/<int:id>', methods=['POST'])
def add_like(id):
    global dataquote
    try:
        dataquote[id]['like'] = dataquote[id]['like'] + 1
        return jsonify({'msg':'add like success', 'kode':'200'})
    except:
        return jsonify({'msg':'add like failed', 'kode':'300'})

@app.route('/dislike/<int:id>', methods=['POST'])
def add_dislike(id):
    global dataquote
    try:
        dataquote[id]['like'] = dataquote[id]['like'] - 1
        return jsonify({'msg':'add dislike success', 'kode':'200'})
    except:
        return jsonify({'msg':'add dislike failed', 'kode':'300'})

@app.route('/delete_quote/<int:id>', methods=['GET'])
def delete(id):
    try:
        global dataquote
        deleted = dataquote.pop(id)
        return jsonify({'msg':'delete success', 'kode':'200'})
    except:
        return jsonify({'msg':'delete failed', 'kode':'300'})

if __name__ == '__main__':
    app.run(debug=True, port=2000)
