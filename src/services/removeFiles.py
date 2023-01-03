from command import run

# ------------------------------ Constants ----------------------------------- #
DIRECTORY_NAME = "mangas"
# ---------------------------------------------------------------------------- #

def removeFilesAndDirectories() -> bool:
    try:
        run(command=["rm", "-rf", DIRECTORY_NAME, DIRECTORY_NAME + ".zip"])

        return True
    except:
        print("Erro ao tentar remover os arquivos " + DIRECTORY_NAME + "e " + DIRECTORY_NAME + ".zip!")

        return False