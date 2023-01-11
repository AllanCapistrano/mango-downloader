from typing import List, Dict
from os import system

from services import Crawler
from services import Downloader
from services import Uploader
from modules.unionLeitor import parser
from modules.terminal.zip import zip
from modules.terminal.removeFiles import removeFilesAndDirectories

if __name__ == "__main__":
    crawler: Crawler = Crawler()
    downloader: Downloader = Downloader()
    uploader: Uploader = Uploader()

    chapters: List[Dict[str, bool]] = []

    option: str = ""

    print("Bem vindo(a) ao Mango Downloader!")

    while(option != "N" and option != "n"):
        link: str = input("Digite a URL do capítulo ou mangá que deseja baixar: ")

        if(parser.isMangaLink(link)): # Caso seja um link de um mangá.
            for chapter_link in crawler.getChaptersUrls(link):
                chapters.append(
                    {
                        "chapter_link": chapter_link,
                        "downloaded": False
                    }
                )
        else:
            chapters.append(
                {
                    "chapter_link": link,
                    "downloaded": False
                }
            )
        
        option: str = input("Deseja baixar mais algum capítulo ou mangá (S/n)? ")

        if(option != "S" and option != "s"):
            print("Opção inválida! Tente novamente.")

    system("clear") # Limpando o terminal

    # Fazendo o download dos capítulos.
    for chapter in chapters:
        if(parser.isValidUrl(chapter["chapter_link"])):
            crawler: Crawler = Crawler()
            downloader: Downloader = Downloader()
            uploader: Uploader = Uploader()

            manga_pages: List[str] = crawler.getMangaImageUrls(
                chapter["chapter_link"]
            )

            chapter["downloaded"] = downloader.downloadImages(manga_pages)
        else:
            chapter["downloaded"] = False

    # Verificando se todos os capítulos foram baixados com sucesso.
    for chapter in chapters:
        if(not chapter["downloaded"]):
            print("Não foi possível baixar o capítulo do link: " 
                + chapter["chapter_link"])
    
    # Comprimindo os arquivos.
    compressed_file: str = zip()

    # Fazendo o upload dos arquivos.
    if(compressed_file != None):
        was_uploaded: bool = uploader.upload([compressed_file])

        if(was_uploaded):
            removeFilesAndDirectories()