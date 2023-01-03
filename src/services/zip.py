from command import run

# ------------------------------ Constants ----------------------------------- #
DIRECTORY_NAME = "mangas"
# ---------------------------------------------------------------------------- #

def zip() -> bool:
    try:
        run(command=["zip", "-q", "-r", DIRECTORY_NAME + ".zip", DIRECTORY_NAME])

        return True
    except:
        print("Erro ao tentar comprimir os arquivos em .zip!")
        
        return False