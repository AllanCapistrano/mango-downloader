from command import run

# ------------------------------ Constants ----------------------------------- #
DIRECTORY_NAME = "mangas"
# ---------------------------------------------------------------------------- #

def zip() -> str:
    """ Realiza a compressão de arquivos utilizando o zip.

    Returns
    -------
    :class:`str`
        Nome do arquivo .zip gerado.
        Caso não seja possível realizar a compressão, será retornado 
        :class:`None`.
    """
    
    try:
        run(command=["zip", "-q", "-r", DIRECTORY_NAME + ".zip", DIRECTORY_NAME])

        return DIRECTORY_NAME + ".zip"
    except:
        print("Erro ao tentar comprimir os arquivos em .zip!")
        
        return None