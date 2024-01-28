mig:
	./manage.py makemigrations
	./manage.py migrate
admin:
	python3 manage.py createsuperuser  --username admin --email  admin@mail.com

run:
	python3 manage.py runserver

req:
	pip3 freeze > requirements.txt

install-req:
	pip3 install -r requirements.txt
