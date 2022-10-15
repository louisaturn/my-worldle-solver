from robots.robot import Input, Output
from local_guesser.guesser import Lazy_Guesser

from datetime import date
from playwright.sync_api import sync_playwright

def guesser_bot(const_dict, save_path):
    with sync_playwright() as pw:
        code = Input(const_dict, save_path, pw).code()
        country_name = Lazy_Guesser(code).answer()
        Output(const_dict, save_path, pw).answer(country_name)

def dir_name():
    # directory name: today's date
    today = date.today()
    return today.strftime("%Y%m%d")

CONST_DICT = {
    'url'          : 'https://worldle.teuteuf.fr/',
    'image'        : 'local.svg',
    'locator'      : '//*[@id="page-content"]/div[2]/div[2]/div/div/div[1]/div/img',
    'selector'     : '//html/body/div[1]/div/div/div[2]/div[2]/div/div/div[3]/form/div/div/input',
    'attribute'    : 'src',
    'screenshot'   : 'screenshot.png',
    'button_share' : '//*[@id="root"]/div[2]/div[2]/div/div[3]/button',
    'copied_result': 'result.txt',
    'button_answer': '//html/body/div[1]/div/div/div[2]/div[2]/div/div/div[3]/form/div/button'
}


guesser_bot(CONST_DICT, dir_name())
