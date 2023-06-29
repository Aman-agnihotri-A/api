from flask import *
import db
app = Flask(__name__)  
@app.route('/')  
def message():  
      values= db.display()
      return render_template(
        'index.html',
        data=values,
      
    )
if __name__ == '__main__':  
   app.run(debug = True) 