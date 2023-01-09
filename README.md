# mango-downloader
Baixa capítulos de mangás e os salva no Google Drive.

## 🖥️ Como utilizar
<details>
<summary><h2>Configurando o Google Drive</h2></summary>

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

</details>

<details>
<summary><h2>Executando o projeto</h2></summary>

1. O projeto executa comandos diretamente no [Sistema Operacional](https://en.wikipedia.org/wiki/Operating_system), desa forma, o mesmo possui a depedência operacional **zip**, então antes de executá-lo, é necessário garantir que a mesma já está instalada, caso não esteja, busque qual o comando para instar na sua distribuição Linux. Alguns exemplos:
   ```powershell
   # Debian-based
   sudo apt install zip
   ```
   ```powershell
   # Redhat 
   sudo dnf install zip
   ```
   ```powershell
   # Arch-based 
   sudo pacman -S zip
   ```
   ```powershell
   # OpenSUSE
   sudo zypper install zip
   ```
2. Faça o download das dependências do projeto:
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
7. Após isso, com um terminal aberto no diretório do projeto, basta executar o comando<sup>4</sup>:
   ```powershell
   python src/main.py
   ```

###### Obs<sup>3</sup>: Caso não tenha copiado, acesse a [Google Cloud Plataform](https://console.cloud.google.com), na aba de **Credenciais** do projeto, em **IDs do cliente OAuth 2.0**, clique em **Editar cliente OAuth**, e então copie o **ID do cliente** e a **Chave secreta do cliente**. ######
###### Obs<sup>4</sup>: Somente na primeira vez que executar o programa, será necessário se autenticar utilizando uma conta Google, deve ser a mesma em que foi criada a pasta no passo **1** - [Configurando o Google Drive](#configurando-o-google-drive) e a mesma definida no passo **15** - [Configurando o Google Drive](#configurando-o-google-drive). ######

</details>
