
# Link Shortener Python 
Python comes with various feature and frameworks, Using best combinations with feature and frameworks We develop the small project for shorting browser urls and store them into the database. Using, 


## Tech Stack

**Frontend:** Basic Html-5

**Backend:** Python-Django (5.1.3)

**Database:** Sqlite (Defualt django)

Note : No need to install any external database, django comes with defualt database Sqlite. We also can go with other database later on.
## Run Locally
Create Python Virtual Environment (here is for mac or linux)

```bash
  python3 -m venv .env 
```

```bash
  source .env/bin/activate
```

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd django_shorting_url
```

Install dependencies with requirements.txt file.

```bash
  pip install -r requirements.txt
```

Ones you have with all dependencies then create database file.
```bash
  python3 manage.py migrate
```

Run server
```bash
  python3 manage.py runserver 
```

hurray, we done !! 🎉🥳

Create Admin user to access admin page.
``` bash
  python3 manage.py createsuperuser 
```




## Library's of python to use.

- [pyshorteners](https://pyshorteners.readthedocs.io/en/latest/)


## Reference Clips 

- [Click here](https://drive.google.com/file/d/1PWzalArJV3Kuvd7dQG0xSFHRjOqB0Xwu/view?usp=sharing)