from typing import List

from command import run

from modules.terminal import createDirectory
from modules.terminal import moveFiles

# ------------------------------ Constants ----------------------------------- #
MANGA_NAME_INDEX = 5
MANGA_CHAPTER_INDEX = 6
FILE_EXTENSION_INDEX = 7
# ---------------------------------------------------------------------------- #

class Downloader:
    def downloadImages(self, urls: List[str]) -> None:
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

            if(createDirectory(directory_name=directory_name)):
                command: List[str] = ["curl"]
                
                for url in urls:
                    command.append("-O")
                    command.append(url)

                try:
                    run(command=command)
                    
                    directory_name: str = "mangas/'" + temp[MANGA_NAME_INDEX] + "'/" + temp[MANGA_CHAPTER_INDEX]
                    image_extension: str = temp[FILE_EXTENSION_INDEX][-4:]

                    moveFiles(
                        file_extension=image_extension, 
                        directory_name=directory_name
                    )

                    print("Capítulo do mangá baixado com sucesso!")
                except:
                    print("Erro ao tentar baixar as imagens!")
                    exit()
        else:
            print("Este capítulo não possui páginas para serem baixadas!")