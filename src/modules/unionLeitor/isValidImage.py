from typing import List

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