import subprocess
from selenium import webdriver
from get_image_links import fetch_image_urls
from persist_image import persist_image
import os
import sys

# This is the path I use
# DRIVER_PATH = '.../Desktop/Scraping/chromedriver 2'
# Put the path for your ChromeDriver here
DRIVER_PATH = './chromedriver.exe'
wd = webdriver.Chrome(executable_path=DRIVER_PATH)


def search_and_download(search_term: str, driver_path: str,  number_images=int, target_path='./images'):
    target_folder = os.path.join(
        target_path, '_'.join(search_term.lower().split(' ')))

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    with webdriver.Chrome(executable_path=driver_path) as wd:
        res = fetch_image_urls(search_term, number_images,
                               wd=wd, sleep_between_interactions=0.5)
    search_term = search_term.replace(' ', '_')
    for elem in res:
        persist_image(target_folder, elem)
    subprocess.call([sys.executable, 'C:\\Users\\Admin\\Desktop\\Python\\GoogleCollage\\collage_maker.py', '-f', f'images/{search_term}', '-o',
                     f'images/small_collages/{search_term}.png', '-w', '1000', '-i', '200', '-s'])
