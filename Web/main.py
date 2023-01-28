from flask import Flask, request, render_template
from sheets import insert_row

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    host = request.form["host"]
    discordTag = request.form['discord-name']
    classes = "CAP4611, COP5030, PSY2000"
    array = []
    array.append(discordTag)
    array.append(classes)
    array.append(host)
    
    
    insert_row("1u0ue3KHkM1Mz_Xtcv__DFzACAxiYTLMvFTphSNQ_Was", "userData!A2:C10", "USER_ENTERED",
                  [
                      array
                  ]
                 )
    return 'Data submitted'

if __name__ == '__main__':
    app.run(debug=True)
  