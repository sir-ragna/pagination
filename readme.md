
# An implementation of offset-based and cursor-based pagination

Article explaining both: 
https://uxdesign.cc/why-facebook-says-cursor-pagination-is-the-greatest-d6b98d86b6c0


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

## Database dependency

This project expects a database to be present 'trashfire.db'.

The schema:

```sql
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "attachments" (
	"attachment_id"	INTEGER,
	"attachment_filename"	TEXT,
	"attachment_url"	TEXT,
	"attachment_message_id"	INTEGER,
	PRIMARY KEY("attachment_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "messages" (
	"message_id"	INTEGER,
	"message_content"	TEXT,
	"message_author"	TEXT,
	"message_channel"	TEXT,
	"Timestamp"	TEXT NOT NULL,
	PRIMARY KEY("message_id" AUTOINCREMENT)
);
COMMIT;
```

You can fill it up by running a discord bot script.
https://github.com/ReX342/Prometheus/blob/824780c5a13e8a2923c7e0252a4eaf33a0beb045/discordbot/Prometheus.py