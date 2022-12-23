from robots.robot import GoofyBot

from datetime import date
from pathlib import Path
from playwright.sync_api import sync_playwright

def guesser_bot(const_dict, save_path):
    with sync_playwright() as pw:
        GoofyBot(const_dict, save_path, pw).answer()

def dir_name():
    # directory name: today's date
    today = date.today().strftime("%Y%m%d")
    dir_name = Path(f"{today}/")
    dir_name.parent.mkdir(parents=True, exist_ok=True)
    return dir_name

CONST_DICT = {
    'url'          : 'https://worldle.teuteuf.fr/',
    'image'        : 'local.svg',
    'locator'      : 'img[alt=\"country to guess\"]',
    'selector'     : '[placeholder=\"Country\\, territory\\.\\.\\.\"]',
    'attribute'    : 'src',
    'screenshot'   : 'screenshot.png',
    'button_share' : '//*[@id="root"]/div[2]/div[2]/div/div[3]/button',
    'copied_result': 'result.txt',
    'button_answer': 'button:has-text(\"Guess\")'
}


guesser_bot(CONST_DICT, dir_name())
