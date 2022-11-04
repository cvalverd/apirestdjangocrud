FROM python:3.9-alpine
RUN apk add --no-cache bash
RUN apk add gcc musl-dev mariadb-connector-c-dev
WORKDIR /APIRESTdjangoCRUD
COPY APIRESTdjangoCRUD/requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY APIRESTdjangoCRUD APIRESTdjangoCRUD
