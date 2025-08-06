# A–Z Soundboard App

**Colorful buttons, alphabet sounds, and a whole lot of Python!**

## Project Overview

This is a fun little soundboard built using Python's `tkinter`, where each button from A to Z plays its corresponding sound. With randomly colored buttons and a background image for extra style, it’s a simple yet satisfying GUI project — perfect for practicing Python fundamentals.

---

## 💡 What I Learned

As a student, this project helped me explore and understand:

* **Audio Integration**: Using `pygame.mixer` to load and play `.mp3` files.
* **Alphabet Looping**: Using the `string` module to loop through A to Z without writing 26 separate functions.
* **Random Styling**: Generating different button colors using Python’s `random.choice()`.
* **GUI Layout**: Creating a grid layout with rows and columns using `tkinter`.
* **Image Backgrounds**: Adding and positioning a background image with `Pillow (PIL)` and `Label`.

---

## Tech Stack

* **Python**
* **Tkinter** – for GUI
* **Pygame** – for sound
* **Pillow (PIL)** – for image handling
* **Random, String modules** – for logic and styling

---

## How It Works

Each button corresponds to a letter from A to Z. When clicked:

1. It loads a sound file named like `a.mp3`, `b.mp3`, etc.
2. It plays the sound.
3. Each button has a random color from a preset list.
4. Buttons are neatly arranged in a grid layout (10 per row max).

---

## Try It Yourself

Make sure to include all these `.mp3` files (a.mp3 to z.mp3) in the same directory, and don't forget to install the required libraries:

```bash
pip install pygame Pillow
```

---

## Final Thoughts

This project started as a fun experiment and turned into a great learning experience. If you're a beginner like me, trying out small projects like this helps you connect the dots between Python modules, logic, and design.

---

Let me know if you want a version with screenshots, installation steps, or GitHub badges too!
