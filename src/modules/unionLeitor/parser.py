from typing import List

def idValidUrl(url: str) -> bool:
    """ Verifica se a URL passada é de uma página do site `unionleitor.top/`.

    Parameters
    ----------
    url: :class:`str`
        URL que deseja verificar.

    Returns
    -------
    :class:`bool`
    """

    valid_urls: List[str] = ["unionleitor.top"]

    for valid_url in valid_urls:
        if(url.find(valid_url) != -1):
            return True

    return False

def isValidImage(url: str) -> bool:
    """ Verifica se a URL passada é de uma imagem ou não.
    Obs: Tipos aceitos: .avif, .gif, .jpg, .jpeg, .png, .svg

    Parameters
    ----------
    url: :class:`str`
        URL que deseja verificar.

    Returns
    -------
    :class:`bool`
    """
    
    image_extensions: List[str] = [".avif", ".gif", ".jpg", ".jpeg", ".png", ".svg"]

    for image_extension in image_extensions:
        if(url.find(image_extension) != -1):
            return True

    return False

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

def isNotBanner(url: str) -> bool:
    """ Verifica se a imagem é um banner.

    Parameters
    ----------
    url: :class:`str`
        URL que deseja verificar.

    Returns
    -------
    :class:`bool`
    """

    if(url.find("banner") != -1):
        return False

    return True