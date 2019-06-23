from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('home.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404