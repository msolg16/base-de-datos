from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class EquipoModel(db.Model):
	__tablename__ = "equipos"

	id = db.Column(db.Integer, primary_key=True)
	pais = db.Column(db.String())
	idioma = db.Column(db.String())
	continente = db.Column(db.String())
	grupo = db.Column(db.String())
	entrenador = db.Column(db.String())
	capitan = db.Column(db.String())
	puntaje = db.Column(db.Integer())

	def __init__(self, pais, idioma, continente, grupo, entrenador, capitan, puntaje):
		self.pais = pais
		self.idioma = idioma
		self.continente = continente
		self.grupo = grupo
		self.entrenador = entrenador
		self.capitan = capitan
		self.puntaje = puntaje

		def __repr__(self):
			return f"{self.pais}:{self.grupo}"

			