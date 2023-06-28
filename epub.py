from PIL import Image
from ebooklib import epub
import os

EPUB_FILES_PATH = './Epubs'

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

def create_output_folder(manga_name: str) -> str:
    """
    :param manga_name: name of the manga
    :return: str with the outputh path created
    """
    if not os.path.exists(EPUB_FILES_PATH):
        os.makedirs(EPUB_FILES_PATH)
    if not os.path.exists(os.path.join(EPUB_FILES_PATH, manga_name)):
        os.makedirs(os.path.join(EPUB_FILES_PATH, manga_name))

    return os.path.join(EPUB_FILES_PATH, manga_name, f'{manga_name}.epub')

def transform_manga_images_to_epub() -> None:
    """
    Transform manga images to epub file
    :return: None
    """
    manga_name = show_and_select_a_manga_folder()

    manga_folder_path = os.path.join('./Mangas', manga_name)
    output_path = create_output_folder(manga_name)

    book = epub.EpubBook()
    book.set_identifier(f'{manga_name}')
    book.set_title(f'{manga_name}')
    book.set_language('en')
    manga_title = os.path.basename(manga_folder_path).replace('_', ' ').title()

    percentage = 0
    spine_items = []
    chapter_list = os.listdir(manga_folder_path)
    chapter_list.sort(key=lambda x: int(x.split('_')[-1]))
    chapter_index = chapter_list[0].split('_')[-1]

    for chapter_folder in chapter_list:
        chapter_index = int(chapter_index)
        print(f'[{percentage}%] - {chapter_folder}')
        percentage = round((int(chapter_index) / len(os.listdir(manga_folder_path))) * 100, 2)
        chapter_path = os.path.join(manga_folder_path, chapter_folder)

        if os.path.isdir(chapter_path):
            chapter_title = f'Chapter {chapter_index}'
            image_html = ''

            image_list = os.listdir(chapter_path)
            image_list.sort(key=lambda x: int(x.split('_')[-2].split('.')[0].replace('image', '')))
            for filename in image_list:
                if filename.endswith('.webp'):
                    image_path = os.path.join(chapter_path, filename)
                    image = Image.open(image_path)

                    image_item = epub.EpubImage()  # Changed this line to EpubImage
                    image_item.file_name = filename  # Using property methods to set the values
                    image_item.media_type = 'image/webp'
                    image_item.content = open(image_path, 'rb').read()  # Set content to the binary data of the image

                    book.add_item(image_item)

                    # Adding each image to the chapter's html content
                    image_html += f'<p><img src="{filename}" alt="image"/></p>'

            c = epub.EpubHtml(title=chapter_title, file_name=f'chapter_{chapter_index}.xhtml')
            c.content = f'<h1>{chapter_title}</h1>{image_html}'
            book.add_item(c)
            spine_items.append(c)

            chapter_index += 1

    book.spine = spine_items

    section = epub.Section(manga_title)
    book.toc.append(section)

    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    epub.write_epub(output_path, book, {})


transform_manga_images_to_epub()