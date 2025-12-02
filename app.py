# app.py
import random
from flask import Flask, jsonify, request

app = Flask(__name__)

VALID_MOVES = ["rock", "paper", "scissors"]

def determine_winner(user, cpu):
    if user == cpu:
        return "tie"
    if (
        (user == "rock" and cpu == "scissors") or
        (user == "paper" and cpu == "rock") or
        (user == "scissors" and cpu == "paper")
    ):
        return "user"
    return "cpu"

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Rock Paper Scissors API",
        "how_to_play": "Send POST to /play with JSON: { 'move': 'rock|paper|scissors' }"
    })

@app.route("/play", methods=["POST"])
def play():
    data = request.get_json(silent=True)

    if not data or "move" not in data:
        return jsonify({"error": "You must send JSON: { 'move': 'rock|paper|scissors' }"}), 400

    user_move = data["move"].lower()
    if user_move not in VALID_MOVES:
        return jsonify({"error": "Move must be rock, paper, or scissors"}), 400

    cpu_move = random.choice(VALID_MOVES)
    result = determine_winner(user_move, cpu_move)

    return jsonify({
        "your_move": user_move,
        "cpu_move": cpu_move,
        "result": result
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
