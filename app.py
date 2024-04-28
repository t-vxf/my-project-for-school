from flask import Flask, render_template, request, jsonify
import sqlite3,json

app = Flask(__name__, template_folder='template')

def query_db(page_name):
    with open("content.json") as content:
        content_data=json.load(content)
    return content_data.get(page_name)
            
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/page/<page_name>')
def page(page_name):
    content = query_db(page_name)
    if content:
        videos = [{'title': key, 'url': value} for key, value in content.get('videos', {}).items()]

        
        print(videos)
        page_name = content['page-name']
        return render_template('page.html', videos=videos,page_name=page_name)

    return "الصفحة غير موجودة", 404

if __name__ == '__main__':
    app.run(debug=True)
