FROM python:3.6.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN mkdir /fundoo
WORKDIR /fundoo
ADD requirements.txt /fundoo/
RUN pip install -r requirements.txt
ADD ./ /fundoo/
CMD ["python", "fundoo/manage.py", "runserver", "0.0.0.0:8000"]