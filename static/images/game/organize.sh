#!/bin/bash

# regex='(info)\\..*'

# for file in *; do
#         if [[ $file =~ $regex ]]; then
#                 echo $file
#         fi
# done
#
# im washed
#
for file in *.*; do
  if [ "$file" =~ ".sh" ]; then
    continue
  fi

  # strip off the extension
  base="${file%.*}"
  # grab the first character
  first="${base:0:1}"
  without=${base:1}

  if [ "$first" = "a" ]; then
    new="history"
  elif [ "$first" = "c" ]; then
    new="chess"
  fi
  new="${new}${without}.png"

  echo "first letter: $first, name without extension: $base, name without first: $without, -> $new"
  mv $file $new
done
