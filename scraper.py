from utils import check_manga_url, download_manga


print('                                    ───── ⋆⋅☆⋅⋆ ─────')
print('                          Welcome to the Manga Tigre Downloader')
print('                                    ───── ⋆⋅☆⋅⋆ ─────')
print('Select an option:')
option = int(input('1.- Download all chapters\n2.- Download from chapter x to chapter y\n3.- Download chapter x\n4.- Download the last chapter\n 0.- Exit\n Enter the option:  '))

while 5 < option < 0:
    print('Invalid option, please try again')
    option = int(input('1.- Download all chapters\n2.- Download from chapter x to chapter y\n3.- Download chapter x\n4.- Download the last chapter\n 0.- Exit\n Enter the option:  '))

if option == 1:
    manga_title = input('Enter the manga title: ')
    download_manga(manga_title=manga_title)
elif option == 2:
    manga_title = input('Enter the manga title: ')
    initial_chapter = int(input('Enter the initial chapter: '))
    final_chapter = int(input('Enter the final chapter: '))
    download_manga(initial_chapter=initial_chapter, final_chapter=final_chapter, manga_title=manga_title)

elif option == 3:
    manga_title = input('Enter the manga title: ')
    chapter = int(input('Enter the chapter: '))
    download_manga(initial_chapter=chapter, final_chapter=chapter, manga_title=manga_title)

elif option == 4:
    manga_title = input('Enter the manga title: ')
    final_chapter = check_manga_url(manga_title)
    download_manga(manga_title=manga_title, download_last_chapter=True)

elif option == 0:
    print('Bye!')

