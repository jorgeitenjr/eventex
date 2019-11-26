# Eventex 

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/jorgeitenjr/eventex.svg?branch=master)](https://travis-ci.org/jorgeitenjr/eventex)
[![Maintainability](https://api.codeclimate.com/v1/badges/2dfe85683c862c8ffd1d/maintainability)](https://codeclimate.com/github/jorgeitenjr/eventex/maintainability)
## Como desenvolver?

1. Clone o repositório.
2. Crie um virtualenv com Python 3.8
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```console
git clone git@github.com:jorgeitenjr/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```
## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para instância
4. Defina DEBUG=False
5. Configure o serviço de e-ail
6. Envie o código para o heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configurar o email
git push heroku master --force
```



