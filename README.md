# Memory Match Game

A card-matching game built in Python with a graphical interface. Flip cards to find all 6 matching pairs.

## Features
- Randomly shuffled cards each game
- Cards stay face up when matched and flip back when they don't
- Win message after all 6 pairs are found
- Images resized at high quality using Pillow

## Requirements
- Python 3
- pyfltk (`pip install pyfltk`)
- Pillow (`pip install pillow`)
- Image files in the same folder as the program: a cover image named `Garfield_Logo.png` and six card images (`Garf.png`, `Arlene.png`, `Nermal.png`, `Lasagna.png`, `Odie.png`, `Jon.png`). These are not included, so use your own PNG images with the same names, or edit the filenames in the code.

## How to Run
```
python memory_game.py
```

## How to Play
Click a card to reveal it, then click a second card. Matching cards stay revealed. Non-matching cards flip back on your next click. Find all 6 pairs to win.
