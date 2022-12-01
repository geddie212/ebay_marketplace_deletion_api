from flask import Flask, request, jsonify, Response
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
        return Response(resp, status=200, mimetype='application/json')
    except KeyError:
        err = {'status_code': 400, 'message': 'no challenge response in params'}
        return Response(err, status=400, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
