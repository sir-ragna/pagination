from flask import Flask, request, render_template
import os
import sqlite3

app = Flask(__name__)

app.config['DATABASE'] = os.getenv('DATABASE') or 'trashfire.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'secret$#€<>'

class Post():
    def __init__(self, attachment_id, attachment_filename, attachment_url, 
        attachment_message_id, message_content, message_author, 
        message_channel, timestamp):
        self.attachment_id = attachment_id
        self.message_id = attachment_message_id
        self.filename = attachment_filename
        self.url = attachment_url
        if attachment_url.endswith('.png'):
            self.type = 'img'
        else:
            self.type = 'other'
        self.content = message_content
        self.author = message_author
        self.nickname = message_author.split('#')[0]
        self.channel = message_channel
        self.timestamp = timestamp

#region database stuff
def get_posts_offset_based(offset=0, amount=5):
    with sqlite3.connect(app.config['DATABASE']) as conn:
        cursor = conn.execute("""
            SELECT attachment_id, attachment_filename, attachment_url, 
                attachment_message_id, message_content, message_author, 
                message_channel, Timestamp
            FROM attachments
            JOIN messages ON attachment_message_id = message_id
            ORDER BY datetime(Timestamp) DESC
            LIMIT ?,?;
        """, (offset, amount))
        rows = cursor.fetchall()
        posts = []
        for row in rows:
            post = Post(*row)
            posts.append(post)
        return posts

#endregion

#region routes
@app.route('/')
def homepage():
    return render_template('home.html.j2')

@app.route('/pages/<int:page>')
def offset_based(page):
    if page == 0:
        app.logger.error("page is 0 and it shouldn't be!")
        page = 1
    amount = 5
    offset = (page - 1) * amount
    posts = get_posts_offset_based(offset=offset, amount=amount)
    nextpage = page + 1
    previouspage = page - 1
    return render_template('limit_based.html.j2', posts=posts, 
        nextpage=nextpage, previouspage=previouspage)


@app.route('/cursor')
def cursor_based():
    timestamp = request.args.get('cursor')
    # get content
    return timestamp

#endregion


