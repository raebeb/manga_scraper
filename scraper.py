import argparse
from utils import download_manga

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download manga from Manga Tigre.')

    parser.add_argument('manga_title', type=str, help='Title of the manga')
    parser.add_argument('-i', '--initial_chapter', type=int, help='Initial chapter to download')
    parser.add_argument('-f', '--final_chapter', type=str, help='Final chapter to download')
    parser.add_argument('-l', '--download_last_chapter', action='store_true', help='Download the last chapter')
    parser.add_argument('-s', '--single_chapter', type=int, help='Download a single chapter')

    args = parser.parse_args()

    if not any(vars(args).values()):
        parser.error("No arguments provided!")

    else:
        params = vars(args)
        download_manga(**params)

    print("Done!")
    print("Bye! ฅ^•ﻌ•^ฅ ")
