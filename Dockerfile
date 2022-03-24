# Pull base image
FROM python:3.9-alpine3.14

RUN apk --update add gcc make g++ zlib-dev

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# Install dependencies
RUN pip install pipenv uvicorn
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system --dev

COPY ./start.sh /start.sh
RUN chmod a+x /start.sh

COPY . /code/

CMD ["./start.sh"]

#EXPOSE 8000
