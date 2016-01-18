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
	file_number = f_name[1]
	if int(file_number) < 20:
		if int(file_number) % 2 == 1:
			
			if class_name not in trainging_data:
				trainging_data[class_name] = list()
			trainging_data[class_name].append("%s_%s" % (class_name, file_number))

		else:

			testing_docs.append("%s_%s" % (class_name, file_number))

# print(trainging_data)
# print(testing_data)

# train result = (V, prior, condprob)	
train_result = naive_bayes.TrainMultinomialNB(trainging_data)

ffff = open("result.txt","w")

for term, cles in train_result[2].items():
	for cl, condprob in cles.items():
		oooo = "%s: %s : %f\n" % (term.encode('utf-8'), cl, condprob)
		ffff.write(oooo)

ffff.close()

# total document number
documentCount = len(testing_docs)

# result is a dictionary, used to store the testing result.
# i.e `result` = { doc_1: class_of_doc_1, doc_2: class_of_doc_2,...}
result = dict()

# save all doucmnet of each class in training data to `all_training_document`
# all_training_document = list(int(d) for (_c, _ds) in classes_docs.iteritems() for d in _ds)

# test all doucment to except training documents
# for d in range(1, documentCount + 1):
# 	if d not in all_training_document:
# 		result[d] = naive_bayes.ApplyMultinomialNB(classes_docs, train_result[0], train_result[1], train_result[2], d)

for doc in testing_docs:
 	result[doc] = naive_bayes.ApplyMultinomialNB(trainging_data, train_result[0], train_result[1], train_result[2], doc)


# Let `term_df` sort by key(term) in dictionary order
result = collections.OrderedDict(sorted(result.items()))
output_data = open("output.txt", "w")

# print result
hit = dict()
hit["1"] = dict()
hit["1"]["hit"] = 0
hit["1"]["count"] = 0
hit["2"] = dict()
hit["2"]["hit"] = 0
hit["2"]["count"] = 0
hit["3"] = dict()
hit["3"]["hit"] = 0
hit["3"]["count"] = 0
hit["4"] = dict()
hit["4"]["hit"] = 0
hit["4"]["count"] = 0
hit["5"] = dict()
hit["5"]["hit"] = 0
hit["5"]["count"] = 0

for (doc_id,class_id) in result.iteritems():

	class_of_doc = (doc_id.replace("_"," ").split())[0]
	hit[class_of_doc]["count"] += 1
	if int(class_of_doc) == int(class_id):
		hit[class_id]["hit"] += 1

for c, value in hit.items():
	output_data.write("Hit Rate of %s: %s \ %s = %f\n" % (c,value["hit"], value["count"], float(value["hit"])/value["count"]))

output_data.write("doc_id\tclass_id\n" )
for (doc_id,class_id) in result.iteritems():		
	output_data.write("%s\t%s\n" % (doc_id, class_id))


