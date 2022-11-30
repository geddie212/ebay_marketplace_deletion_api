from flask import Flask, request, jsonify
import hashlib
import os

app = Flask(__name__)

# verification_token = 'r8943d2h7f65g7426-2j437589f27-0895f728-674g3298f675'
# endpoint = 'https://ebay-deletion.herokuapp.com'

verification_token = os.environ.get('verification_token')
endpoint = os.environ.get('endpoint')

@app.route('/')
def index():
    args = request.args
    args_dict = args.to_dict()
    try:
        resp_hash = hashlib.sha256(args_dict['challenge_code'].encode() + verification_token.encode() + endpoint.encode())
        resp = {'challengeResponse': resp_hash.hexdigest()}
        return jsonify(resp), 200
    except KeyError:
        return '<p>Wrong Parameters</p>', 404


if __name__ == '__main__':
    app.run(debug=True)