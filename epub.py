from PIL import Image
from ebooklib import epub
import os


def get_all_manga_folders() -> list:
    """
    Get all manga folders
    :return: list of manga folders
    """
    return os.listdir('./Mangas')


def show_and_select_a_manga_folder() -> str:
    """
    Show all manga folders with a number to user to selecy
    :return: Manga folder selected
    """
    manga_folders = get_all_manga_folders()
    print('Mangas:')
    for manga in manga_folders:
        print(f' {manga_folders.index(manga) + 1} - {manga}')

    manga_folder = int(input('Select a manga (insert the number here) --> '))
    while manga_folder > len(manga_folders):
        print('Invalid number, try again')
        manga_folder = int(input('Select a manga (insert the number here) --> '))

    manga_name = manga_folders[manga_folder - 1]

    return manga_name


def transform_manga_images_to_epub() -> None:
    """
    Transform manga images to epub
    :return: None
    """
    percent = 0
    manga_name = show_and_select_a_manga_folder()
    manga_path = f'./Mangas/{manga_name}'
    manga_chapters = os.listdir(manga_path)
    manga_chapters.sort()

    book = epub.EpubBook()
    book.set_identifier('id123456')
    book.set_title(manga_name)
    book.add_author('Manga Tigre')

    for manga_chapter in manga_chapters:
        print(f'Chapter {manga_chapter} - {percent}%')
        percent = round((manga_chapters.index(manga_chapter) / len(manga_chapters)) * 100, 2)
        chapter_path = f'{manga_path}/{manga_chapter}'
        chapter_images = os.listdir(chapter_path)
        chapter_images.sort()

        chapter = epub.EpubHtml(title=f'Chapter {manga_chapter}')
        chapter.set_content(f'<h1>Chapter {manga_chapter}</h1><br><br>')

        for chapter_image in chapter_images:
            image_path = f'{chapter_path}/{chapter_image}'
            image = Image.open(image_path)
            width, height = image.size
            # image = image.resize((int(width / 2), int(height / 2)))
            image.save(image_path)

            image_item = epub.EpubImage(uid=chapter_image, file_name=chapter_image, media_type='image/jpeg')


            chapter.add_item(image_item)
            # chapter.set_content(f'<img src="{chapter_image}">')

        book.add_item(chapter)

        book.toc = (epub.Link(f'{manga_chapter}.xhtml', f'{manga_chapter}', f'{manga_chapter}'),)

    output = f'./Mangas/{manga_name}/{manga_name}.epub'
    epub.write_epub(output, book, {})

    print(f'Chapters: {manga_chapters}')


transform_manga_images_to_epub()