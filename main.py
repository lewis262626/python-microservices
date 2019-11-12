from flask import Flask, escape, request, jsonify, redirect, url_for, abort

app = Flask(__name__)

persons = [
    {
        "id": 1,
        "name": "Tim",
        "age": 80,
        "Hobbies": "Gardening",
    },
    {
        "id": 2,
        "name": "Chris",
        "age": 30,
        "hobbies": "martial-arts",
    }
]

@app.route('/')
def index():
    return redirect(url_for('persons_response'))

@app.route('/persons')
def persons_response():
    response = jsonify(persons)
    response.headers["Content-Type"] = "text/json"
    return response

@app.route('/person/<id>')
def person_response(id):
    if int(id) > 1:
        abort(401)
    else:
        new_list = sorted(persons, key = lambda k : k['name']) # assuming not sorted
        response = jsonify(new_list[int(id)])
        response.headers['Content-Type'] = 'text/json'
        return response