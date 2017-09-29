# 192. Word Frequency
#
# Write a bash script to calculate the frequency of each word in a text file words.txt.
# 
# For simplicity sake, you may assume:
# 
# words.txt contains only lowercase characters and space ' ' characters.
# Each word must consist of lowercase characters only.
# Words are separated by one or more whitespace characters.
#
# For example, assume that words.txt has the following content:
# 
# the day is sunny the the
# the sunny is is
#
# Your script should output the following, sorted by descending frequency:
# the 4
# is 3
# sunny 2
# day 1
# Note:
# Don't worry about handling ties, it is guaranteed that each word's frequency count is unique.
# 
# [show hint]
# 
# Hint:
# Could you write it in one-line using Unix pipes?
# Read from the file words.txt and output the word frequency list to stdout.

cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -nr | awk '{print $2,$1}'
cat words.txt |  tr -s ' ' '\n' | sort | uniq -c | sort -rn | awk '{print $2" "$1}'

## Explain:

# tr -s: 使用指定字符串替换出现一次或者连续出现的目标字符串（把一个或多个连续空格用换行符代替）

# sort: 将单词从小到大排序

# uniq -c: uniq用来对连续出现的行去重，-c参数为计数

# sort -rn: -r 倒序排列， -n 按照数值大小排序

# awk '{ print $2, $1 }': 格式化输出，将每一行的内容用空格分隔成若干部分，$i为第i个部分。
