**Report is updated every minute for testing celery**

### INSTALLATION:
1. git clone --branch celery-docker https://github.com/DenMaslov/quiz_celery.git
2. cd quiz_celery
3. pipenv shell
4. pipenv install
5. cd survey_models_django
6. docker-compose build
7. docker-compose up -d
8.  docker-compose exec web python manage.py migrate


### TESTED WITH:
* Windows 10
* Chrome
* python 3.9
