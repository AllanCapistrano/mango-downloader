from typing import List

from services.crawler import Crawler
from services.downloader import Downloader
from services.unionLeitor import parser

if __name__ == "__main__":
    print("Bem vindo(a) ao Mango Downloader!")
    chapter_link = input("Digite a URL do capítulo que deseja baixar: ")

    if(parser.idValidUrl(chapter_link)):
        crawler = Crawler()
        downloader = Downloader()

        manga_pages: List[str] = crawler.getMangaImageUrls(chapter_link)

        downloader.downloadImage(manga_pages)
    else:
        print("Error! URL inválida, tente novamente.")