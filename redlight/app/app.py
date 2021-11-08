from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''<!DOCTYPE html>
<html>
<head>
<style>
body {background-color: red;
      padding-top: 30%;
      padding-left: 40%;
      }
h1   {color: white;}
p    {color: white;}
</style>
</head>
<body>
<h1>RED LIGHT</h1>
<p>Don't Move</p>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050)