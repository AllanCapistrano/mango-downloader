from os.path import dirname, join
from re import sub

def getMangaListPage(manga_name: str) -> str:
    """ Retorna a página da lista de mangás que contém o mangá desejado,

    Parameters
    ----------
    manga_name: :class:`str`
        Nome do mangá que deseja saber a página

    Returns
    -------
    :class:`str`
        URL da página da lista de mangás.
    """

    manga_name: str = manga_name.lower()

    current_path: str = dirname(__file__)
    file_path: str = join(current_path, "../../lists/mangas.list")

    # Verificando se o primeiro caractere do nome do mangá é uma letra ou não.
    if(sub(r"[aA-zZ\-\s]", "", manga_name[:1]) != ""):
        # Se não for uma letra entra, retorna a primeira URL presente no arquivo.
        with open(file_path, "r") as file:
            return file.readline()

    # Caso seja uma letra, procura a URL correspondente no arquivo.
    with open(file_path, "r") as file:
        while True:
            line = file.readline()

            if not line:
                return None

            # Caso o primeiro caractere do nome do mangá seja igual ao último
            # da URL presente no arquivo.
            if(manga_name[:1] == line.strip()[-1:]):
                return line.strip()