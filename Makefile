#Archivo para configurar comandos personalizados
runserver:
	python3 manage.py runserver --settings=settings.local
makemigrations:
	python3 manage.py makemigrations --settings=settings.local
makemigrations:
	python3 manage.py migrate --settings=settings.local