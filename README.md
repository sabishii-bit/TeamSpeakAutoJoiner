# TeamSpeakAutoJoiner

Made for my friend, Shade, so they can join TeamSpeak calls while they're still asleep.
The reasons for why this was needed were never extrapolated upon, but I don't question the work given to me.

# Usage

Run the binary located in dist. A cmd or PowerShell window will open with instructions from there.


# Compiling Distributable
```
pyinstaller --onefile --paths .venv/Lib/site-packages src/autojoiner.py
```