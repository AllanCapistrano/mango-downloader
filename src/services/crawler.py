from typing import List, Dict
from re import sub

import requests
from bs4 import BeautifulSoup

from modules import isValidImage, isValidMangaImage, isNotBanner

class Crawler:
    def __reqUrl__(self, url: str) -> BeautifulSoup:
        """ Requisita uma determinada URL e retorna no tipo aceito pela 
        biblioteca `BeautifulSoup`.

        Parameters
        -----------
        url: :class:`str`
            URL do site.

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
            URL do capítulo do mangá

        Returns
        -------
        imagesUrl :class:`List[str]`
        """

        imagesUrl: List[str] = []
        
        for image in self.__reqUrl__(url).find_all("img", class_="img-manga"):
            if(
                image.attrs["src"] != None and 
                isValidMangaImage(image.attrs["src"]) and
                isValidImage(image.attrs["src"]) and
                isNotBanner(image.attrs["src"])
            ):
                imagesUrl.append(image.attrs["src"])
                
        
        return imagesUrl

    def getChaptersUrls(self, url: str) -> List[str]:
        """ Obtém as URLs de todos os capítulos de um mangá.

        Parameters
        -----------
        url: :class:`str`
            URL do mangá.

        Returns
        -------
        :class:`List[str]`
        """

        chapter_links: List[str] = []

        for chapters in self.__reqUrl__(url).find_all("div", class_="capitulos"):
            chapter = chapters.find("a")

            chapter_links.append(chapter.attrs["href"])

        return chapter_links

    def getChaptersNamesAndUrls(self, url: str) -> List[Dict[str, str]]:
        """ Obtém os nomes e as URLs de todos os capítulos de um mangá.

        Parameters
        -----------
        url: :class:`str`
            URL do mangá.

        Returns
        -------
        :class:`List[Dict[str, str]]`
        """

        chapter_info: List[Dict[str, str]] = []

        for chapters in self.__reqUrl__(url).find_all("div", class_="capitulos"):
            chapter = chapters.find("a")

            chapter_name: str = chapter.contents[0]
            chapter_link:str = chapter.attrs["href"]

            chapter_info.append({
                "chapter_name": chapter_name,
                "chapter_link": chapter_link
            })

        return chapter_info

    def getAllMangaNames(self, url: str) -> List[str]:
        """ Obtém o nome de todos os mangás listados na página.

        Parameters
        -----------
        url: :class:`str`
            URL da página de lista de mangás.

        Returns
        -------
        :class:`List[str]`
        """

        manga_names: List[str] = []

        for manga in self.__reqUrl__(url).find_all("div", class_="lista-mangas-novos"):
            manga_names.append(manga.find("b").contents[0])

        return manga_names

    def getAllMangaUrls(self, url: str) -> List[str]:
        """ Obtém a URL de todos os mangás listados na página.

        Parameters
        -----------
        url: :class:`str`
            URL da página de lista de mangás.

        Returns
        -------
        :class:`List[str]`
        """

        manga_urls: List[str] = []

        for manga in self.__reqUrl__(url).find_all("div", class_="lista-mangas-novos"):
            manga_urls.append(manga.find("a").attrs["href"])

        return manga_urls

    def getAllMangaNamesAndUrls(self, url: str) -> List[Dict[str, str]]:
        """ Obtém o nome e a URL de todos os mangás listados na página.

        Parameters
        -----------
        url: :class:`str`
            URL da página de lista de mangás.

        Returns
        -------
        :class:`List[Dict[str, str]]`
        """

        manga_info: List[Dict[str, str]] = []

        for manga in self.__reqUrl__(url).find_all("div", class_="lista-mangas-novos"):
            manga_name: str = manga.find("b").contents[0]
            manga_url: str = manga.find("a").attrs["href"]

            manga_info.append({
                "manga_name": manga_name,
                "manga_url": manga_url
            })

        return manga_info

    def getLastPageNumberMangaList(self, url: str) -> int:
        """ Obtém o número da última página da lista de mangás.

        Parameters
        -----------
        url: :class:`str`
            URL da primeira página da lista de mangás.

        Returns
        -------
        :class:`int`
        """

        pagination = self.__reqUrl__(url).find("ul", class_="pagination")
        last_manga_list_page: str = pagination.find_all("li")[-1].find("a").attrs["href"]

        return int(sub(r"\D", "", last_manga_list_page))