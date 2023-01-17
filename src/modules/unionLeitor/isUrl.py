from typing import List

def isUrl(url: str) -> bool:
    """ Verifica se o que foi passado é uma URL ou não.

    Parameters
    ----------
    url: :class:`str`
        URL que deseja verificar.

    Returns
    -------
    :class:`bool`
    """

    valid_urls: List[str] = ["https://", "http://"]

    for valid_url in valid_urls:
        if(url.find(valid_url) != -1):
            return True

    return False