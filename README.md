
---

# Anki Flashcard Interface

## Overview

A simple tool for creating vocabulary flashcards in Anki. 

---

## Features

* Simple Tkinter-based GUI for entering words.
* Works with **Anki** through **AnkiConnect**.
* Automatically creates the default deck **"vocabular"** if it doesn’t already exist.
* Recommendations for a cleaner look: Align flashcard text to **left** in AnkiDroid.

---

## Requirements

* Python 3 (tested on Python 3.12)
* [Anki](https://apps.ankiweb.net/) installed and running.
* [AnkiConnect](https://ankiweb.net/shared/info/2055492159) add-on installed and running.
* pip-installed dependencies:

  ```
  requests>=2.0.0
  ```
* tkinter for GUI (usually included with Python)

---

## Installation

It is recommended to use a Python virtual environment to install dependencies safely. You can create and activate one using python3 -m venv venv and source venv/bin/activate (Linux/macOS) or venv\Scripts\activate (Windows), then run pip install -r requirements.txt.

1. Clone this repository:

   ```bash
   git clone https://github.com/EragonTheGuy/AnkiCardInterface.git
   cd AnkiCardINterface
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Open and run the GUI:

   ```bash
   python main.py
   ```
4. Make sure **Anki** and **AnkiConnect** are running.

---

## Usage

1. Launch the app with `python main.py`.
2. Enter a word, select a card type, and choose whether to include pronunciation.
3. Click to generate and send the flashcard to Anki.
4. Cards will appear in the **"vocabular"** deck.

## Notes

* For the best viewing experience in AnkiDroid, set card text alignment to **left**.
* Requires **Anki** to be running in the background with **AnkiConnect** enabled.


