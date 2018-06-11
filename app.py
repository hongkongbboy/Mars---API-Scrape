# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app)

# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # Find data
    mars_data = mongo.db.collection.find()

    # return template and data
    return render_template("index.html", mars_data=mars_data)

# Route that will trigger scrape functions
@app.route("/scrape")
def scrape():

    # Run scraped functions
    news = scrape_mars.scrape_news()
    weather = scrape_mars.scrape_weather()
    facts = scrape_mars.scrape_facts()
    hemispere = scrape_mars.scrape_hemisperes()

    # Store results into a dictionary
    listings = {
        "news_headline": news["news_headline"],
        "news_discription": news["news_discription"],
        "news_weather": weather["news_weather"],
        "mars_facts": facts["mars_facts"],
        "hemisperes": hemispere["hemisperes"]
    }

    # Insert forecast into database
    mongo.db.collection.insert_one(listings)

    # Redirect back to home page
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)