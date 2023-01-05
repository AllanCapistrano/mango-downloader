from typing import List

import requests
from bs4 import BeautifulSoup

from ..modules.unionLeitor import parser

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