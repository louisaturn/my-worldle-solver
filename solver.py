from robots.robot import GoofyBot

from datetime import date
from playwright.sync_api import sync_playwright

def guesser_bot(const_dict, save_path):
    with sync_playwright() as pw:
        #code = GoofyBot(const_dict, save_path, pw).code()
        #country_name = Lazy_Guesser(code).answer()
        GoofyBot(const_dict, save_path, pw).answer()

def dir_name():
    # directory name: today's date
    today = date.today()
    return today.strftime("%Y%m%d")

CONST_DICT = {
    'url'          : 'https://worldle.teuteuf.fr/',
    'image'        : 'local.svg',
    'locator'      : 'country to guess',
    'selector'     : 'Country, territory...',
    'attribute'    : 'src',
    'screenshot'   : 'screenshot.png',
    'button_share' : '//*[@id="root"]/div[2]/div[2]/div/div[3]/button',
    'copied_result': 'result.txt',
    'button_answer': 'Guess'
}


guesser_bot(CONST_DICT, dir_name())
