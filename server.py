from flask import Flask, render_template


app = Flask(__name__)   
@app.route('/play')         
def play():
    return render_template("index.html", times = 3, color = 'cornflowerblue')  


@app.route('/play/<int:num>')
def boxes(num):
    return render_template("index.html", times= num, color = 'cornflowerblue')

@app.route('/play/<int:num>/<string:color>')
def boxes2(num, color):
    return render_template("index.html", times= num, color = color,)




if __name__=="__main__":     
    app.run(debug=True)   

