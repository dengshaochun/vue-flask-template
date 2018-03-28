# vue-flask-template

> A minimal vue admin template with Element UI & axios & iconfont & permission control & lint & flask

## Backend Build Setup

``` bash

# Clone project
git clone https://github.com/dengshaochun/vue-flask-template.git

# change to backend directory
cd backend

# install pipenv and install requirements python packages
sudo pip install pipenv && pipenv install

# init database
pipenv run python manange.py db init && pipenv run python manange.py db migrate && pipenv run python manange.py db upgrade

# feed test data
pipenv run python manange.py feed_data

# run backend servers, server localhost:5000, user: dengsc@example.com pass:12345
pipenv run python manange.py runserver

```

## Frontend Build Setup

```bash

# change to frontend directory
cd ../frontend

# Install dependencies
npm install

# server with hot reload at localhost:9528
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```
Frontend demo copy from `https://github.com/PanJiaChen/vueAdmin-template`

## Demo
![demo](https://github.com/PanJiaChen/PanJiaChen.github.io/blob/master/images/demo.gif)
