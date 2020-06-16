import random
import json
from search_and_download import search_and_download
import subprocess
import sys
DRIVER_PATH = './chromedriver.exe'


def main():
    with open('animals.json') as json_file:
        data = json.load(json_file)
        for i in range(3):
            x = data[random.randint(0, 223)]
            print(x)
            search_and_download(x + ' animal', DRIVER_PATH, 25)


main()
subprocess.call([sys.executable, 'C:\\Users\\Admin\\Desktop\\Python\\GoogleCollage\\collage_maker.py', '-f', f'images/small_collages', '-o',
                 f'big_collage.png', '-w', '10000', '-i', '900', '-s'])
