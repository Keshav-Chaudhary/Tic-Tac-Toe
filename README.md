
![image](https://github.com/user-attachments/assets/3fb3fa97-ed7d-4bfd-9e45-5756d876d8e3)

# Tic-Tac-Toe

Tic-Tac-Toe is a web-based game where two players can play the classic Tic-Tac-Toe game on the same device. The application features an intuitive and responsive UI for both phones and PCs.

## Features

- **Play Tic-Tac-Toe**: A two-player game interface where players take turns.
- **Current Player Display**: Shows whose turn it is.
- **Winner Announcement**: Highlights the winner or declares a draw.
- **Game Restart**: Quickly reset the game and start over.
- **Developer Information Page**: Learn more about the developers behind the project.

## Highlights

- **Responsive Design**: Fully functional on phones, tablets, and desktops using Tailwind CSS.
- **Interactive Gameplay**: Dynamic updates for each move and player turn.
- **User-Friendly UI**: Clean and simple design for easy navigation.

## Technologies Used

- **Frontend**: HTML, CSS (via Tailwind CSS), and JavaScript.
- **Backend**: Python and Flask.
- **Deployment**: Hosted on Vercel for fast and reliable access.

## Access the Application

Play the game here: https://temp-three-jade.vercel.app/

## Usage

1. Visit the game link above.
2. Two players can take turns clicking on the cells to play.
3. The game announces the winner or a draw at the end.
4. Click "Restart Game" to reset the board.

## Current Limitation

- Both players must be on the same device to play. Future updates aim to enable online multiplayer functionality.

## Future Enhancements

- **Online Multiplayer**: Allow players to compete over the internet.
- **AI Opponent**: Single-player mode with a computer opponent.
- **Game History**: Save and display past game results.
- **Themes**: Add customizable themes for the game interface.
- **Sound Effects**: Add sound for moves and win/loss notifications.

---

### Project Structure

The project is organized as follows:

```plaintext
Tic-Tac-Toe/
├── __pycache__       # Compiled Python files
├── static/           # Static assets (CSS, JavaScript, images)
├── templates/        # HTML templates for Flask
├── about.html        # About the developers page
├── index.html        # Main game page
├── README.md         # Project documentation
├── app.py            # Flask application entry point
├── index.py          # Additional routing or logic
├── requirements.txt  # Dependencies for the Python backend
├── vercel.json       # Configuration for Vercel deployment
├── wsgi.py           # WSGI entry point for production
