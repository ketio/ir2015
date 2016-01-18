#coding=UTF-8
import csv 
import jieba
import jieba.posseg as pseg
import stopWords

def tokenizer(doc_string, parse = False):

	seg_list = list(jieba.cut(doc_string, cut_all=False))
	seg_list = stopWords.rmStopWords(seg_list)
	if parse:
	 	seg_list = ",".join(seg_list)
		seg_list = seg_list.encode("utf-8")

	return seg_list