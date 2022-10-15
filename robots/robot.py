from pathlib import Path
import time

# import pyperclip

import requests
import shutil

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
    def new_browser(self):
        self.browser = self.pw.firefox.launch(headless=False)
    
        # open the game on browser:
        self.page = self.browser.new_page()
        self.page.goto(self.url)
    
    def close_browser(self):
        self.browser.close()

# This class opens a browser and get the country image. 
class Input(Robot):
    def __init__(self, info, save_path, pw):
        super().__init__(info, save_path, pw)

    def new_browser(self):
        super().new_browser()
    
    def get_link_image(self):
        self.new_browser()
        self.page.wait_for_load_state("networkidle")

        element = self.page.locator(self.locator)
        return self.url + element.get_attribute('src')
    
    # get the code, the two letters that represents the name of the country/local.
    # this method is only necessary when we are using the "Lazy Guesser".
    def code(self):
        return self.get_link_image().split("/")[-2]

    """
    This part is only necessary when we need the country image to compare
    with the list of SVG that represents the countries. This is "the fancy
    mode" to solve the game. It's not working yet :/.

    """
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

class Output(Robot):
    def __init__(self, info, save_path, pw):
        super().__init__(info, save_path, pw)
    
    def new_browser(self):
        super().new_browser()

    def answer(self, country_name):
        self.new_browser()
        self.page.wait_for_load_state("networkidle")
        
        self.page.locator(self.selector).fill(f'{country_name}')
        # a timer, because the selection is really fast
        time.sleep(3)
        self.page.locator(self.button_answer).click()
        # waiting for the full bar of success
        time.sleep(2)
        
        self.page.screenshot(path=self.screenshot, full_page=True)
        self.close_browser()