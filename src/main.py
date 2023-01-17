from typing import List, Dict
from os import system
from re import sub

from services import Crawler
from services import Downloader
from services import Uploader
from modules.unionLeitor import getMangaListPage, isUrl, isValidUrl, isMangaLink
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
        link: str = input("Digite o nome do mangá ou a URL do capítulo ou mangá que deseja baixar: ")

        if(isUrl(link)):
            if(isMangaLink(link)): # Caso seja um link de um mangá.
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
        else:
            manga_name: str = link

            manga_list_page: str = getMangaListPage(manga_name)
            last_page: int = crawler.getLastPageNumberMangaList(manga_list_page)
            
            mangas: List[Dict[str, str]] = []

            for page_number in range(0, last_page):
                url: str = sub(r"\d", f"{page_number + 1}", manga_list_page)

                mangas = mangas + crawler.getAllMangaNamesAndUrls(url)

            if(len(mangas) > 0):
                result: List[Dict[str, str]] = []

                for manga in mangas:
                    if(manga["manga_name"].lower().find(manga_name.lower()) != -1):
                        result.append(manga)

                for index in range(0, len(result)):
                    print(f"{index + 1} - {result[index]['manga_name']}")

                manga_option: int = -1

                while(manga_option <= 0 or manga_option > len(result)):
                    try:
                        manga_option: int = int(input("Digite o número correspondente ao mangá que deseja baixar: "))
                    except:
                        print("Opção inválida! Tente novamente.")

                    if(manga_option == 0 or manga_option > len(result)):
                        print("Opção inválida! Tente novamente.")

                manga_option = manga_option - 1

                print(manga_option)

                # TODO: Exibir quais são as opções de capítulos disponíveis para o usuário baixar.
            else:
                chapters.append(
                    {
                        "chapter_link": link,
                        "downloaded": False
                    }
                )

        option: str = input("Deseja baixar algo mais (S/n)? ")

        if(option != "S" and option != "s"):
            print("Opção inválida! Tente novamente.")

    system("clear") # Limpando o terminal

    # Fazendo o download dos capítulos.
    for chapter in chapters:
        if(isValidUrl(chapter["chapter_link"])):
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