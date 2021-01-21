#!/bin/bash
# service setup

apt get install python3
python3 -V

apt install python3-venv
python3 -m venv venv

source venv/bin/activate
pip install Flask
pip install -r requirements.txt
deactivate

echo "Preprocess edges? [Y/N]:"
read pre_edges

if [ "$pre_edges" == "Y" ] || [ "$pre_edges" == "y" ]; then
	gnome-terminal -e ./precalc_edges.sh
fi

source venv/bin/activate
export FLASK_APP=./sample/app.py
flask run