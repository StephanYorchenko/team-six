# Pull base image
FROM python:3.9-alpine3.14

RUN apk --update add gcc make g++ zlib-dev

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system --dev

COPY . /code/

#CMD ["uvicorn app:app --host 0.0.0.0 --port 8000 --reload"]

EXPOSE 8000
