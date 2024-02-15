#!/bin/bash


while read -r line
do
	surname=$(echo $line | cut -d, -f1 | cut -d' ' -f1)
	name=$(echo $line | cut -d, -f2)
	email=$(echo $line | cut -d, -f3)

	username=${name:0:1}_$surname
	username=${username,,}


	username=$(echo $username | iconv -f utf8 -t ascii//TRANSLIT)

	rm -rf /home/$username/ex01

done < ../../scripts/iso.csv 
