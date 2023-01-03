from command import run

# ------------------------------ Constants ----------------------------------- #
DIRECTORY_NAME = "mangas"
# ---------------------------------------------------------------------------- #

def zip() -> None:
    run(command=["zip", "-q", "-r", DIRECTORY_NAME + ".zip", DIRECTORY_NAME])