from typing import List, Dict
from os import system

from services import Crawler
from services import Downloader
from services import Uploader
from modules.unionLeitor import parser
from modules.terminal.zip import zip
from modules.terminal.removeFiles import removeFilesAndDirectories

if __name__ == "__main__":
    print("Bem vindo(a) ao Mango Downloader!")

    chapter_link: str = input("Digite a URL do capítulo que deseja baixar: ")
    chapters: List[Dict[str, bool]] = [
        {
            "chapter_link": chapter_link,
            "downloaded": False
        }
    ]

    option: str = input("Deseja baixar mais algum capítulo (S/n)? ")

    while(option != "N" and option != "n"):
        if(option != "S" and option != "s"):
            print("Opção inválida! Tente novamente.")

        chapter_link: str = input("Digite a URL do capítulo que deseja baixar: ")    
        chapters.append(
            {
                "chapter_link": chapter_link,
                "downloaded": False
            }
        )

        option: str = input("Deseja baixar mais algum capítulo (S/n)? ")

    system("clear") # Limpando o terminal

    # Fazendo o download dos capítulos.
    for chapter in chapters:
        if(parser.idValidUrl(chapter["chapter_link"])):
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