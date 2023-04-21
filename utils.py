import json
import os

import requests
from bs4 import BeautifulSoup


def check_manga_url(manga_title:str) -> str:
    """
    Check if the manga exists
    :param manga_title: name of the manga to check
    :return: valid manga url
    """
    manga_title = manga_title.replace(' ', '-')
    manga_url = f'https://www.mangatigre.net/manga/{manga_title}'

    check_url = requests.get(manga_url)
    while check_url.status_code != 200:
        print('Manga not found, please try again')
        manga_title = input('Enter the manga title: ')
        manga_title = manga_title.replace(' ', '-')
        manga_url = f'https://www.mangatigre.net/manga/{manga_title}'
        check_url = requests.get(manga_url)

    return manga_url

def find_last_chapter(manga_title:str) -> int:
    """
    Find the last chapter of a manga
    :param manga_title: title of the manga
    :return: the
    """
    print('Finding the last chapter...')
    chapter = 1

    url_template = f'https://www.mangatigre.net/manga/{manga_title}'

    response = requests.get(url_template)
    soup = BeautifulSoup(response.text, 'html.parser')
    li = soup.findAll('li')
    print(li[0])
    return 2

    # while response.status_code == 200:
    #     chapter += 1
    #     url_template = f'https://www.mangatigre.net/manga/{manga_title}/{chapter}'
    #     url = url_template.format(chapter=chapter)
    #     response = requests.get(url)
    # return chapter - 1

def download_manga(initial_chapter:int = None, final_chapter:int = None, manga_title:str = '', download_last_chapter:bool = False) -> None:
    """
    Download a manga from Manga Tigre
    :param initial_chapter: the initial chapter to download
    :param final_chapter: the final chapter to download
    :param manga_title: title of the manga
    :param download_last_chapter: check if the user wants to download the last chapter
    :return: None
    """
    manga_title = manga_title.replace(' ', '-')
    manga_url = check_manga_url(manga_title)
    parent_dir = f'./{manga_title}'

    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)

    if initial_chapter is None and final_chapter is None:
        initial_chapter = 1 if not download_last_chapter else find_last_chapter(manga_title)
        final_chapter = find_last_chapter(manga_title) if not download_last_chapter else initial_chapter
        print('The last chapter is: ', final_chapter)

    for chapter in range(initial_chapter, final_chapter + 1):
        percent = round((chapter - initial_chapter) / (final_chapter - initial_chapter) * 100, 2) if final_chapter != initial_chapter else 100
        # Construct the URL for the current chapter
        print(f'Downloading chapter {chapter}... {percent}%')
        url_template = f'https://www.mangatigre.net/manga/{manga_title}/{chapter}'
        url = url_template.format(chapter=chapter)
        print(url)

        # Send a GET request to the URL
        response = requests.get(url)

        # Parse the HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        scripts = soup.findAll('script')
        window_chapter = scripts[8].text.strip().replace('window.chapter = ', '').replace(';', '').replace('\'', '')
        chapter_dict = json.loads(window_chapter)
        images = chapter_dict['images']

        images_list = []
        for image in images:
            image_name = images[image]['name']
            image_url = f'https://i2.mtcdn.xyz/chapters/{manga_title}/{chapter}/{image_name}.webp'
            images_list.append(image_url)

        # Create a directory for the current chapter
        chapter_dir = f'{parent_dir}/chapter_{chapter}'
        if not os.path.exists(chapter_dir):
            os.makedirs(chapter_dir)

        # Download each image
        count = 1
        for image_url in images_list:
            # Construct the file name
            file_name = image_url.split('/')[-1]
            file_path = f'{chapter_dir}/image{count}_{file_name}'

            # Send a GET request to the image URL
            response = requests.get(image_url, stream=True)
            # print(response.content)

            # Save the image to disk
            with open(file_path, 'wb') as f:
                f.write(response.content)

            count += 1
        print(f'Chapter {chapter} downloaded! {percent}%')