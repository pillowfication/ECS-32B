#!/bin/bash

if [ "$1" == "" ]; then
  echo "No folder selected"
  exit
fi

DIR=${@%/}

# Create a new branch with only the folder specified
git checkout -B $DIR
git rm -rf .
git checkout HEAD -- $DIR
git checkout HEAD -- .gitignore

# Move all the files to the root of the repository
mv $DIR/* .
git rm -rf $DIR

# Commit everything
git add -A
git commit -m "Submit $DIR"

# Push and move back to master
git push -u origin $DIR
git checkout master
