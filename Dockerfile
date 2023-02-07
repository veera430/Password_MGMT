FROM python:3.8
RUN mkdir /app
WORKDIR /app

RUN python -m pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8000
CMD [ "python3", "manage.py", "runserver"]
