

from flask import  jsonify, json, render_template, request, url_for, redirect, flash, Blueprint
from werkzeug.exceptions import abort

from app.main import bp
from app.utils import get_db_connection, get_post
from main import app

# Define the main route of the web application 
@bp.route('/')
@bp.route('/index')
def index():

    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()

    return render_template('index.html', posts=posts)

# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@bp.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
        app.logger.error(f"Post_id: `{post_id}` not found")
        return render_template('404.html'), 404
    else:
        app.logger.info(f'Article "{post["title"]}" retrieved')
        return render_template('post.html', post=post)

# Define the About Us page
@bp.route('/about')
def about():
    app.logger.info(f'The "About Us" page is retrieved')
    return render_template('about.html')

# Define the post creation functionality 
@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            connection.close()

            app.logger.info(f'A new article called "{title}" is created.')
            return redirect(url_for('main.index'))

    return render_template('create.html')

@bp.route('/healthz')
def healthz():
    response = app.response_class(
        response=json.dumps({"result": "OK - Healthy"}),
        status = 200,
        mimetype="application/json"
    )
    app.logger.info("Health status request successful")
    return response

@bp.route('/metrics')
def metrics():
    connection = get_db_connection()
    posts_cnt = connection.execute('SELECT COUNT(*) FROM posts').fetchone()
    connection.close()
    
    response = app.response_class(
        response=json.dumps({
            "result": "OK - Healthy",
            "db_connection_count": posts_cnt[0]
            }
        ),
        status = 200, 
        mimetype="application/json"
    )
    return response