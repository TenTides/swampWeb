from flask import Flask, request, render_template
from sheets import insert_row

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    discord_id = request.form['discord-name']
    insert_row("1u0ue3KHkM1Mz_Xtcv__DFzACAxiYTLMvFTphSNQ_Was", "userData!A2:C10", "USER_ENTERED",
                  [
                      [discord_id]
                  ]
                 )
    return 'Data submitted'

if __name__ == '__main__':
    app.run(debug=True)