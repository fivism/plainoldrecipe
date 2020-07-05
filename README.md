This program parses recipes from common websites and displays them using
plain-old HTML.

You can use it here: https://www.plainoldrecipe.com/

Saver Branch
-----------
This runs locally and uses AutoIndex to view cached recipes saved in the `recipes` folder.

Todos:
- [ ] Format the AutoIndex to be more mobile friendly or find out if we can drop the index pathing to leave it to Apache's default indexer (maybe more [mobile friendly](https://github.com/mulhoon/doxy)?) 
- [ ] Allow access to this mobile service from outside the home network (?) 
- [ ] Fix the state that causes `/recipes` to fail when the directory is not created yet. (Create the folder at initial runtime perhaps) 
- [ ] favicon
- [ ] add https://www.onceuponachef.com/
- [ ] use lispy case for cached recipes not snake_case
- [ ] Favicon and apple-touch-icon the /recipes url 
- [ ] Rebase most of this into an atomic commit

Screenshots
-----------

Home Page:
![Home Page](/screenshots/home.png?raw=true "Home Page")

View the recipe in your browser:
![Recipe](/screenshots/screen.png?raw=true "Recipe")

If you print the recipe, shows with minimal formatting:
![Print View](/screenshots/print.png?raw=true "Print View")

Deploy
------

gcloud app deploy --account=gargoylemusic@gmail.com --project=plainoldrecipe 

Acknowledgements
----------------

- https://github.com/hhursev/recipe-scrapers
- https://evenbettermotherfucking.website/

Contributing
------------

1. If you want to add a new scraper, please feel free to make a PR. Your diff
   should have exactly two files: `parsers/__init__.py` and add a new class
   in the `parsers/` directory. [Here is an example](https://github.com/poundifdef/plainoldrecipe/commit/cac857c1abb1a8cb674a2a63ebb24df0c00aa666) of what your commit might
   look like.

2. If you want to fix a bug in an existing scraper, please feel free to do so,
   and include an example URL which you aim to fix. Your PR should modify exactly
   one file, which is the corresponding module in the `parsers/` directory.

3. If you want to make any other modification or refactor: please create an
   issue and ask prior to making your PR. Of course, you are welcome to fork,
   modify, and distribute this code with your changes in accordance with the LICENSE.

4. I don't guarantee that I will keep this repo up to date, or that I will respond
   in any sort of timely fashion! Your best bet for any change is to keep PRs small
   and focused on the minimum changeset to add your scraper :)
