#!/bin/bash
python=python3
index=0
for i in */test*
do
    echo $i
    dir=$(dirname $i)
    fname=$(basename $i)
    (cd $dir && python $fname)
    declare "retval_$index"=$?
    index=$(($index+1))
done

test_result(){
    if [ "$1" = "0" ]; then echo "PASS"; else echo "FAIL"; fi
}

echo "Results: "
echo "-------------*****************--------------"
index=0
for i in */test*
do
    fname=$(basename $i)
    retval=retval_$index
    echo "$fname: " `test_result ${!retval}`
    index=$(($index+1))
done