FROM python:3.10.8


WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


#python -m pip install Pillow
#venv\Scripts\activate

#docker run -p 8000:8000 e-library
