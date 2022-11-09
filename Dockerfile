FROM python:3.10.8

<<<<<<< HEAD
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
=======

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


#python -m pip install Pillow
#venv\Scripts\activate
>>>>>>> WIN-26-Custom_user_profile
