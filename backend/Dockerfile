# Etapa 1: Usar a imagem oficial do Python como base
FROM python:3.12-slim as base

# Etapa 2: Instalar dependências do sistema necessárias para a instalação de pacotes
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Etapa 3: Instalar o Poetry
RUN pip install poetry

# Etapa 4: Definir o diretório de trabalho no container
WORKDIR /app

# Etapa 5: Copiar o pyproject.toml e poetry.lock (se existir)
COPY pyproject.toml poetry.lock* /app/

# Etapa 6: Instalar as dependências do projeto com o Poetry
RUN poetry install --no-root --no-dev  # Instalando dependências para produção

# Etapa 7: Copiar o restante do código-fonte do projeto
COPY ./backend /app

# Etapa 8: Expor a porta padrão do Django (8000)
EXPOSE 8000

# Etapa 9: Definir o comando de execução para rodar o servidor Django
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
