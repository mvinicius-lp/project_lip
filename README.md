# ReMind 📚🔥

ReMind é uma plataforma de organização e acompanhamento de estudos baseada em **aprendizado ativo**, **revisões espaçadas** e **métricas de desempenho**, ajudando o usuário a manter constância, foco e evolução real nos estudos.

O sistema foi desenvolvido com **FastAPI**, **MongoDB** e **arquitetura orientada a objetos**, seguindo princípios de **Clean Architecture**.

---

## 🚀 Funcionalidades Principais

### 📖 Estudos
- Cadastro de estudos com:
  - Disciplina
  - Conteúdo estudado
  - Tempo dedicado (horas e minutos)
  - Nível de dificuldade
- Edição de estudos
- Exclusão de estudos (com exclusão automática das revisões associadas)

### 🔁 Revisões
- Geração automática de revisões espaçadas
- Marcação de revisão como concluída
- Registro de tempo dedicado por revisão
- Exclusão de revisões individuais

### 🔥 Ofensiva (Streak)
- Contabiliza **dias consecutivos de estudo**
- Um dia conta como ofensiva se o usuário:
  - Registrar um estudo **ou**
  - Concluir ao menos uma revisão
- Caso o usuário fique um dia sem atividade, a ofensiva é automaticamente zerada

### 📊 Dashboard
- Total de revisões do dia
- Dias de ofensiva atual
- Tempo total estudado
- Disciplina mais estudada
- Próximas revisões
- Atividade semanal

### 📜 Histórico
- Histórico completo de estudos:
  - Data
  - Disciplina
  - Tópico estudado
  - Tempo dedicado
- Gestão de estudos diretamente pelo histórico

### 📄 Relatório em PDF
- Geração de relatório completo do usuário
- Contém:
  - Histórico de estudos
  - Métricas gerais
- Download direto via endpoint

### 🎨 Disciplinas
- CRUD completo de disciplinas
- Cada disciplina possui:
  - Nome
  - Cor personalizada

### 👤 Usuários
- Cadastro e autenticação

---

## 🧱 Arquitetura

O projeto segue **Clean Architecture**, com separação clara de responsabilidades:

## 🧱 Estrutura do Projeto

app/
├── api/
│   └── routers/
├── application/
│   └── use_cases/
├── domain/
│   └── entities/
├── infrastructure/
│   └── mongodb/
├── core/
└── utils/

## Princípios aplicados

- Orientação a Objetos

- Casos de uso isolados

- Repositórios desacoplados

- Domínio independente de framework

- Infraestrutura substituível

## 📦 Instalação

### Clonar o repositório

git clone <url-do-repositorio>
cd lip

### Criar ambiente virtual

python -m venv venv

### Ativar o ambiente virtual

## Windows

venv\Scripts\activate


## Linux / macOS

source venv/bin/activate

### Instalar dependências

pip install -r requirements.txt

## Rodar o projeto

uvicorn app.main:app --reload

