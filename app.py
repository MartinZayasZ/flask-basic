from database import db
from models import Persona
from flask import Flask, render_template
from flask_migrate import Migrate

app = Flask(__name__)

# Configuración  flask-wtf
app.config['SECRET_KEY'] = 'LLAVE_SECRETA'

# Configuración de la db
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB = 'sap_flask_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Inicialización del objeto db de sqlalchemy
# db = SQLAlchemy(app)
db.init_app(app)

# configurar flask-migrate
migrate = Migrate()
migrate.init_app(app, db)


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
    # Listado de personas
    personas = Persona.query.all()
    total_personas = Persona.query.count()

    app.logger.debug(f'Listado Personas: {personas}')
    app.logger.debug(f'Total Personas: {total_personas}')

    return render_template('index.html', personas=personas, total_personas=total_personas)

@app.route('/ver/<int:id>')
def ver_detalle(id):
    # persona = Persona.query.get(id)
    persona = Persona.query.get_or_404(id)
    app.logger.debug(f'Ver persona: {persona}')
    return render_template('detalle.html', persona=persona)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    persona = Persona()

    return render_template('agregar.html')


