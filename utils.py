import json
import os
from typing import Optional

import requests
from bs4 import BeautifulSoup

MANGA_MAIN_PATH = "Mangas"


def check_manga_url(manga_title: str) -> str:
    """
    Check if the manga exists
    :param manga_title: name of the manga to check
    :return: valid manga url
    """
    manga_title = manga_title.replace(' ', '-')
    manga_url = f'https://www.mangatigre.net/manga/{manga_title}'

    check_url = requests.get(manga_url)
    if check_url.status_code != 200:
        raise Exception('Manga not found, please try again')

    return manga_url

def find_last_chapter(manga_title: str) -> int:
    """
    Find the last chapter of a manga
    :param manga_title: title of the manga
    :return: the
    """
    print('Finding the last chapter...')

    url_template = f'https://www.mangatigre.net/manga/{manga_title}'

    response = requests.get(url_template)
    soup = BeautifulSoup(response.text, 'html.parser')
    li_list = soup.findAll('li', {'class': 'pl-1 d-flex'})
    last_chapter_url = li_list[0].a['href']
    chapter_number = last_chapter_url.split('/')[-1]
    return chapter_number


def create_path(dir_name: str) -> str:
    if not os.path.exists(MANGA_MAIN_PATH):
        os.makedirs(MANGA_MAIN_PATH)

    manga_path = os.path.join(MANGA_MAIN_PATH, dir_name)
    if not os.path.exists(manga_path):
        os.makedirs(manga_path)

    return manga_path

def get_chapters_list(manga_title: str, initial_chapter: float) -> list:
    """
    Get the list of all chapters of a manga
    :param manga_title: title of the manga
    :param initial_chapter: the initial chapter to download
    :return: list of chapters
    """
    url_template = f'https://www.mangatigre.net/manga/{manga_title}/{initial_chapter}'

    response = requests.get(url_template)
    soup = BeautifulSoup(response.text, 'html.parser')
    li_list = soup.find('select', {'class': 'form-control rounded-sketch chapters-list mx-100 w-md-auto ml-md-0 mr-md-2 mb-2 mb-md-0 custom-select select-chapters'})
    options = li_list.findAll('option')
    chapters = []

    for li in options:
        chapter_number = li.get('value')
        chapters.insert(0, chapter_number)

    return chapters

def download_images(parent_dir: str, manga_title: str, chapter: int, images: dict) -> None:
    """
    Download the images of a chapter
    :param parent_dir: directory of the manga
    :param manga_title: title of the manga
    :param chapter: number of the chapter
    :param images: dict with the images
    :return: None
    """
    images_list = []
    for image in images:
        image_name = images[image]['name']
        image_url = f'https://i2.mtcdn.xyz/chapters/{manga_title}/{chapter}/{image_name}.webp'
        images_list.append(image_url)

    chapter_dir = f'{parent_dir}/chapter_{chapter}'
    if not os.path.exists(chapter_dir):
        os.makedirs(chapter_dir)

    count = 1
    percentage = 0
    print(f'\nDownloading images from chapter {chapter}\n')
    for image_url in images_list:
        print(f'{int(percentage)}%')
        file_name = image_url.split('/')[-1]
        file_path = f'{chapter_dir}/image{count}_{file_name}'

        response = requests.get(image_url, stream=True)

        with open(file_path, 'wb') as f:
            f.write(response.content)

        count += 1
        percentage += 100 / len(images_list)
    print('100%')
    print('DONE!\n')

def download_manga(
        manga_title: Optional[str] = '',
        download_last_chapter: Optional[bool] = False,
        initial_chapter: Optional[int] = None,
        final_chapter: Optional[str] = 'last',
        single_chapter: Optional[int] = None
) -> None:
    """
    Download a manga from Manga Tigre
    :param initial_chapter: the initial chapter to download
    :param final_chapter: the final chapter to download
    :param manga_title: title of the manga
    :param download_last_chapter: check if the user wants to download the last chapter
    :param single_chapter: check if the user wants to download a single chapter
    :return: None
    """
    manga_title = manga_title.replace(' ', '-').lower()
    parent_dir = create_path(manga_title)
    chapter_list = get_chapters_list(manga_title, initial_chapter)
    print('Manga found! Downloading...')
    if single_chapter is not None:
        initial_chapter = single_chapter
        final_chapter = single_chapter

    if final_chapter == 'last' or download_last_chapter:
        final_chapter = find_last_chapter(manga_title)
    if final_chapter is not None and single_chapter is None:
        final_chapter = int(final_chapter) if '.' not in final_chapter else float(final_chapter)

    if initial_chapter is None and final_chapter is None and single_chapter is None:
        initial_chapter = 1 if not download_last_chapter else find_last_chapter(manga_title)
        final_chapter = find_last_chapter(manga_title) if not download_last_chapter else initial_chapter
        print('The last chapter is: ', final_chapter)

    if download_last_chapter:
        initial_chapter = final_chapter


    if final_chapter < initial_chapter:
        raise Exception('The initial chapter must be less than the final chapter')


    for chapter in chapter_list:
        if '.' in chapter:
            chapter = float(chapter)
        else:
            chapter = int(chapter)
        if initial_chapter > chapter:
            continue
        if final_chapter < chapter:
            break

        percent = round((chapter - initial_chapter) / (final_chapter - initial_chapter) * 100, 2) if final_chapter != initial_chapter else 100
        print('╌──═❁═──╌' * 5)
        print(f'\n\nDownloading chapter {chapter}... {percent}% Completed\n\n')
        url_template = f'https://www.mangatigre.net/manga/{manga_title}/{chapter}'
        url = url_template.format(chapter=chapter)

        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        scripts = soup.findAll('script')
        window_chapter = scripts[8].text.strip().replace('window.chapter = ', '').replace(';', '').replace('\'', '')

        try:
            chapter_dict = json.loads(window_chapter)
        except json.decoder.JSONDecodeError:
            print('JSONDecodeError, trying again...')
            window_chapter = scripts[9].text.strip().replace('window.chapter = ', '').replace(';', '').replace('\'', '')
            chapter_dict = json.loads(window_chapter)

        images = chapter_dict['images']

        download_images(parent_dir, manga_title, chapter, images)
        print(f'Chapter {chapter} downloaded! {percent}%')