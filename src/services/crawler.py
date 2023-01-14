from typing import List

import requests
from bs4 import BeautifulSoup

from modules import parser

class Crawler:
    def __reqUrl__(self, url: str) -> BeautifulSoup:
        """ Requisita uma determinada URL e retorna no tipo aceito pela 
        biblioteca `BeautifulSoup`.

        Parameters
        -----------
        url: :class:`str`
            Url do site.

        Returns
        -----------
        soup: :class:`BeautifulSoup`
        """

        req = requests.get(url)

        return BeautifulSoup(req.text, 'lxml')

    def getMangaImageUrls(self, url: str) -> List[str]:
        """ Obtém as URLs das imagens das páginas de um capítulo de um mangá
        no formato de uma lista de `strings`.

        Parameters
        -----------
        url: :class:`str`
            Url do capítulo do mangá

        Returns
        -------
        imagesUrl :class:`List[str]`
        """

        imagesUrl: List[str] = []
        
        for image in self.__reqUrl__(url).find_all("img", class_="img-manga"):
            if(
                image.attrs["src"] != None and 
                parser.isValidMangaImage(image.attrs["src"]) and
                parser.isValidImage(image.attrs["src"]) and
                parser.isNotBanner(image.attrs["src"])
            ):
                imagesUrl.append(image.attrs["src"])
                
        
        return imagesUrl

    def getChaptersUrls(self, url: str) -> List[str]:
        """ Obtém todas as URLs dos capítulos de um mangá.

        Parameters
        -----------
        url: :class:`str`
            Url do mangá.

        Returns
        -------
        :class:`List[str]`
        """

        chapter_links: List[str] = []

        for chapters in self.__reqUrl__(url).find_all("div", class_="capitulos"):
            chapter = chapters.find("a")

            chapter_links.append(chapter.attrs["href"])

        return chapter_links

    def getAllMangaNames(self, url: str) -> List[str]:
        """ Obtém o nome de todos os mangás listados na página.

        Parameters
        -----------
        url: :class:`str`
            Url da página de lista de mangás.

        Returns
        -------
        :class:`List[str]`
        """

        mangaNames: List[str] = []

        for manga in self.__reqUrl__(url).find_all("div", class_="lista-mangas-novos"):
            mangaNames.append(manga.find("b").contents[0])

        return mangaNames
