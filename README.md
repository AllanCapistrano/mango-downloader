# mango-downloader

## 📖 Descrição ##
> **O programa se trata de um programa escrito em [Python](https://www.python.org/) para baixa capítulos de mangás e disponibilizá-los na plataforma [Google Drive](https://drive.google.com/drive/my-drive).**
> 
> Para isso é informado a URL do capitúlo do mangá (consutar as [plataformas suportadas](#-plataformas-suportadas)), é feito o download das imagens, os arquivos então são comprimidos utilizando `.zip`, e fica disponível em uma pasta do [Google Drive](https://drive.google.com/drive/my-drive) configurada pelo usuário.
>
> O nome **mango-downloader** é uma brincadeira juntando a palavra *"mango"*, que traduzindo do idioma Inglês, significa a fruta "manga", pois essa palavra em português é bem próxima da palavra "mangá"; e *"downloader"* que estaria realacioda com a palavra *"download"* do idioma Inglês, que significa "baixar".
>
> Qualquer dúvida, sugestão, *bugs* ou erros são bem-vindos, para isso, utilize a aba de [Issues](https://github.com/AllanCapistrano/mango-downloader/issues) com a [*label*](https://github.com/AllanCapistrano/mango-downloader/labels) correta.

## 🌐 Plataformas suportadas
- [x] [Union Mangás](https://unionleitor.top/home)

## 🖥️ Como utilizar
<h2>Configurando o Google Drive</h2>

1. Crie uma pasta no [Google Drive](https://drive.google.com/drive/my-drive) para onde serão feitos os uploads dos arquivos;
2. Entre na [Google Cloud Plataform](https://console.cloud.google.com) e clique em **Criar Projeto**;
3. Digite o nome do projeto e depois clique em **Criar**;
4. Clique no menu lateral esquerdo, e depois selecione a opção **APIs e serviços**;
5. No menu lateral esquerdo, clique em **Biblioteca**;
6. Na caixa de pesquisa, procure por **Google Drive**;
7. Clique no resultado **Google Drive API**, e clique em **Ativar**;
8. No menu lateral esquerdo, clique em **Credenciais**;
9. Clique em **Criar Credenciais** no topo da página, e em **ID doCliente OAuth**;
10. Clique no botão **Configurar Tela de Consentimento**;
11. Em **User Type**<sup>1</sup> selecione **Externo**, e clique em **Criar**;
12. Em **Informações do app**, digite<sup>2</sup> o **Nome do app** e selecione um **E-mail para suporte do usuário**;
13. Em **Dados de contato do desenvolvedor**, digite **Endereços de e-mail** para o contato, e depois clique em **Salvar e continar**;
14. Em **Escopos** clique em **Salvar e continar**;
15. Em **Usuários de teste**, adicione a conta Google que deseja fazer upload dos arquivos (a mesma em que foi criada a pasta no passo **1** - [Configurando o Google Drive](#configurando-o-google-drive)), e clique em **Salvar e continar**;
16. Em **Resumo** clique em **Voltar para o Painel**;
17. Repita os passos **7** e **8**;
18. Mas agora, selecione **App para computador**, digite o **Nome**, e clique em **Criar**;
19. Copie o **ID de cliente** e ** Chave secreta de cliente**, clique em **Fazer download do JSON** e logo depois clique no botaõ **OK**;
20. Faça um Fork deste repositório (caso queira modificá-lo) ou somente clone-o;
21. Coloque o arquivo contendo as credenciais (`.json`) na pasta do projeto;
22. Renomei o arquivo contendo as credenciais (`.json`) para `client_secrets.json`.


###### Obs<sup>1</sup>: Caso seja um usuário do Google Workspace, poderá utilizar a opção **Interno** caso deseje. ######
###### Obs<sup>2</sup>: Caso queira poderá preencher os demais campos não obrigatórios também. ######

<h2>Executando o programa</h2>

1. O programa executa comandos diretamente no [Sistema Operacional](https://en.wikipedia.org/wiki/Operating_system), desa forma, o mesmo possui as depedências operacionais **zip** e [**curl**](https://curl.se/download.html), então antes de executá-lo, é necessário garantir que as mesmas já estão instaladas, caso não estejam, busque qual o comando para instalá-las na sua distribuição Linux. Alguns exemplos:
   ```powershell
   # Debian-based
   sudo apt install zip
   
   sudo apt install curl
   ```
   ```powershell
   # Redhat 
   sudo dnf install zip
   
   sudo dnf install curl
   ```
   ```powershell
   # Arch-based 
   sudo pacman -S zip
   
   sudo pacman -S curl
   ```
   ```powershell
   # OpenSUSE
   sudo zypper install zip
   
   sudo zypper install curl
   ```
2. Faça o download das dependências do programa:
   ```powershell
   pip install -r requirements.txt
   ```
   ou
   ```powershell
   pip3 install -r requirements.txt
   ```
3. Faça uma cópia do arquivo `.env.example` com o nome de `.env`, ou altere o nome do arquivo `.env.example` para `.env`:
   ```powershell
   cp .env.example .env
   ```
   ou
   ```powershell
   mv .env.example .env
   ```
4. Faça uma cópia do arquivo `settings.example.yaml` com o nome de `settings.yaml`, ou altere o nome do arquivo `settings.example.yaml` para `settings.yaml`:
   ```powershell
   cp settings.example.yaml settings.yaml
   ```
   ou
   ```powershell
   mv settings.example.yaml settings.yaml
   ```
5. Abra o arquivo `.env` e preencha os campos:
   1. [Opcional] `GOOGLE_DRIVE_LINK` link para acessar a pasta em que será feito o upload dos arquivos (passo **1** - [Configurando o Google Drive](#configurando-o-google-drive))
   2. `FOLDER_ID` ID da pasta em que será feito o upload dos arquivos (passo **1** - [Configurando o Google Drive](#configurando-o-google-drive)), por exemplo no link "https://drive.google.com/drive/folders/id_da_pasta"
6. Abra o arquivo `settings.yaml` e preencha os campos `client_id` e `client_secret`, com o que foi copiado<sup>3</sup> no passo **19** - [Configurando o Google Drive](#configurando-o-google-drive);
7. Após isso, com um terminal aberto no diretório do programa, basta executar o comando<sup>4</sup>:
   ```powershell
   python src/main.py
   ```

###### Obs<sup>3</sup>: Caso não tenha copiado, acesse a [Google Cloud Plataform](https://console.cloud.google.com), na aba de **Credenciais** do projeto, em **IDs do cliente OAuth 2.0**, clique em **Editar cliente OAuth**, e então copie o **ID do cliente** e a **Chave secreta do cliente**. ######
###### Obs<sup>4</sup>: Somente na primeira vez que executar o programa, será necessário se autenticar utilizando uma conta Google, deve ser a mesma em que foi criada a pasta no passo **1** - [Configurando o Google Drive](#configurando-o-google-drive) e a mesma definida no passo **15** - [Configurando o Google Drive](#configurando-o-google-drive). ######

## 👨‍💻 Autor ##

| [![Allan Capistrano](https://github.com/AllanCapistrano.png?size=100)](https://github.com/AllanCapistrano) |
| -----------------------------------------------------------------------------------------------------------|
| [Allan Capistrano](https://github.com/AllanCapistrano)                                                     |

<p>
    <h3>Onde me encontrar:</h3>
    <a href="https://github.com/AllanCapistrano">
        <img src="https://github.com/AllanCapistrano/AllanCapistrano/blob/master/assets/github-square-brands.png" alt="Github icon" width="5%">
    </a>
    &nbsp
    <a href="https://www.linkedin.com/in/allancapistrano/">
        <img src="https://github.com/AllanCapistrano/AllanCapistrano/blob/master/assets/linkedin-brands.png" alt="Linkedin icon" width="5%">
    </a> 
    &nbsp
    <a href="https://mail.google.com/mail/u/0/?view=cm&fs=1&tf=1&source=mailto&to=asantos@ecomp.uefs.br">
        <img src="https://github.com/AllanCapistrano/AllanCapistrano/blob/master/assets/envelope-square-solid.png" alt="Email icon" width="5%">
    </a>
</p>

## 🙏 Apoie ##

**Por favor ⭐️ este repositório caso este projeto seja útil e/ou tenha lhe ajudado.**

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/allancapistrano)

## ⚖️ Licença ##
[GPL-3.0 License](./LICENSE)
