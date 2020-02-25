### COMP0034 Web Development
This repository is a very simple illustration of use of the the Flask-Uploads package with Flask-WTF and Flask-SQLAlchemy.

Issue: `ImportError: cannot import 'secure_filename' from 'werkzeug'`
There appears to be a compatibility issue with the recent release of Werkzeug 1.0.0 and Flask-Uploads. You may need to use Werkzeug 0.16.1 to get Flask-Uploads to work.