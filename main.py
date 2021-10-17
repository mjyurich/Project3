from flask import Flask,render_template,request,jsonify
from textblob import TextBlob
import csv
import os



#-------------------------------------------------------------------------

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search",methods=["POST"])
def search():
    search_tweet = request.form.get("search_query")
    file_path = os.path.abspath(os.curdir)
    file = open(file_path + '/Resources/twitter_data.csv', 'r')
    reader = csv.reader(file)
    t=[]
    for line in reader:
      if search_tweet and search_tweet in line[1]:
       t.append(line[1])  
    tweets = []
    for tweet in t:
      polarity = TextBlob(tweet).sentiment.polarity
      subjectivity = TextBlob(tweet).sentiment.subjectivity
      tweets.append([tweet,polarity,subjectivity])

    return jsonify({"success":True,"tweets":tweets})

app.run()