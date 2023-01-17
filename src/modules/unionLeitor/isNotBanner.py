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