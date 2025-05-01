import tkinter as tk
import random
import time
import webbrowser

# Sample paragraphs
paragraphs = [
    "The journey has come to an unexpected end. Though the path was filled with moments of triumph, today the odds were simply not in your favor. Every challenge you faced taught you something, and every obstacle helped you grow stronger. This defeat is not the end it’s merely a pause in your story. Take a deep breath, reflect on what you’ve learned, and prepare to rise again. For even in loss, there is a lesson.",
    "GAME OVER. The echo of failure reverberates through the digital void, but do not let it shatter your spirit. Every player stumbles, and every hero must face defeat to know the sweetness of victory. Think back to your best move, your closest call, and remember: perseverance beats perfection. The game may have ended this time, but you are far from finished. Ready your mind and dive back in stronger than ever.",
    "Your journey ends here for now. You’ve navigated twists and turns, braved obstacles, and tested your limits. Though the screen flashes “Game Over,” your progress speaks louder than those two words. This is not failure it’s feedback. It’s an invitation to try again, to press start once more, and rewrite the ending. Champions aren't the ones who never fall, but the ones who rise every time they do.",
    "The game may be over, but the story continues. What you built, what you explored, and what you risked none of it was in vain. This is where many give up, but not you. You understand that true mastery is forged in the fire of repetition. Reflect on your strategy, sharpen your skills, and when you're ready, come back with a vengeance. This was only the rehearsal for your comeback."
]

# Global game state
game_state = {
    'start_time': 0,
    'time_left': 45,
    'score': 0,
    'username': "",
    'game_in_progress': False,
    'wpm': 0,
    'typed_text': "",
    'total_time': 45
}

leaderboard = []

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

