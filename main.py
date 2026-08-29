from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)

# В вашем Flask приложении
app.jinja_env.globals['static'] = lambda filename: url_for('static', filename = filename)



@app.route('/')
def home():
    """Главная страница"""
    # Проверяем, была ли нажата ссылка "Моя страница"
    show_content = request.args.get('show', 'false') == 'true'
    return render_template('home.html', page = 'home', show_content = show_content)


@app.route('/content')
def content():
    show_content = request.args.get('show', 'false') == 'true'
    return render_template('content.html', page = 'content', show_content = show_content)



if __name__ == '__main__':
    app.run(debug = True, port = 5000)