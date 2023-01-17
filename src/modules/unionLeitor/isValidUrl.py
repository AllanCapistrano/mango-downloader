from typing import List

def isValidUrl(url: str) -> bool:
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