import json

import requests
from bs4 import BeautifulSoup
import os

# Set the URL and the parent directory to save the images
initial_chapter = 130
final_chapter = 200
url_template = 'https://www.mangatigre.net/manga/vinland-saga/{chapter}'
parent_dir = 'vinland_saga'

# Create the parent directory if it doesn't exist
if not os.path.exists(parent_dir):
    os.makedirs(parent_dir)

# Iterate over the chapters and download the images
for chapter in range(initial_chapter, final_chapter + 1):
    # Construct the URL for the current chapter
    url = url_template.format(chapter=chapter)

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    scripts = soup.findAll('script')
    window_chapter = scripts[8].text.strip().replace('window.chapter = ', '').replace(';', '').replace('\'', '')
    chapter_dict = json.loads(window_chapter)
    images = chapter_dict['images']
    # print(chapter_dict['images'])

    images_list = []
    for image in images:
        image_name = images[image]['name']
        image_url = f'https://i2.mtcdn.xyz/chapters/vinland-saga/{chapter}/{image_name}.webp'
        images_list.append(image_url)

   # Create a directory for the current chapter
    chapter_dir = f'{parent_dir}/chapter_{chapter}'
    if not os.path.exists(chapter_dir):
        os.makedirs(chapter_dir)

    # Find all the images on the page

    # Download each image
    for image_url in images_list:
        # Construct the file name
        file_name = image_url.split('/')[-1]
        file_path = f'{chapter_dir}/{file_name}'

        # Send a GET request to the image URL
        response = requests.get(image_url, stream=True)
        # print(response.content)

        # Save the image to disk
        with open(file_path, 'wb') as f:
            f.write(response.content)
