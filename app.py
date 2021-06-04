from flask import Flask , redirect , url_for , render_template , request , flash , send_file

app = Flask(__name__)

@app.route("/" , methods=["GET" , "POST"])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:    
        file = request.files['file']
        print(file.filename)
        file.save("D:/Programming/Flask/uploads/" + file.filename)
        return send_file('D:/Programming/Flask/uploads/lol.txt' , as_attachment=True)
@app.route("/home" , methods=['GET' , 'POST'])
def nothing():
    if request.method == "POST":
        link = request.form["link"]
        print(link)
        web_link =  "https://" + str(link) + ".com"
        return redirect(web_link)
    else:
        return render_template("nothing.html")
    
if __name__ == '__main__':
    app.run(debug=True)