def start_game(username, selected_time):
    global game_state
    game_state.update({
        'username': username if username else "Anonymous",
        'score': 0,
        'time_left': selected_time,
        'total_time': selected_time,
        'game_in_progress': False,
        'typed_text': ""
    })

    paragraph = random.choice(paragraphs)
    username_window.destroy()

    game_window = tk.Tk()
    game_window.title("PROTO TYPE")
    center_window(game_window, 900, 650)
    game_window.configure(bg="#f0f4f8")

    label_paragraph = tk.Text(game_window, height=6, width=100, font=("Verdana", 14), wrap="word", bg="#f0f4f8", bd=0)
    label_paragraph.pack(pady=10)
    label_paragraph.config(state="disabled")

    text_input = tk.Text(game_window, font=("Verdana", 14), width=90, height=4, bg="#ffffff", fg="#333333", insertbackground="#0078d4", wrap="word")
    text_input.pack(pady=10)
    text_input.config(state="disabled")

    label_time = tk.Label(game_window, text=f"Time left: {game_state['time_left']}s", font=("Verdana", 14, "bold"), bg="#f0f4f8", fg="#d32f2f")
    label_time.pack()

    label_score = tk.Label(game_window, text="Score: 0", font=("Verdana", 14), bg="#f0f4f8", fg="#0078d4")
    label_score.pack(pady=5)

    leaderboard_label = tk.Label(game_window, text="Leaderboard", font=("Verdana", 16, "bold"), bg="#f0f4f8", fg="#333333")
    leaderboard_label.pack()

    leaderboard_text = tk.Label(game_window, text="", font=("Verdana", 12), justify="left", bg="#f0f4f8", fg="#333333")
    leaderboard_text.pack()

    countdown_label = tk.Label(game_window, text="", font=("Verdana", 20, "bold"), bg="#f0f4f8", fg="#0078d4")
    countdown_label.pack(pady=10)

    footer = tk.Label(game_window, text="GitHub", font=("Verdana", 12), bg="#f0f4f8", fg="#0078d4", cursor="hand2")
    footer.pack(side="bottom", pady=5)
    footer.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/cyberluciferrr"))

    def update_leaderboard():
        leaderboard_display = "\n".join(
            [f"{entry['username']}: {entry['score']} pts (WPM: {entry['wpm']})" for entry in leaderboard[:5]]
        )
        leaderboard_text.config(text=leaderboard_display)

    def highlight_text():
        label_paragraph.config(state="normal")
        label_paragraph.delete("1.0", tk.END)
        typed = text_input.get("1.0", tk.END).strip()
        typed_words = typed.split()
        original_words = paragraph.split()
        for i, word in enumerate(original_words):
            tag = ""
            if i < len(typed_words):
                tag = "correct" if typed_words[i] == word else "incorrect"
            else:
                tag = "remaining"
            label_paragraph.insert(tk.END, word + " ", tag)
        label_paragraph.config(state="disabled")

    def check_input(event=None):
        if not game_state['game_in_progress']:
            return
        game_state['typed_text'] = text_input.get("1.0", tk.END).strip()
        score = count_correct_words(game_state['typed_text'], paragraph)
        game_state['score'] = score
        label_score.config(text=f"Score: {score}")
        highlight_text()

    def count_correct_words(typed, original):
        typed_words = typed.strip().split()
        original_words = original.split()
        correct = sum(1 for i in range(min(len(typed_words), len(original_words))) if typed_words[i] == original_words[i])
        return correct

    def calculate_wpm():
        elapsed = time.time() - game_state['start_time']
        if elapsed <= 0:
            return 0
        correct = count_correct_words(game_state['typed_text'], paragraph)
        return round(correct / (elapsed / 60), 2)

    def end_game():
        game_state['game_in_progress'] = False
        game_state['wpm'] = calculate_wpm()
        label_paragraph.config(state="normal")
        label_paragraph.delete("1.0", tk.END)
        label_paragraph.insert("1.0", "Game Over!")
        label_paragraph.config(fg="#d32f2f", state="disabled")
        label_score.config(text=f"Final Score: {game_state['score']}")
        label_time.config(text=f"WPM: {game_state['wpm']}")
        text_input.config(state="disabled")

        leaderboard.append({
            'username': game_state['username'],
            'score': game_state['score'],
            'wpm': game_state['wpm']
        })
        leaderboard.sort(key=lambda x: x['score'], reverse=True)
        update_leaderboard()

        tk.Button(game_window, text="Play Again", font=("Verdana", 14), bg="#0078d4", fg="white",
                  activebackground="#005ea6", command=lambda: [game_window.destroy(), ask_for_username()]).pack(pady=10)

    def update_timer():
        if game_state['game_in_progress'] and game_state['time_left'] > 0:
            game_state['time_left'] -= 1
            label_time.config(text=f"Time left: {game_state['time_left']}s")
            game_window.after(1000, update_timer)
        elif game_state['game_in_progress']:
            end_game()

    def start_countdown(count=5):
        if count > 0:
            countdown_label.config(text=f"Starting in {count}...")
            game_window.after(1000, start_countdown, count - 1)
        else:
            countdown_label.config(text="")
            game_state['start_time'] = time.time()
            game_state['game_in_progress'] = True
            text_input.config(state="normal")
            text_input.focus()
            update_timer()

    # Apply text tags for color
    label_paragraph.tag_configure("correct", foreground="green")
    label_paragraph.tag_configure("incorrect", foreground="red")
    label_paragraph.tag_configure("remaining", foreground="black")

    update_leaderboard()
    highlight_text()
    text_input.bind("<KeyRelease>", check_input)
    start_countdown()
    game_window.mainloop()

def ask_for_username():
    global username_window, entry_username
    username_window = tk.Tk()
    username_window.title("PROTO TYPE")
    center_window(username_window, 400, 300)
    username_window.configure(bg="#f0f4f8")

    tk.Label(username_window, text="Enter your username:", font=("Verdana", 14), bg="#f0f4f8").pack(pady=10)
    entry_username = tk.Entry(username_window, font=("Verdana", 14))
    entry_username.pack(pady=10)

    tk.Label(username_window, text="Select time limit:", font=("Verdana", 12), bg="#f0f4f8").pack()
    selected_time = tk.IntVar(value=45)
    for t in [30, 45, 60, 90]:
        tk.Radiobutton(username_window, text=f"{t} seconds", variable=selected_time, value=t,
                       font=("Verdana", 11), bg="#f0f4f8").pack(anchor="w", padx=100)

    tk.Button(username_window, text="Play", font=("Verdana", 14), bg="#0078d4", fg="white",
              command=lambda: start_game(entry_username.get(), selected_time.get())).pack(pady=20)

    username_window.mainloop()

ask_for_username()
