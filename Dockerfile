FROM python:3.12.4-alpine3.20

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN pip install --upgrade pip; \
    pip install poetry;

RUN poetry config virtualenvs.in-project true; \
    poetry install --no-interaction --no-ansi;

COPY pyservice /app/pyservice
CMD ["poetry", "run", "uvicorn", "pyservice.api.main:app", "--port", "8000", "--reload"]

EXPOSE 8000