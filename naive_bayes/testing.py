#coding=UTF-8
import collections
import naive_bayes
import csv
import tokenizer
import os

def NBtesting(doc_string):

	current_file_path = os.path.dirname(os.path.abspath(__file__))

	# total document number
	# documentCount = len(testing_docs)

	# result is a dictionary, used to store the testing result.
	# i.e `result` = { doc_1: class_of_doc_1, doc_2: class_of_doc_2,...}
	result = dict()

	classes = ["1", "2", "3", "5"]

	# (new_V, prior, condprob)
	#	condprob[t][_class] term,class,prob

	f_v = open(current_file_path+"/training_result/v.txt", "r")
	v = f_v.read().decode("utf-8").split(",")
	
	f_prior = open(current_file_path+"/training_result/prior.txt", "r")
	prior = dict()
	for row in csv.DictReader(f_prior):
		prior[row["class"]]=float(row["prob"])


	f_condprob = open(current_file_path+"/training_result/condprob.txt", "r")
	condprob = dict()
	for row in csv.DictReader(f_condprob):
		term = row["term"].decode("utf-8")
		_class = row["class"]
		prob = float(row["prob"])
		
		if term not in condprob:
			condprob[term]=dict()
		condprob[term][_class] = prob

	doc_terms = tokenizer.tokenizer(doc_string)
	
	result = naive_bayes.ApplyMultinomialNB(classes, v, prior, condprob, doc_terms)

	return result