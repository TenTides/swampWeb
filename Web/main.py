from flask import Flask, request, render_template # pylint: disable=import-error
from sheets import insert_row, del_row, sheets_to_df
from similarity import compare

app = Flask(__name__)

@app.route('/')
def home():
    """home page"""
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    """submit page"""
    host = request.form["host"]
    discord_tag = request.form['discord-name']
    classes = request.form.getlist("courses")
    array = []
    array2 = [discord_tag, host]
    comp_array = ["COP2500","COP3223C","CDA3103","COP3502C","COP3503C","COP3330","COP3402","Foundation Exam","COP4331C","COT3100","CIS3360"]

    for i in range(len(comp_array)): 
        if(classes.count(comp_array[i]) == 0):
            classes.insert(i," ")
    for i in range(len(comp_array)-len(classes)):
        classes.append(" ")
    for i in classes:
        if(i == " "):
            array.append(0)
        else:
            array.append(1)
    array2.extend(array)

    comparison_df = sheets_to_df("1u0ue3KHkM1Mz_Xtcv__DFzACAxiYTLMvFTphSNQ_Was", "userData!A1:M100000")
    insert_row("1u0ue3KHkM1Mz_Xtcv__DFzACAxiYTLMvFTphSNQ_Was", "userData!A2:C10",[array2])
    
    full_df = sheets_to_df("1u0ue3KHkM1Mz_Xtcv__DFzACAxiYTLMvFTphSNQ_Was", "userData!A1:M100000")
    
    print(comparison_df)
    
    group = compare(array2, comparison_df)
    # bot_message(group)
    
    print(group)
    
    for member in group:
        # member_row = full_df.loc[full_df['discord_id']== member, full_df.index].iat[0]
        # value = df.loc[df['B'] == 5, full_df.index].iat[0]
        # member_row = full_df.loc[full_df['discord_id']== member].item()
        print(member_row)
        del_row("1u0ue3KHkM1Mz_Xtcv__DFzACAxiYTLMvFTphSNQ_Was", "0", "userData!A2:C10", member_row, member_row + 1)
    
    return render_template('post.html')

if __name__ == '__main__':
    app.run(debug=True)