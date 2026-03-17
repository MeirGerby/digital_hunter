FROM python:3.11-slim AS base 


WORKDIR /app 

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir  -r /requirements.txt


FROM base as api

COPY ./shared ./shared 
COPY ./api ./app/api 

CMD ["python", "-m", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]