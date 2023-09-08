# measure run time of program a
# Usage: ./measure.sh a

# open and clear file time1.txt
> time1.txt


time ./iter < input.txt > output1.txt >> time1.txt

# open and clear file time2.txt
> time2.txt

time ./recur < input.txt > output2.txt >> time2.txt

