from flask import Flask, render_template, request, jsonify, redirect, make_response, url_for, flash
from flask_autoindex import AutoIndex
from recipe_scrapers import scrape_me, WebsiteNotImplementedError, SCRAPERS
import urllib
import parsers
import logging
from pathlib import Path
import os

app = Flask(__name__)

files_index = AutoIndex(app, os.path.curdir + '/recipes', add_url_rules=False)

def save_recipe(rendered_recipe, recipe_name):
    Path("recipes").mkdir(parents=True, exist_ok=True)
    fname = "recipes/" + recipe_name.replace(" ", "_") + ".html"
    text_file = open(fname, "w")
    text_file.write(rendered_recipe)
    text_file.close()

def scrape_recipe(url):
    recipe = {}

    try:
        scraper = scrape_me(url)
        instructions = [i.strip() for i in scraper.instructions().split("\n") if i.strip()]
        recipe = {
            'name': scraper.title(),
            'ingredients': scraper.ingredients(),
            'instructions': instructions,
            'image': scraper.image(),
            'url': url,
        }
    except WebsiteNotImplementedError:
        pass

    if not recipe:
        parsed_uri = urllib.parse.urlparse(url)
        domain = parsed_uri.netloc.lower()
        domain = domain.replace('www.', '', 1) if domain.startswith('www.') else domain
        parser = parsers.getParser(domain)

        if parser is None:
            return None

        recipe = parser.Parse(url)

        #try:
        #    recipe = parser.Parse(url)
        #except:
        #    return recipe

    return recipe

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipe')
def recipe():
    url = request.args['url']
    parsed_uri = urllib.parse.urlparse(url)
    domain = parsed_uri.netloc.lower()

    try:
        recipe = scrape_recipe(url)
        if recipe is None:
            return render_template('unsupported.html', domain=domain)

        rendered_recipe = render_template('recipe.html', recipe=recipe)
        save_recipe(rendered_recipe, recipe['name'])

        return rendered_recipe
    except:
        logging.exception(url)
        return render_template('parse_error.html', domain=domain)

@app.route('/recipes')
@app.route('/recipes/<path:path>')
def autoindex(path='.'):
    return files_index.render_autoindex(path)

@app.route('/supported-websites')
def supported_websites():
    sites = list(SCRAPERS.keys())
    sites += parsers.PARSERS
    sites.sort()

    return render_template('supported.html', sites=sites)

if __name__ == '__main__':
    app.run('localhost', 8080, debug=True, threaded=True)
