# from local_guesser.guesser import LocalGuesser

import requests
import shutil


class Robot:
    def __init__(self, info, save_path, pw):
        self.url = info["url"]
        self.image = info["image"]
        self.locator = info["locator"]
        self.attribute = info["attribute"]
        self.screenshot = info["screenshot"]
        self.copied_result = info["copied_result"]
        self.save_path = save_path

        # new browser instance
        self.browser = pw.firefox.launch(headless=False)
    
        # open the game on browser:
        self.page = self.browser.new_page()
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")

# This class opens a browser and get the country image. 
class Input(Robot):
    def __init__(self, info, save_path, pw):
        super().__init__(info, save_path, pw)

        # get image link
        element = self.page.locator(self.locator)
        self.link_image = self.url + element.get_attribute('src')

    def save_image(self):
        req = requests.get(self.link_image, stream = True)
        if req.status_code == 200:
            with open(self.save_path + self.image,'wb') as f:
                shutil.copyfileobj(req.raw, f)
                # return "success"
        # else:
        #     print('Sorry, I could not get the image of the country')

# class Output(Robot):
#     def __init__(self, info, save_path):
#         super().__init__(self)

#     #find and select the local name
#      def answer(self):
#         self.choose_option(self)
#         self.page.wait_for_load_state("networkidle")

#         # screenshot and txt file with "SHARE" results
#         self.page.screenshot(path="{path}/{self.screenshot}")
#         # TODO: click SHARE, copy and paste in a txt file
#         # page.wait_for_load_state("networkidle")

#         self.browser.close()

#      def choose_option(self):
#         selector = self.page.locator(self.selector)

#         option = LocalGuesser().final_answer()
        
#         # page.wait_for_load_state("networkidle")
#         self.page.select_option(selector, option)
