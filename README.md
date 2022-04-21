# DigiCom+

## from GoBeyond Digital

This is the backend for GBD's DigiCom+, an app that provides credit ratings based on corporate compliance and a number of other factors.

### Basic setup

It's recommended that you have [Pipenv](https://pipenv.pypa.io/en/latest/) set up in your environment; this will allow you to reproduce the server exactly. You will, of course, also need Python and Pip.

To set up this app:

1. Clone the repo
2. Run `pipenv install` to install the necessary packages.
3. Run `export FLASK_APP=server.server` to set Flask to the appropriate file. You can also run `export FLASK_ENV=development` to set up debug mode.
4. Run `flask run` to launch the server.

### Structure

This project is setup largely as a skeleton; the Flask server is separated from the model for ease of refactoring. Replacing Flask with Django or another server technology should be fairly straightforward.

### To do

1. Integrate the server with the APIs of any data providers.
2. Set up databases to store the info.
3. Security & auth; power-user customers will also need storage for their own custom weights and rating scales when generating scores for the companies they're looking into.
