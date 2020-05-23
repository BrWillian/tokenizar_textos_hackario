from app import app
from flask import request, render_template
import requests
import re
from bs4 import BeautifulSoup
import nltk
from app.controllers.stop import stopwords

@app.route('/', methods=['POST', 'GET'])
def index():
	erros = []
	resultado = []	
	if request.method == "POST":
		try:
			url = request.form['url']
			resposta = requests.get(url)
		except:
			erros.append(
				"Não foi possivel acessar a url especificada, Por favor entre com uma url valida!"

			)


		if resposta:
			texto = BeautifulSoup(resposta.text, 'html.parser').get_text()
			nltk.data.path.append('./data/')
			tokens = nltk.word_tokenize(texto)
			texto_tokenizado = nltk.Text(tokens)

			tirar_pont = re.compile('.*[A-Za-z].*')

			palavr_text = [ p for p in texto_tokenizado if tirar_pont.match(p)]
			no_stop_words = [ p for p in palavr_text if p.lower() not in stopwords]
			return stopwordsg
	return render_template('index.html', erros=erros)