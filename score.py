import os

HIGHSCORE_FILE = "highscore.txt"
def load_highscore():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as f:
            try:
                return int(f.read().strip())
            except:
                return 0
    return 0

def save_highscore(score):
    current = load_highscore()
    if score > current:
        with open(HIGHSCORE_FILE, "w") as f:
            f.write(str(score))
        return True  # yeni yüksek skor
    return False

def reset_highscore():
    with open(HIGHSCORE_FILE, "w") as f:
        f.write("0")
