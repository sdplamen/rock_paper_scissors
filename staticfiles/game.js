const gameForm = document.getElementById('game-form');
const playButton = document.getElementById('play-button');
const playerChoiceDisplay = document.getElementById('player-choice-display');
const computerChoiceDisplay = document.getElementById('computer-choice-display');
const resultMessageBox = document.getElementById('result-message-box');
const gameResultsDiv = document.getElementById('game-results');
const winsScore = document.getElementById('wins-score');
const lossesScore = document.getElementById('losses-score');
const drawsScore = document.getElementById('draws-score');

// Function to fetch CSRF token from Django's cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// Function to update the UI with game results
function updateUI(data) {
    playerChoiceDisplay.textContent = data.player_move;
    computerChoiceDisplay.textContent = data.computer_move;
    resultMessageBox.textContent = data.result_message;

    // Apply styling based on the result message
    resultMessageBox.classList.remove('win', 'lost', 'draw');
    if (data.result_message === 'You win!') {
        resultMessageBox.classList.add('win');
    } else if (data.result_message === 'You lost!') {
        resultMessageBox.classList.add('lost');
    } else {
        resultMessageBox.classList.add('draw');
    }

    winsScore.textContent = data.win;
    lossesScore.textContent = data.lost;
    drawsScore.textContent = data.draw;
    gameResultsDiv.classList.remove('hidden'); // Show results div
}

// Handle form submission
gameForm.addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent default form submission

    const selectedMove = document.querySelector('input[name="player_move"]:checked');
    if (!selectedMove) {
        alert('Please select your move!'); // Using alert for simplicity, but a modal is better
        return;
    }

    const playerMoveValue = selectedMove.value;

    try {
        const response = await fetch('/api/play/', { // Your API endpoint
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken, // Include CSRF token
            },
            body: JSON.stringify({ player_move: playerMoveValue }),
        });

        if (!response.ok) {
            const errorData = await response.json();
            console.error('API Error:', errorData);
            alert('Error playing round: ' + JSON.stringify(errorData));
            return;
        }

        const data = await response.json();
        updateUI(data);

    } catch (error) {
        console.error('Fetch error:', error);
        alert('An error occurred while communicating with the server.');
    }
});

// Optional: Fetch initial scores when the page loads
document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch('/api/play/'); // GET request to get initial state
        if (!response.ok) {
            console.error('Failed to fetch initial scores.');
            return;
        }
        const data = await response.json();
        winsScore.textContent = data.win;
        lossesScore.textContent = data.lost;
        drawsScore.textContent = data.draw;
    } catch (error) {
        console.error('Error fetching initial scores:', error);
    }
});

// Add event listeners to labels to simulate radio button selection visual feedback
document.querySelectorAll('label[for]').forEach(label => {
    label.addEventListener('click', function() {
        // Remove selected class from all labels
        document.querySelectorAll('label[for]').forEach(l => l.classList.remove('bg-indigo-600', 'text-white'));
        // Add selected class to the clicked label
        this.classList.add('bg-indigo-600', 'text-white');
    });
});