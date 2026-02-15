import random
import tkinter as tk
import pygame
from PIL import Image, ImageTk

# Initialize music mixer
pygame.mixer.init()

# Image paths
images = {
    "happy": "images/happy.jpg",
    "sad": "images/sad.jpg",
    "excited": "images/excited.jpg",
    "relaxed": "images/relaxed.jpg"
}

# Music paths
music = {
    "happy": "music/happy.mp3",
    "sad": "music/sad.mp3",
    "excited": "music/excited.mp3",
    "relaxed": "music/relaxed.mp3"
}

# Function to get quotes from file
def get_quotes(mood):
    try:
        with open(f"quotes/{mood}.txt", "r", encoding="utf-8") as file:
            quotes = file.readlines()
        return [q.strip() for q in quotes]
    except FileNotFoundError:
        return ["No quotes found for this mood."]

# Play music
def play_song(mood):
    pygame.mixer.music.load(music[mood])
    pygame.mixer.music.play()

# Stop music
def stop_music():
    pygame.mixer.music.stop()

# Change background image
def change_background(mood):
    path = images.get(mood)
    if path:
        img = Image.open(path)
        img = img.resize((800, 600))
        bg_img = ImageTk.PhotoImage(img)
        bg_label.configure(image=bg_img)
        bg_label.image = bg_img

# Mood function
def mood(selected_mood):
    quotes = get_quotes(selected_mood)
    result = random.choice(quotes)

    message.config(text=result, font=("Arial", 14, "bold"))

    play_song(selected_mood)
    change_background(selected_mood)


# GUI Setup
window = tk.Tk()
window.title("Mood-Based Music & Quote Player")
window.geometry("800x600")

bg_label = tk.Label(window)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

title_label = tk.Label(window,
                       text="What's Your Mood Today?",
                       font=("Arial", 20, "bold"),
                       bg="lightblue",
                       fg="purple")
title_label.pack(pady=20)

# Buttons
button_frame = tk.Frame(window, bg="lightblue")
button_frame.pack(pady=20)

tk.Button(button_frame, text="HAPPY 😊", width=15,
          command=lambda: mood("happy")).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="SAD 😢", width=15,
          command=lambda: mood("sad")).grid(row=0, column=1, padx=10)

tk.Button(button_frame, text="EXCITED 🤩", width=15,
          command=lambda: mood("excited")).grid(row=0, column=2, padx=10)

tk.Button(button_frame, text="RELAXED 😌", width=15,
          command=lambda: mood("relaxed")).grid(row=0, column=3, padx=10)

# Quote display
message = tk.Label(window,
                   text="",
                   wraplength=600,
                   bg="lightblue",
                   fg="purple")
message.pack(pady=30)

# Stop music button
tk.Button(window, text="Stop Music", width=20,
          command=stop_music).pack(pady=10)

window.mainloop()
