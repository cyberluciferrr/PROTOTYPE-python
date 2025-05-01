# PROTOTYPE-python

# 🧠 Typing Speed Game (Python + Tkinter)

A simple and interactive typing speed game built using **Python** and **Tkinter GUI**. It challenges users to type as fast and accurately as possible within a selected time limit.

## 🚀 Features

- 🖱️ Graphical User Interface (Tkinter)
- ⏳ Selectable time duration (30, 60, 120 seconds)
- 📄 Random paragraph generation
- ✅ Live word-by-word accuracy feedback
- 📈 Real-time score and WPM (Words Per Minute)
- 🏆 Top 5 Leaderboard with usernames
- 🔁 Play again option after time ends

## 📸 Screenshot

*(Add a screenshot of your game window here if you'd like)*

## 🛠️ Tech Stack

- **Language:** Python 3
- **GUI:** Tkinter
- **Modules Used:** 
  - `random` for paragraph selection  
  - `time` for timer and WPM calculation  
  - `webbrowser` (optional - for GitHub link or help button)

## 🧠 How It Works

1. User is asked to enter their name and choose a time duration.
2. A random paragraph appears.
3. User starts typing in the text box.
4. The game gives real-time feedback on typing accuracy.
5. After the time is up, it shows:
   - Total score
   - WPM
   - Leaderboard with top scores
6. Option to play again.


## 🔢 WPM Calculation

WPM is calculated using this formula:

## 📝 Example Paragraphs

A few random tongue-twisters or quotes are stored in a list:
```python
paragraphs = [
    "The quick brown fox jumps over the lazy dog.",
    "Pack my box with five dozen liquor jugs.",
    "A journey of a thousand miles begins with a single step."
]

🎯 Possible Improvements
Save the leaderboard to a local file

Add login/signup with password

Theme switching (light/dark mode)

Add difficulty levels (easy/medium/hard

