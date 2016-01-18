#coding=UTF-8
import csv 
import jieba
import jieba.posseg as pseg
import stopWords
import tokenizer
jieba.set_dictionary('./dict/dict.txt.big')
JUSKY_NAME = "./JUKSY.csv"
PTT01_NAME = "./PTT01.csv"
FUNNYJOKE_NAME = "./FUNNYJOKE.csv"
BUZZHAND_NAME = "./BUZZHAND.csv"
 
file_list = list()
jusky = open(JUSKY_NAME, 'r')  
ptt01 = open(PTT01_NAME, 'r')  
funnyjoke = open(FUNNYJOKE_NAME, 'r')  
buzzhand = open(BUZZHAND_NAME, 'r')  
file_list.append(jusky)
file_list.append(ptt01)
file_list.append(funnyjoke)
file_list.append(buzzhand)

# for row in csv.reader(f):  
#	print (r"%s" %row['class'])  
data = dict()
data["1"] = list()
data["2"] = list()
data["3"] = list()
data["4"] = list()
data["5"] = list()

for elem in file_list:
	for row in csv.DictReader(elem):
		if row["class_code"] in data:
			data[row["class_code"]].append(row["content"])
	elem.close()

import os
if not os.path.exists('./docs'):
	os.mkdir('./docs')


i = 0
class_doc_counter = dict()
for key, docs in data.items():
	if key not in class_doc_counter:
		class_doc_counter[key] = 0
	
	for doc in docs:
		seg_list_parse = tokenizer.tokenizer(doc, True)
		
		class_doc_counter[key] += 1

		# print result
		output_data = open("./docs/%d_%03d.txt" %(int(key), int(class_doc_counter[key])), "w" )
		output_data.write(seg_list_parse)