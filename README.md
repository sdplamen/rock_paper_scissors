# Rock Paper Scissors Game

This project is a web-based "Rock, Paper, Scissors" game built with Python and Django. It also includes a console-based version of the game.

## Project Goals

The main goal of this project is to create a simple, interactive "Rock, Paper, Scissors" game that can be played in a web browser or in the console. The project demonstrates the use of Django for web development and the Django REST Framework for creating APIs.

## Features

*   Play "Rock, Paper, Scissors" against the computer.
*   Web interface for playing the game.
*   Console version of the game.
*   Keeps track of your score (wins, losses, and draws).
*   API endpoint for playing the game programmatically.

## Technologies Used

*   **Backend:** Python, Django, Django REST Framework
*   **Frontend:** HTML, CSS, JavaScript
*   **Database:** PostgreSQL (based on `psycopg2-binary` in `requirements.txt`)

## API Endpoint

The project also provides an API endpoint for playing the game.

*   **URL:** `/api/game/`
*   **Method:** `POST`
*   **Body:**
    ```json
    {
        "player_move": "rock"
    }
    ```
*   **Response:**
    ```json
    {
        "player_move": "Rock",
        "computer_move": "Scissors",
        "result_message": "You win!",
        "win": 1,
        "lost": 0,
        "draw": 0
    }
    ```
