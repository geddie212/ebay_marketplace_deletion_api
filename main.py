from flask import Flask, request, jsonify, Response
import json
import hashlib
import os

app = Flask(__name__)

verification_token = 'r8943d2h7f65g7426-2j437589f27-0895f728-674g3298f675'
endpoint = 'https://ebay-deletion.herokuapp.com/delete-notification'

# verification_token = os.environ.get('verification_token')
# endpoint = os.environ.get('endpoint')

@app.route('/')
def index():
    args = request.args
    args_dict = args.to_dict()
    try:
        resp_hash = hashlib.sha256(
            args_dict['challenge_code'].encode() + verification_token.encode() + endpoint.encode())
        resp = {'challengeResponse': resp_hash.hexdigest()}
        return jsonify(resp), 200, {'content-type': 'application/json'}
    except KeyError:
        err = {'status_code': 400, 'message': 'no challenge response in params'}
        return jsonify(err), 400, {'content-type': 'application/json'}

@app.route('/delete-notification')
def delete():
    args = request.args
    args_dict = args.to_dict()
    try:
        resp_hash = hashlib.sha256(
            args_dict['challenge_code'].encode() + verification_token.encode() + endpoint.encode())
        resp = {'challengeResponse': resp_hash.hexdigest()}
        return jsonify(resp), 200, {'content-type': 'application/json'}
    except KeyError:
        err = {'status_code': 400, 'message': 'no challenge response in params'}
        return jsonify(err), 400, {'content-type': 'application/json'}


if __name__ == '__main__':
    app.run(debug=True)
