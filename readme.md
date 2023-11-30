# Getting started

You can setup everything in two  different ways


## Local without docker
You can run the code without docker by following the statements below.

```bash
cd source

py -m pip install --upgrade pip
py -m pip install -r requirements.txt

py manage.py migrate


### OR WITH VIRTUAL ENVIRONMENT ####
cd source

py -m venv .venv
# Activate (Powershell)
.\.venv\Scripts\Activate.ps1 
# Or (Unix)
./.venv/Scripts/activate

py -m pip install --upgrade pip
py -m pip install -r requirements.txt

```


## Migrations

```bash
# After changing the models, you will need to create migration files
py manage.py makemigrations

# The migration files are applied with this command
py manage.py migrate
```