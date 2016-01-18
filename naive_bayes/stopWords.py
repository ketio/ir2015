#coding=UTF-8
#	Stop Word List come from the website below
#	http://www.lextek.com/manuals/onix/stopwords1.html
#


words = ["的"," ", "，", "。", "在", "也", "、", "？", "▼", "'", "\"", "(","（","）" 
")", "...", "；", "「", "」", "《", "》", "了", "我", "你", "們", "~", 
"是", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
"O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "”", "“", "【", 
"】", "▶"]

def rmStopWords(oriList):

	result = list()

	for word in oriList:
		if word.encode("utf-8") not in words:
			result.append(word)

	return result

