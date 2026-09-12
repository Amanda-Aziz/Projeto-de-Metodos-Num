<h1>Métodos Numéricos — Determinação da Altura de uma Coluna de Água</h1>

<p align="center">
  <img src="http://img.shields.io/static/v1?label=Python&message=3.x&color=3776AB&style=for-the-badge&logo=python"/>
  <img src="http://img.shields.io/static/v1?label=Jupyter&message=Notebook&color=F37626&style=for-the-badge&logo=jupyter"/>
  <img src="http://img.shields.io/static/v1?label=Git&message=2.x&color=f05032&style=for-the-badge&logo=git"/>
  <img src="http://img.shields.io/static/v1?label=GitHub&message=2026&color=181717&style=for-the-badge&logo=github"/>
  <img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=yellow&style=for-the-badge"/>
</p>

> Status do Projeto: :heavy_check_mark: (concluído) | :warning: (em desenvolvimento) | :x: (não iniciado)

---

# Tópicos

:small_blue_diamond: [Contexto](#contexto-information_source)  

:small_blue_diamond: [Problema](#problema-writing_hand)  

:small_blue_diamond: [Objetivo](#objetivo-dart)  

:small_blue_diamond: [Métodos Numéricos](#métodos-numéricos-chart_with_upwards_trend)  

:small_blue_diamond: [Estrutura do Projeto](#estrutura-do-projeto-file_folder)  

:small_blue_diamond: [Pré-requisitos](#pré-requisitos-warning)  

:small_blue_diamond: [Instalação](#instalação-rocket)  

:small_blue_diamond: [Como Rodar o Projeto](#como-rodar-o-projeto-computer)  

:small_blue_diamond: [Tecnologias Utilizadas](#tecnologias-utilizadas-wrench)  

:small_blue_diamond: [Documentação](#documentação-book)  

:small_blue_diamond: [Desenvolvedores](#desenvolvedores-octocat)  

---

# Contexto :information_source:

<p align="justify">
O projeto foi desenvolvido para a disciplina de <strong>Métodos Numéricos</strong>, do curso de <strong>Ciência da Computação da Universidade Católica de Pernambuco (UNICAP)</strong>. O trabalho utiliza métodos numéricos para resolver uma equação não linear associada a um problema de escoamento de água.
</p>

<p align="justify">
Os métodos de determinação de raízes deverão ser implementados pelo próprio grupo em um pacote Python, sem utilização de funções prontas para encontrar raízes. Um Jupyter Notebook deverá importar as funções do pacote e utilizá-las na resolução e análise do problema.
</p>

---

# Problema :writing_hand:

<p align="justify">
O problema consiste em determinar a altura inicial <strong>H</strong> de uma coluna de água necessária para que a velocidade de escoamento através de um tubo alcance <strong>5 m/s</strong> após <strong>2,5 s</strong>.
</p>

O modelo é dado por:

```text
v = √(2gH) · tanh((√(2gH) / 2L) · t)
```

Para o problema:

- **g = 9,81 m/s²**
- **L = 4 m**
- **t = 2,5 s**
- **v = 5 m/s**

A equação utilizada na determinação da raiz é:

```text
f(H) = √(19,62H) · tanh((2,5√(19,62H)) / 8) - 5
```

---

# Objetivo :dart:

<p align="justify">
O objetivo do trabalho é determinar numericamente a altura inicial da coluna de água que satisfaz o modelo proposto, aplicando diferentes métodos de determinação de raízes e comparando os resultados obtidos.
</p>

<p align="justify">
Além da obtenção da solução, o trabalho estabelece e justifica critérios de parada, precisão numérica, intervalo inicial e condições de convergência. Os métodos são aplicados à mesma função para permitir uma comparação coerente entre número de iterações, aproximação encontrada, erro e resíduo.
</p>

---

# Métodos Numéricos :chart_with_upwards_trend:

### Métodos utilizados no projeto

- Método do Ponto Fixo (Iteração Linear)
- Método da Bisseção
- Método da Falsa Posição
- Método de Newton-Raphson
- Método da Secante

> As implementações dos métodos ficam no pacote Python. O Jupyter Notebook apenas importa essas funções e as utiliza para resolver o problema.

---

# Estrutura do Projeto :file_folder:

```text
Projeto-de-Metodos-Num/
│
├── notebooks/
│   └── aplicacao_analise_comparativa_metodos_numericos.ipynb
│
├── src/
│   └── metodos_numericos/
│       ├── __init__.py
│       ├── ponto_fixo.py
│       ├── bissecao.py
│       ├── falsa_posicao.py
│       ├── newton_raphson.py
│       └── secante.py
│
├── pyproject.toml
├── .gitignore
└── README.md
```

---

# Pré-requisitos :warning:

Antes de clonar o repositório e executar o projeto, é necessário ter instalado:

**1. Python 3.x:**
  - Caso não tenha Python, instale: https://www.python.org/downloads/

**2. Git:**
  - Caso não tenha Git, instale: https://git-scm.com/install/

**3. VS Code (ou outra IDE com suporte a Jupyter Notebook):**
  - Caso não tenha VS Code, instale: https://code.visualstudio.com/download

---

# Instalação :rocket:

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/Amanda-Aziz/Projeto-de-Metodos-Num.git
```

---

### 2️⃣ Entrar na pasta do projeto

```bash
cd Projeto-de-Metodos-Num
```

---

### 3️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

---

### 4️⃣ Ativar ambiente virtual

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

---

### 5️⃣ Instalar o projeto e as dependências

Com o ambiente virtual ativado:

```bash
python -m pip install --upgrade pip
pip install -e .
```

O comando `pip install -e .` utiliza o arquivo `pyproject.toml` para instalar o pacote desenvolvido pelo grupo e todas as dependências necessárias ao projeto. 

---

# Como Rodar o Projeto :computer:

Com o ambiente virtual ativado e o pacote instalado, execute:

```bash
jupyter notebook
```

Depois, abra:

```text
notebooks/aplicacao_analise_comparativa_metodos_numericos.ipynb
```

O notebook utiliza as funções implementadas no pacote localizado em:

```text
src/metodos_numericos/
```

As implementações dos métodos numéricos não deverão estar dentro do notebook.

---

# Tecnologias Utilizadas :wrench:

- **Python**
- **Jupyter Notebook**
- **NumPy**
- **Pandas**
- **Matplotlib**
- **pip**
- **Git**
- **GitHub**

> O módulo **Math** pertence à biblioteca padrão do Python e, portanto, não precisa ser instalado como dependência externa.

---

# Documentação :book:

A formulação matemática, a aplicação dos métodos e a análise dos resultados estão disponíveis no notebook do projeto:

- [Aplicação e Análise Comparativa de Métodos Numéricos](notebooks/aplicacao_analise_comparativa_metodos_numericos.ipynb)

O notebook apresenta:

- Formulação matemática do problema
- Transformação para `f(H) = 0`
- Domínio e continuidade
- Escolha do intervalo inicial
- Verificação da unicidade da solução
- Critérios de parada
- Escolha da tolerância
- Aplicação dos métodos numéricos
- Comparação dos resultados
- Referências bibliográficas

---

# Desenvolvedores :octocat:

Time responsável pelo desenvolvimento do projeto.

| [<img src="https://github.com/Alexandre-MCS.png" width="115"><br><sub>Alexandre</sub>](https://github.com/Alexandre-MCS) | [<img src="https://github.com/Amanda-Aziz.png" width="115"><br><sub>Amanda Aziz</sub>](https://github.com/Amanda-Aziz) | [<img src="https://github.com/francisLauriano.png" width="115"><br><sub>Francis Lauriano</sub>](https://github.com/francisLauriano) | [<img src="https://github.com/lucascoffeedark.png" width="115"><br><sub>Lucas</sub>](https://github.com/lucascoffeedark) | [<img src="https://github.com/Sofiafs.png" width="115"><br><sub>Sofia Farias</sub>](https://github.com/Sofiafs) |
| :---: | :---: | :---: | :---: | :---: |

---
