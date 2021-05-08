from flask import Flask, render_template, request
from models import create_post, get_posts
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

	# if request.method == 'GET':
    #     pass

    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)

    posts = get_posts()

    return render_template('index.html', posts=posts)

@app.route('/posts', methods=['GET'])
def getAllPosts():

	# if request.method == 'GET':
    #     pass

    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)

    posts = get_posts()
    posts_l = []
    posts_d = {}
    for post in posts:
        posts_d["id"] = post[0]
        # posts_d["user_id"] = post[0]
        posts_d["username"] = post[1]
        posts_d["content"] = post[2]
        posts_d["likes"] = post[3]
        posts_l.append(posts_d)
    jsonString = json.dumps(posts_l)
    return "list: " + jsonString

if __name__ == '__main__':
    app.run(debug=True)
