# Stockspot
Stockspot Pandora Challenge(django)


### Prequisites

- Python 3.6+
- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
- [pipenv](https://pipenv.readthedocs.io/en/latest/)
- MySQL 5.7+

### Setup

- Install dependencies and activate virtualenv(must setup your own mysql)

  ```
  pipenv shell # activate python virtualenv
  pip install -r requirements.txt
  manage.py runserver 7000
  ```

- Build & launch development server(mysql is included in the docker-compose)

  ```
  docker-compose build # will import data file from the resources directory
  docker-compose up # localhost:7000
  ```

- Initialise DB and import data
  ```
  docker-compose exec app python manage.py migrate
  docker-compose exec app python manage.py import_company resources/companies.json -d
  docker-compose exec app python manage.py import_people resources/people.json -d
  ```

### Configuration

- Change DB configuration

  ```
  Modify "paranuara/settings.py" file
  ```

- Change data file
  ```
  Replace files in the "resources/" directory
  
  In docker shell
  python manage.py import_company resources/companies.json -d
  python manage.py import_people resources/people.json -d

  After reset the DB, unittest should be modified accordingly
  ```

### Test

- Unit Test
  ```
  docker-compose exec app python manage.py test
  ```

- curl example
  ```
  curl http://127.0.0.1:7000/v1/api/company/BUGSALL

  curl "http://127.0.0.1:7000/v1/api/people/Moon%20Herring"

  curl "http://127.0.0.1:7000/v1/api/people/Moon%20Herring,Rosemary%20Hayes"
  ```
