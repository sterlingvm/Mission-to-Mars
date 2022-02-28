from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraper

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route('/')
def index():
    mars = mongo.db.mars.find_one() # interesting that a variable is serving as a recallable function here
    return render_template('index.html', mars=mars)

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars # reference the database using a variable
   mars_data = scraper.scrape_all() # 
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

# EXAMPLE of Flask update database syntax:
# .update_one(query_parameter, {"$set": data}, options)

if __name__ == "__main__":
   app.run()