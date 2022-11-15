import code_contries

class LocalGuesser:
     def __init__(self, code_country):
        self.country = code_country
        self.names = code_contries.code_to_names()

"""
The "Lazy Guesser" only look for the two letters that represents the country
on the link of the country image. Yes, I'm cheating, shame on me ;D.

"""
class Lazy_Guesser(LocalGuesser):
    def answer(self):
        return self.names[self.country.upper()].upper()

"""
The "Fancy Guesser" is inactive, because I'm still learning how to
compare two SVGs. I tried base64 but the image that I got by request
and the SVGs of the directory "countries" do not match perfectly
TODO: explicar o problema

"""        
# from pathlib import Path
# from PIL import Image

# class Fancy_Guesser(LocalGuesser):
#     def country_search(self):
#         for country_directory in self.countries.iterdir():
#             self.compare_images(country_directory, self.local)

#     def answer(self, country_dir):
#         p = Path(country_dir).glob('**/svg')

#         # check if there's some svg file to compare
#         dir_images = [x for x in p if x.is_file()]
#         if dir_images:
#             if self.its_a_match(dir_images[0], self.local_image):
#                 return country_dir.stem
#         return None

#     def its_a_match(self):
#         listed_country_image = Image.open(Path(country).joinpath('vector.svg'))
#         if list(self.local.getdata()) == list(listed_country_image.getdata()):
#             return True
#         return False
