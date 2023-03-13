from flask import Flask, request

app = Flask(__name__)

def create_json_response_for_permissions(hasAdmin: bool, hasAuthor: bool):
    return {"hasAdmin": hasAdmin, "hasAuthor": hasAuthor}

@app.route('/', methods=['GET'])
def home():
    username = request.args.get('username', default = "", type = str)

    if username:
        return create_json_response_for_permissions(
            "admin" in username.lower(),
            "staff-author" in username.lower()
        )

    return create_json_response_for_permissions(False, False)

@app.route('/third-party-auth', methods=['GET'])
def vercel_compatible_home():
    username = request.args.get('username', default = "", type = str)

    if username:
        return create_json_response_for_permissions(
            "admin" in username.lower(),
            "staff-author" in username.lower()
        )

    return create_json_response_for_permissions(False, False)

@app.route('/about')
def about():
    return 'About'