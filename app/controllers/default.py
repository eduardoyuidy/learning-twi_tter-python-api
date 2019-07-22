from app import app

@app.route('/index', methods=['GET'])
@app.route('/', methods=['GET'])
def index():
    return "Hello World"

@app.route('/test', defaults={'name': None})
@app.route('/test/<name>')
def test(name):
    if name: 
        return "Olá, %s!" % name
    else: 
        return "Olá, usuário!"

# Converting param from str to int
@app.route('/testuser/<int:id>')
def testuser(id):
    print(type(id))
    return 'Id view'

