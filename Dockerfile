FROM python:3.11-slim AS base 

ENV PYTHONDONTWRITEBINARYCODE=1 \
    PYTHONPATH=/ 

WORKDIR /app 

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir  -r requirements.txt


FROM base as api

COPY ./shared ./shared 
COPY ./api ./app/api 
EXPOSE 8000 
CMD ["python", "-m", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]