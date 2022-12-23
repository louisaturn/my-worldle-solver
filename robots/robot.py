import sys
import time

from pathlib import Path

sys.path.append(".")
from local_guesser.guesser import Lazy_Guesser

class Robot:
    def __init__(self, info, save_path, pw):
        self.pw = pw
        self.save_path = save_path

        self.url           = info["url"]
        self.image         = info["image"]
        self.locator       = info["locator"]
        self.selector      = info["selector"]
        self.attribute     = info["attribute"]
        self.screenshot    = info["screenshot"]
        self.button_share  = info["button_share"]
        self.button_answer = info["button_answer"]
        self.copied_result = info["copied_result"]

    # new browser instance
    def new_browser(self, headless):
        self.browser = self.pw.webkit.launch(headless=headless)
    
        # open the game on browser:
        self.page = self.browser.new_page()
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")
    
    def close_browser(self):
        self.browser.close()

    def get_link_image(self):
        self.new_browser(headless=True)

        image = self.page.locator(self.locator)
        link_image = self.url + image.get_attribute('src')
        
        self.close_browser()
        return link_image

# This class opens a browser and get the country image. 
class GoofyBot(Robot):

    # get the code, the two letters that represents the name of the country/local.
    # this method is only necessary when we are using the "Lazy Guesser".

    def answer(self):
        code_country = self.get_link_image().split("/")[-2]
        country_name = Lazy_Guesser(code_country).answer()

        self.new_browser(headless=False)

        self.page.locator(self.selector).fill(f'{country_name}')
        # a timer, because the selection is really fast
        time.sleep(3)
        self.page.locator(self.button_answer).click()
        # waiting for the full bar of success and the colored thingies <3
        time.sleep(10)
        
        self.page.screenshot(path=Path(f"{self.save_path}/answer").joinpath(self.screenshot), full_page=True)
        self.close_browser()

"""
    This part is only necessary when we need the country image to compare
    with the list of SVG that represents the countries. This is "the fancy
    mode" to solve the game. It's not working yet :/.

"""
# import pyperclip

# import requests
# import shutil

#     # save the country svg on the date directory
#     def save_image(self):
#         file_path = Path(f"{self.save_path}/{self.image}")
#         file_path.parent.mkdir(parents=True, exist_ok=True)

#         req = requests.get(self.link_image, stream = True)
#         if req.status_code == 200:
#             with open(file_path,'wb') as f:
#                 shutil.copyfileobj(req.raw, f)
#                 return "success"
#         else:
#             print('Sorry, I could not get the image of the country')
