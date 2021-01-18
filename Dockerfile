FROM python:3.5

ENV PYTHONUNBUFFERED 1
RUN mkdir /invera

WORKDIR /invera
COPY . /invera/

RUN pip install -r requirements.txt

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "invera", "invera.wsgi:application"]