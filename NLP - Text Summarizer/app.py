from flask import Flask, render_template,url_for,redirect
from flask import request as req
import requests

app = Flask(__name__)   # create instance of class Flask
@app.route('/',methods=["GET","POST"])         # decorator

def Index():
    return render_template('index.html')

@app.route("/Summarize",methods=["GET","POST"])
def Summarize():
    if req.method == "POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": f"Bearer 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"}
        
        data = req.form['data']

        minL=maxL//4
        maxL=int(req.form["maxL"])

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        output = query({
            "inputs": data,
            "parameters": {"min_length": minL, "max_length": maxL},
        })[0]

        return render_template('index.html',result=output["summary_text"])
    else:
        return render_template('Index.html')





if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)