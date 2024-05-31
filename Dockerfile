FROM huecker.io/library/python:3.11-alpine

WORKDIR /kitchenView

RUN pip install --upgrade pip
RUN pip install poetry && poetry config virtualenvs.create false

RUN mkdir static && mkdir kitchenView

COPY ./poetry.lock ./pyproject.toml /kitchenView/

RUN poetry install --no-interaction

COPY ./kitchenView /kitchenView/kitchenView

CMD ["uvicorn", "kitchenView.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]