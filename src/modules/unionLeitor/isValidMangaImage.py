from typing import List

def isValidMangaImage(url: str) -> bool:
    """ Verifica se a URL passada é de uma página contendo a imagem de uma 
    página de mangá do site `unionleitor.top/`.

    Parameters
    ----------
    url: :class:`str`
        URL que deseja verificar.

    Returns
    -------
    :class:`bool`
    """

    validations: List[str] = ["umangas.club", "unionleitor.top", "leitor", "mangas"]
    counter: int = 0
    
    for validation in validations:
        if(url.find(validation) != -1):
            counter += 1

    return counter >= 2