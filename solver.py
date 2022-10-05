from robots.robot import Input

from datetime import date
from playwright.sync_api import sync_playwright


CONST_DICT = {
    'url': 'https://worldle.teuteuf.fr/',
    'image': 'local.svg',
    'button_share': '//*[@id="root"]/div[2]/div[2]/div/div[3]/button',
    'button_answer': '//*[@id="root"]/div[2]/div[2]/div/div[3]/form/div/button',
    'locator': '//html/body/div[1]/div[2]/div/div/div[1]/img',
    'attribute': 'src',
    'selector': '/*[@id="root"]/div[2]/div/div/div[3]/form/div/div/input',
    'screenshot': 'screenshot.png',
    'copied_result': 'result.txt'
}

def guesser_bot(CONST_DICT, save_path):
    with sync_playwright() as pw:
        Input(CONST_DICT, save_path, pw).save_image()
    # await Output(CONST_DICT, save_path).answer()

def dir_name():
    # directory name: today's date
    today = date.today()
    return today.strftime("%d-%b-%Y")


guesser_bot(CONST_DICT, dir_name())