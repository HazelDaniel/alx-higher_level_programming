#!/bin/bash

for k in $(ls | grep -P '.*\.py')
do
	echo :$k:
	eval "./$k"
done
