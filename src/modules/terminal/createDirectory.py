from command import run

def createDirectory(directory_name: str) -> bool:
        """ Cria um diretório a partir do caminho especificado.
        
        Parameters
        ----------
        directory_name: :class:`str`
            Nome do diretório juntamente com o caminho.
        """
        
        try:
            run(command=["mkdir", "-p", directory_name])

            return True
        except:
            print("Erro ao criar o diretório: " + directory_name)

            return False