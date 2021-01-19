#!/bin/bash
# precalc edges

source venv/bin/activate
pip install Flask
pip install flask_script

python ./admin.py edges
