FROM python:3.10

RUN mkdir -p /usr/app/
WORKDIR /usr/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# RUN chmod +x db.sh

# ENTRYPOINT ["/usr/app/db.sh"]

# CMD ["gunicorn","backend.wsgi:application", "--bind", "0.0.0.0:8000", "--timeout", "120", "-k", "gevent", "--workers" ,"4", "--log-level","info","--capture-output"]
