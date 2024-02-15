#!/bin/bash


for d in ./*.txt
do
    if ! [[ -f $d ]]; then
        continue
    fi



    filename=$(basename $d)
    dirname=$(echo $filename | cut -d'.' -f1)

    mv $filename $dirname/$filename

done