def isMangaLink(url: str) -> bool:
    """ Verifica se a URL informada é de um mangá ou não.

    Parameters
    ----------
    url: :class:`str`
        URL que deseja verificar.

    Returns
    -------
    :class:`bool`
    """

    if(url.find("manga") != -1):
        return True

    return False