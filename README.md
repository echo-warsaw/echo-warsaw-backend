# System requirements
[mongodb, redis-server, yarn]

# Installation

git clone https://github.com/echo-warsaw/echo-warsaw-backend.git

git clone https://github.com/echo-warsaw/echo-warsaw.github.io.git

cp -a /echo-warsaw.github.io/. /echo-warsaw-backend/static/

cd ./echo-warsaw-backend/static

yarn install && yarn build

cd ..

## using NLTK:
- 'pip install nltk'
- 'python'
- import nltk
- nltk.download()

Z Corpora pobrać:
- Wordnet
- omw

### do this in virtualenv
pip install -r requirements.txt

python runserver.py
