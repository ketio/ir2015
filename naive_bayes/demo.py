#coding=UTF-8
import collections
import naive_bayes
from os import listdir

fs = [f for f in listdir("./docs")]
trainging_data = dict()
testing_docs = list()

for f in fs:
	f_name = f.replace("_"," ").replace("."," ").split()
	class_name = f_name[0]
	if class_name == "4":
		continue

	file_number = f_name[1]
	# if int(file_number) > 10:
	# 	continue
	if int(file_number) % 2 != 1:
		
		if class_name not in trainging_data:
			trainging_data[class_name] = list()
		trainging_data[class_name].append("%s_%s" % (class_name, file_number))

	else:
		testing_docs.append("%s_%s" % (class_name, file_number))

# print(testing_docs)
# train result = (V, prior, condprob)	
train_result = naive_bayes.TrainMultinomialNB(trainging_data)

classes = ["1", "2", "3", "5"]


result=dict()
for doc in testing_docs:

	f = open("./docs/%s.txt" % doc, "r")
	terms = f.read().decode('utf-8')
	doc_terms = terms.split(",")
	f.close()	
	result[doc] = naive_bayes.ApplyMultinomialNB(
		classes, train_result[0], train_result[1], train_result[2], doc_terms)



result = collections.OrderedDict(sorted(result.items()))
# print(result)


ffff = open("./demo_result.txt","w")

hits = dict()
hits["ALL"] = dict()
hits["ALL"]["hit"] = 0
hits["ALL"]["count"] = 0

for doc_name, _class in result.items():
	class_of_doc = (doc_name.replace("_"," ").split())[0]
	if class_of_doc not in hits:
		hits[class_of_doc] = dict()
		hits[class_of_doc]["hit"] = 0
		hits[class_of_doc]["count"] = 0

	hits[class_of_doc]["count"] += 1
	hits["ALL"]["count"] += 1
	
	if class_of_doc == _class:
		hits[class_of_doc]["hit"] += 1
		hits["ALL"]["hit"] += 1

hits = collections.OrderedDict(sorted(hits.items()))

for key, value in hits.items():

	hit = int(value["hit"])
	count = int(value["count"])
	ffff.write("Hit Rate of %s :  %d / %d = %f\n" % (key, hit, count, float(hit)/count ))

for doc_name, _class in result.items():
	ffff.write("%s, %s\n" % (doc_name, _class))

ffff.close
