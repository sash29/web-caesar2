from caesar2 import rotate_string
from flask import Flask,request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form method="POST">
        <label>Rotate by
                <input name="rot" type="text" value=0><br>
        </label><br>
                                  
        <textarea rows="4" cols="50" name="text" >
        </textarea><br>
        
        <input type = "submit" value='Submit Query'>
        
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=['post'])
def encrypt():
    rot_by=int(request.form['rot'])
    text_inp=str(request.form['text'])
    result=rotate_string(text_inp, rot_by)
    return'<h1>'+ result + '</h1>'
app.run()
    