from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Temporary in-memory users list
USERS = [
    {"id": 1, "username": "admin", "password": "admin123"}
]

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    # Validation
    if not username or not password:
        return jsonify({"message": "All fields are required"}), 400

    # Check if user already exists
    for user in USERS:
        if user["username"] == username:
            return jsonify({"message": "Username already exists"}), 409

    # Create new user
    new_user = {
        "id": len(USERS) + 1,
        "username": username,
        "password": password
    }
    USERS.append(new_user)

    return jsonify({"message": "Registration successful"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    for user in USERS:
        if user["username"] == username and user["password"] == password:
            return jsonify({
                "message": "Login successful",
                "user": {
                    "id": user["id"],
                    "username": user["username"]
                }
            }), 200

    return jsonify({"message": "Invalid username or password"}), 401


if __name__ == "__main__":
    app.run(debug=True)
