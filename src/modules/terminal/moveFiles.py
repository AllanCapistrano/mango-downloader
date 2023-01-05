from os import system

def moveFiles(file_extension: str, directory_name: str) -> bool:
        """ Move todos os arquivos de uma determinada extensão, para o diretório
        especificado.

        Parameters
        ----------
        file_extension: :class:`str`
            Extensão do arquivo.
        directory_name: :class:`str`
            Nome do diretório juntamente com o caminho.

        """
        
        file_extension: str = "*" + file_extension

        try:
            system("mv " + file_extension + " " + directory_name)

            return True
        except:
            return False