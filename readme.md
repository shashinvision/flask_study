### Soruce From

```
https://flask.palletsprojects.com/en/3.0.x/quickstart/
```

```
pip install flask gunicorn
```
```
python3 -m venv .venv

```
## Run on develop
```
flask --app main run --host=0.0.0.0 --debug
```


## run on production
```
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

## Freeze 
```
pip freeze > requirements.txt
```

## install requirements
```
pip install -r requirements.txt
```