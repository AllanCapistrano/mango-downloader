from typing import List
from os import getenv
from dotenv import load_dotenv

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

load_dotenv()

# ------------------------------ Constants ----------------------------------- #
GOOGLE_DRIVE_LINK = getenv("GOOGLE_DRIVE_LINK")
FOLDER_ID = getenv("FOLDER_ID")
# ---------------------------------------------------------------------------- #

class Uploader:
    def __init__(self) -> None:
        """ Método construtor.
        """
        
        self.gauth = GoogleAuth()           
        self.drive = GoogleDrive(self.gauth)

    def upload(self, files: List[str]) -> bool:
        """ Realiza o upload dos arquivos para o Google Drive.

        Parameters
        ----------
        files: :class:`List[str]`
            Lista contendo o nome dos arquivos que se deseja fazer o upload
            para o Google Drive.

        Returns
        -------
        :class:`bool`
        """

        if(len(files) > 0):
            try:
                for upload_file in files:
                    gfile = self.drive.CreateFile({'parents': [{'id': FOLDER_ID}]})
                    
                    # Read file and set it as the content of this instance.
                    gfile.SetContentFile(upload_file)
                    gfile.Upload() # Upload the file.
                
                print("Os capítulos baixados já estão disponíveis no Google Drive!")
                print(GOOGLE_DRIVE_LINK)

                return True
            except Exception as e:
                print("Não foi possível realizar o upload do(s) arquivo(s)!")
                print(e)
                
                return False