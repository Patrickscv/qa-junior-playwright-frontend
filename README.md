
1. Configurando váriaveis de ambiente:

O arquivo ".env.exemplo" já vai com as váriaveis de ambiente padrões do SauceDemo, só é necessário alterar o nove de ".env.exemplo" para ".env".

2. Como realizar a instalação:
   
Em seu terminal, navegue até a pasta do projeto:

cd qa-junior-playwright-frontend

Crie um ambiente virtual:

python -m venv venv

Ative o ambiente virtual:

PowerShell: .\venv\Scripts\Activate.ps1

No Linux e Mac: source venv/bin/activate

Instale as dependências:

Retorne para a pasta principal onde está o requirements.txt
cd ..

pip install -r requirements.txt

3. Execução dos Testes

Na pasta do projeto (cd qa-junior-playwright-frontend)

Execute o comando "pytest" para rodar sem interface gráfica:

pytest

Para ver o navegador abrir e as ações sendo executadas:

pytest --headed

Para ver os logs de cada teste utilize o comando:

pytest --log-cli-level=INFO

