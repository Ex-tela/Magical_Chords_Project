#!/bin/sh

export FLASK_APP=magical_chords
export FLASK_ENV=development

echo "Executing flask service"
flask run -h 0.0.0.0  
