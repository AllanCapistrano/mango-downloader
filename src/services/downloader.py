from typing import List
from os import system

from command import run

# ------------------------------ Constants ----------------------------------- #
MANGA_NAME_INDEX = 5
MANGA_CHAPTER_INDEX = 6
FILE_EXTENSION_INDEX = 7
# ---------------------------------------------------------------------------- #

class Downloader:
    def downloadImage(self, urls: List[str]) -> None:
        """ Baixa as imagens a partir de uma URL, e coloca no diretório 
        `mangas/<nome do mangá>/<capítulo do mangá>`.

        Parameters
        -----------
        url: :class:`str`
            Url das imagens.
        """
        
        if(len(urls) > 0):
            temp: List[str] = urls[0].split("/")
            directory_name: str = "mangas/" + temp[MANGA_NAME_INDEX] + "/" + temp[MANGA_CHAPTER_INDEX]

            if(self.__createDirectory__(directory_name=directory_name)):
                command: List[str] = ["curl"]
                
                for url in urls:
                    command.append("-O")
                    command.append(url)

                try:
                    run(command=command)
                    
                    directory_name: str = "mangas/'" + temp[MANGA_NAME_INDEX] + "'/" + temp[MANGA_CHAPTER_INDEX]
                    image_extension: str= temp[FILE_EXTENSION_INDEX][3:7]

                    self.__moveFiles__(
                        file_extension=image_extension, 
                        directory_name=directory_name
                    )

                    print("Capítulo do mangá baixado com sucesso!")
                except:
                    print("Erro ao tentar baixar as imagens!")
                    exit()
        else:
            print("Este capítulo não possui páginas para serem baixadas!")

    def __createDirectory__(self, directory_name: str) -> bool:
        """ Cria um diretório a partir do caminho especificado.
        
        Parameters
        ----------
        directory_name: :class:`str`
            Nome do diretório juntamente com o caminho.
        """
        
        try:
            run(command=["mkdir", "-p", directory_name])

            return True
        except:
            print("Erro ao criar o diretório: " + directory_name)

            return False

    def __moveFiles__(self, file_extension: str, directory_name: str) -> bool:
        """ Move todos os arquivos de uma determinada extensão, para o diretório
        especificado.

        Parameters
        ----------
        file_extension: :class:`str`
            Extensão do arquivo.
        directory_name: :class:`str`
            Nome do diretório juntamente com o caminho.

        """
        
        file_extension: str = "*" + file_extension

        try:
            system("mv " + file_extension + " " + directory_name)

            return True
        except:
            return False