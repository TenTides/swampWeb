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
    classes = request.form.getlist("courses")
    array = []
    array2 = [discordTag,host]
    compArray = ["COP2500","COP3223C","CDA3103","COP3502C","COP3503C","COP3330","COP3402","Foundation Exam","COP4331C","COT3100","CIS3360"]

    for i in range(len(compArray)):
        if(classes.count(compArray[i]) == 0):
            classes.insert(i," ")
    for i in range(len(compArray)-len(classes)):
        classes.append(" ")
    for i in classes:
        if(i == " "):
            array.append(0)
        else:
            array.append(1)
    array2.extend(array)

    insert_row("1u0ue3KHkM1Mz_Xtcv__DFzACAxiYTLMvFTphSNQ_Was", "userData!A2:C10",[array2])
    return render_template('post.html')

if __name__ == '__main__':
    app.run(debug=True)
  