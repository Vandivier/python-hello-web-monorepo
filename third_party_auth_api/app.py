from flask import Flask, request

app = Flask(__name__)

def create_json_response_for_permissions(hasAdmin: bool):
    return {"hasAdmin": hasAdmin}

@app.route('/', methods=['GET'])
def home():
    username = request.args.get('username', default = "", type = str)

    if username:
        return create_json_response_for_permissions("admin" in username.lower())

    return create_json_response_for_permissions(False)

@app.route('/about')
def about():
    return 'About'