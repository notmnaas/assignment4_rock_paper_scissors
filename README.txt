Short description:
This is a Rock-Paper-Scissors game implemented as a Flask web API. The user sends a move (rock/paper/scissors), the computer randomly chooses a move, and the API returns the winner.

How to run locally:
1. Install dependencies:
   pip install -r requirements.txt
2. Run the app:
   python app.py
3. Play:
   POST to http://localhost:5000/play with JSON:
   { "move": "rock" }

How to run with Docker:
1. Build the image:
   docker build -t yourdockerusername/rps-game:latest .
2. Run the container:
   docker run --rm -p 5000:5000 yourdockerusername/rps-game:latest
3. Play:
   POST to http://localhost:5000/play

GitHub repo URL:
https://github.com/notmnaas/assignment4_rock_paper_scissors

Docker Hub image URL:
https://hub.docker.com/repository/docker/mnaas/assignment4_rock_paper_scissors

