# Projeto de Automação Frontend com Playwright & Python

Este repositório contém um framework de automação de testes End-to-End (E2E) desenvolvido em **Python** utilizando a biblioteca **Playwright** para o site **SauceDemo**.

---

### Pré-requisitos

Certifique-se de que você tem o **Python 3** e o **pip** instalados em sua máquina.

### 1. Configuração do Projeto e Instalação

Siga os passos abaixo para preparar o ambiente de execução:

#### **Passo 1: Variáveis de Ambiente**

1.  Localize o arquivo `.env.exemplo` na raiz do projeto.
2.  **Renomeie** o arquivo para `.env`.
    * > **Observação:** Este arquivo já contém as variáveis de ambiente padrão para o SauceDemo, mas pode ser editado para customizações futuras.

#### **Passo 2: Clonar e Navegar**

1.  Clone o repositório para sua máquina.
2.  Navegue até a pasta principal do projeto no seu terminal:
    ```bash
    cd SauceDemo_2E2_Automation-main
    ```

#### **Passo 3: Configurar o Ambiente Virtual**

1.  Crie o ambiente virtual (venv):
    ```bash
    python -m venv venv
    ```
2.  Ative o ambiente virtual:
    * **Windows (PowerShell):**
        ```bash
        .\venv\Scripts\Activate.ps1
        ```
    * **Linux e macOS:**
        ```bash
        source venv/bin/activate
        ```

#### **Passo 4: Instalar Dependências**

1.  Instale todas as bibliotecas Python listadas no `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
2.  Instale os *browsers* necessários para o Playwright:
    ```bash
    playwright install
    ```

---

### 2. Execução dos Testes

Certifique-se de que você está na pasta do projeto (`SauceDemo_2E2_Automation-main`) e com o ambiente virtual ativado.

Utilize o `pytest` para executar os testes com as seguintes opções:

| Comando | Descrição |
| :--- | :--- |
| `pytest` | Executa todos os testes em **modo *headless*** (sem interface gráfica). |
| `pytest --headed` | Executa os testes abrindo o navegador (modo *headed*), permitindo que você **veja as ações** serem executadas. |
| `pytest --log-cli-level=INFO` | Executa os testes e exibe os **logs** detalhados no terminal durante a execução. |

---

### 3. Estrutura do Projeto

* `tests/`: Contém os arquivos de teste (ex: `test_login.py`).
* `pages/`: Contém o Page Object Model (POM) dos elementos da aplicação (se aplicável).
* `requirements.txt`: Lista de dependências do Python.
* `.env`: Variáveis de ambiente utilizadas no projeto.
