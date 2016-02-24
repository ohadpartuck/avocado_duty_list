from flask import Flask, render_template, url_for, redirect
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
from flask_debugtoolbar import DebugToolbarExtension
import os


ENV = os.environ.get('PYTHON_ENV') or 'development'
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'avocado_'+ repr(ENV),
    'host': 'localhost',
    'port': 27017
}
app.config['DEBUG_TB_PANELS'] = (
    'flask_debugtoolbar.panels.versions.VersionDebugPanel',
    'flask_debugtoolbar.panels.timer.TimerDebugPanel',
    'flask_debugtoolbar.panels.headers.HeaderDebugPanel',
    'flask_debugtoolbar.panels.request_vars.RequestVarsDebugPanel',
    'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel',
    'flask_debugtoolbar.panels.template.TemplateDebugPanel',
    'flask_debugtoolbar.panels.sqlalchemy.SQLAlchemyDebugPanel',
    'flask_debugtoolbar.panels.logger.LoggingPanel',
    'flask_debugtoolbar.panels.route_list.RouteListDebugPanel',
    'flask_debugtoolbar.panels.profiler.ProfilerDebugPanel',
    'flask.ext.mongoengine.panels.MongoDebugPanel'
)

db = MongoEngine(app)
# use mongo as a session store
# app.session_interface = MongoEngineSessionInterface(db)
app.debug = True
app.config['SECRET_KEY'] = '1111'
toolbar = DebugToolbarExtension(app)

class User(db.Document):
    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)

@app.route('/')
def hello_world():
    for user in User.objects:
        a = user.email
    return render_template('index.html')

@app.route('/redirect')
def redirect_example():

    response = redirect(url_for('index'))
    response.set_cookie('test_cookie', '1')
    return response

# Paginate through todo
def view_todos(page=1):
    paginated_todos = Todo.objects.paginate(page=page, per_page=10)

# Paginate through tags of todo
def view_todo_tags(todo_id, page=1):
    todo = Todo.objects.get_or_404(_id=todo_id)
    paginated_tags = todo.paginate_field('tags', page, per_page=10)
if __name__ == '__main__':
    app.run(port=8000, use_reloader=True, debug=True)
