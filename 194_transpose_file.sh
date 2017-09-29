# 194. Transpose File
#
# Given a text file file.txt, transpose its content.
# 
# You may assume that each row has the same number of columns and each field is separated by the ' ' character.
# 
# For example, if file.txt has the following content:
# 
# name age
# alice 21
# ryan 30
# Output the following:
# 
# name alice ryan
# age 21 30

# read file
len=$(head -1 194_file.txt | wc -w)
len=$((len-1))

for i in $(seq 0 $len); do
    while read line; do
      #echo "$line"
      arr=($line)
      echo -n "${arr[$i]} "
    done < 194_file.txt
    echo
done


# awk
awk '
{
    for (i = 1; i <= NF; i++) {
        if(NR == 1) {
            s[i] = $i;
        } else {
            s[i] = s[i] " " $i;
        }
    }
}
END {
    for (i = 1; s[i] != ""; i++) {
        print s[i];
    }
}' file.txt

# 
while read -a line; do
    for ((i = 0; i < "${#line[@]}"; ++i)); do
        a[$i]="${a[$i]} ${line[$i]}"
        #echo ${line[$i]}
        #echo ${a[i]}

    done
done < file.txt

echo ------------------
for ((i = 0; i < ${#a[@]}; ++i)); do
    echo ${a[i]}
done
