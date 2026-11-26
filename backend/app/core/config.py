"""
This file holds global config constants
"""

from pathlib import Path
import json

USERNAME = "tallen21"
USER_ID = "839972291348639744"
SMACKERS_LEAGUE_ID_2025 = "1259602742452690944" # Lexington Smackers
SMACKERS_LEAGUE_ID_2026 = "1332085284707237888" # Lexington Smackers

SMACKERS_USERS = [
    "LongJohnSilvers23",
    "blakespencer18",
    "RKozemko193",
    "SoupOrMan53",
    "JasonGarcia12",
    "Astaton24",
    "Bean216",
    "Jallen2202",
    "Braceandrew8",
    "Cbranham",
    "jackiebaseball",
    "tallen21"
]

BASE_DIR = Path(__file__).resolve().parent
WEEK_FILE = f"{BASE_DIR}/week.in"

def getCurWeek() -> int:
    thisWeek = -1
    try:
        with open(WEEK_FILE, 'r') as weekFile:
            thisWeek = json.load(weekFile)
    except Exception as e:
        print(f"Error loading {WEEK_FILE}")
        print(f"ERROR:\n{e}")
    return thisWeek

CUR_WEEK = getCurWeek()
