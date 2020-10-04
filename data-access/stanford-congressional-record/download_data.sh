#!/bin/bash

StringVal="audit.zip hein-bound.zip hein-daily.zip speakermap_stats.zip vocabulary.zip phrase_clusters.zip phrase_partisanship.zip party_full.zip"

# Iterate the string variable using for loop
for val in $StringVal; do
    echo "Pulling:"
    echo $val
    url=$(printf 'https://stacks.stanford.edu/file/druid:md374tz9962/%s' "$val")
    wget $url
    unzip $val
    rm $val
    echo "....done"
done
