from pathlib import Path
from PIL import Image

class LocalGuesser:
    def __init__(self, local_dir, countries):
        self.local = Image.open(local_dir)
        self.countries = countries
    
    def compare_imgs(self, img):
        if list(self.local.getdata()) == list(img.getdata()):
            return True
        return False

    # look for a match on data/countries directory
    def compare(self):
        for country in self.countries:
            country_img = Image.open(Path(country).joinpath('vector.svg'))
            if self.compare_imgs(country_img):
                return country
        return None

    # get the name of the directory and give the name of the country
    def answer(two_letters):
        pass