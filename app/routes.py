from app import app

@app.route('/')
@app.route('/index')

def index():
    return "Let's get to work."