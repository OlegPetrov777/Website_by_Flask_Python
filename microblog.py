from app import app, db, cli
from app.models import User, Post, Answer


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Answer': Answer}
