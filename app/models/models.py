from app import db
from datetime import date



class SalvarBusca(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	data = db.Column(db.Date, default=date.today)
	url = db.Column(db.CLOB)
	palavras = db.Column(db.CLOB)
	palavras_c = db.Column(db.CLOB)

	def __init__(self, url, palavras, palavras_c):
		self.url = url
		self.palavras = palavras
		self.palavras_c = palavras_c

	def __repr__(self):
		return '<Url %r>' % self.url