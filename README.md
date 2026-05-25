# 🧠 Porquinho ML API

Microsserviço responsável pela categorização automática de transações utilizando Machine Learning para o ecossistema Porquinho.

<p align="center">
  <img src="https://img.shields.io/badge/python-3.13-blue.svg" />
  <img src="https://img.shields.io/badge/fastapi-0.115-green.svg" />
  <img src="https://img.shields.io/badge/scikit--learn-ML-orange.svg" />
  <img src="https://img.shields.io/badge/status-development-yellow.svg" />
</p>

---

# 📌 Sobre

O Porquinho ML API é um microsserviço de machine learning projetado para classificar automaticamente transações financeiras em categorias como:

- ALIMENTACAO
- TRANSPORTE
- EDUCACAO
- ENTRETENIMENTO
- SAUDE
- ASSINATURAS
- CASA
- PETS
- BELEZA
- VIAGEM

O serviço é consumido pela API principal desenvolvida em Spring Boot.

---

# 🏗️ Arquitetura

```text
Frontend React
      ↓
API Spring Boot
      ↓
Porquinho ML API
      ↓
Modelo de Machine Learning Treinado
```

---

# ⚙️ Tecnologias

- Python 3.13
- FastAPI
- Scikit-learn
- Pandas
- Joblib
- Uvicorn

---

# 📂 Estrutura do Projeto

```text
porquinho-ml-api/
│
├── .venv/
├── app.py
├── training.py
├── transactions.csv
├── model_category.pkl
├── requirements.txt
└── README.md
```

---

# 🚀 Executando Localmente

## 1. Clonar repositório

```bash
git clone https://github.com/enzorva/porquinho-ml-api.git
```

---

## 2. Criar ambiente virtual

```bash
python -m venv .venv
```

---

## 3. Ativar ambiente virtual

### Windows

```bash
.venv\Scripts\activate
```

### Linux / MacOS

```bash
source .venv/bin/activate
```

---

## 4. Instalar dependências

```bash
pip install -r requirements.txt
```

---

# 🧠 Treinando o Modelo

Para treinar o modelo de categorização de transações:

```bash
python training.py
```

Esse comando gera:

```text
model_category.pkl
```

---

# ▶️ Executando a API

```bash
uvicorn app:app --reload
```

O servidor ficará disponível em:

```text
http://localhost:8000
```

---

# 📘 Documentação Swagger

O FastAPI gera automaticamente a documentação Swagger:

```text
http://localhost:8000/docs
```

---

# 🔍 Exemplo de Requisição

## Endpoint

```http
POST /predict
```

## Corpo da Requisição

```json
{
  "description": "ifood pedido hamburguer"
}
```

## Resposta

```json
{
  "category": "ALIMENTACAO"
}
```

---

# 🤖 Pipeline de Machine Learning

O pipeline atual de ML utiliza:

- CountVectorizer
- Multinomial Naive Bayes

Fluxo do pipeline:

```text
Descrição da Transação
        ↓
Vetorização do Texto
        ↓
Classificação por ML
        ↓
Categoria Prevista
```

---

# 📈 Melhorias Futuras

- Score de confiança
- Suporte multilíngue
- Categorização personalizada por usuário
- Treinamento contínuo
- Detecção de anomalias financeiras
- Geração de insights financeiros

---

# 👨‍💻 Equipe

Desenvolvido como parte do projeto acadêmico Porquinho.

- Backend: Java + Spring Boot
- Frontend: React
- Serviço ML: Python + FastAPI

---

# 📄 Licença

Este projeto possui finalidade educacional.
