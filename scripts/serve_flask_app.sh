#!/bin/sh

set -e # abort if any command fails

export FLASK_APP=magical_chords
export FLASK_ENV=development

echo "Creating database"
flask init-db
echo "Executing flask service"
flask run -h 0.0.0.0  
