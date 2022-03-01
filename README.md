# Mission-to-Mars

## Purpose

Create a web applicaiton that scrapes data from various websites and amalgamates data related to Mars exploration and information onto a single html page.

## Process

1) Data-Finding & Scraping 
We scrapes the following data:
-NASA Mars News
-JPL Mars Space Images
-Mars Weather
-Mars Facts
-Mars Hemispheres with Pictures

2) MongoDB Setup
We set up a mongo database under the collection mars. THis houses our scraped data so that we can access it freely and connect what we find more consistently to our web application

3) Flask Application
Using flask's webdev framework, we configured a simple locally-hosted website to house our scraped data on the Mission to Mars. THe app.py for the flask app contains two routes: the base route ('/') and the revised scraped data route ('/scrape')


## Summary

The result is a website framework, polished with bootstrap & CSS stylesheets, that allows you to scrape data with the click of a button then display it.

The site has a technical error in it that I hope to debug later down the line.

