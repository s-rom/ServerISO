#!/bin/bash



if [[ $# -ne 1 ]]; then
	echo "Usage: ./this ex0?"
	exit
fi

while read -r line
do
	surname=$(echo $line | cut -d, -f1 | cut -d' ' -f1)
	name=$(echo $line | cut -d, -f2)
	email=$(echo $line | cut -d, -f3)

	username=${name:0:1}_$surname
	username=${username,,}

	pass=123

	username=$(echo $username | iconv -f utf8 -t ascii//TRANSLIT)
	echo $username
		
	ex=$1
    cp -r $ex/ /home/$username/ejercicios_grep/
    chown -R $username /home/$username/ejercicios_grep/$ex/
    chgrp -R $username /home/$username/ejercicios_grep/$ex/
    chmod -R u+rwx /home/$username/ejercicios_grep/


done < ../../scripts/iso.csv 
