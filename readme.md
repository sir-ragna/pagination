
# First time set-up

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create file .flaskenv with parameters.

```sh
FLASK_ENV=development
FLASK_RUN_PORT=5000

DATABASE="trashfire.db"
SECRET_KEY="f48580fff014fce82b31c4cee4a13504"
```

Now you can execute `flask run`.

# Running again

Activate the environment and run flask.

```sh
source venv/bin/activate
flask run
```


