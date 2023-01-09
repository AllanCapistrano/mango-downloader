from typing import List

from services import Crawler
from services import Downloader
from services import Uploader
from modules.unionLeitor import parser
from modules.terminal.zip import zip
from modules.terminal.removeFiles import removeFilesAndDirectories

if __name__ == "__main__":
    print("Bem vindo(a) ao Mango Downloader!")
    chapter_link = input("Digite a URL do capítulo que deseja baixar: ")

    if(parser.idValidUrl(chapter_link)):
        crawler: Crawler = Crawler()
        downloader: Downloader = Downloader()
        uploader: Uploader = Uploader()

        manga_pages: List[str] = crawler.getMangaImageUrls(chapter_link)

        downloader.downloadImages(manga_pages)
        compressed_file: str = zip()

        if(compressed_file != None):
            was_uploaded: bool = uploader.upload([compressed_file])

            if(was_uploaded):
                removeFilesAndDirectories()
    else:
        print("Error! URL inválida, tente novamente.")