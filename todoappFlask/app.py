from flask import Flask, request, Response, jsonify, make_response
import sqlite
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def add_item():
    req_data = request.get_json()
    item = req_data['item']
    actiontime = req_data['actiontime']
    # print(req_data['repeatcount'])
    # repeatcount = req_data['repeatcount']
    print(f'POST:{request}')
    res_data = sqlite.add_to_list(item, actiontime, 2)

    if res_data is None:
        response = Response("{'error': 'Item not added - " + item + "'}", status=400 , mimetype='application/json')
        return response


    response = jsonify(res_data)
    return response


@app.route('/', methods=["GET"])
def get_all_items_fromdb():
 
    res_data = sqlite.get_all_items()
    return make_response(jsonify(res_data))


@app.route('/', methods=['PUT'])
def updatedb():
    
    req_data = request.get_json()
    print(req_data)
    dict_ = sqlite.update(req_data['item'], req_data['status'], req_data['actiontime'], req_data['repeatcount'])
    return make_response(jsonify(dict_))


@app.route('/', methods=['DELETE'])
def delete():
    req_data = request.get_json()
    return sqlite.delete(req_data['item'])

app.run()