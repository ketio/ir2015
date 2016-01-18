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
	# if int(file_number) < 20:
		# if int(file_number) % 4 != 1:
			
	if class_name not in trainging_data:
		trainging_data[class_name] = list()
	trainging_data[class_name].append("%s_%s" % (class_name, file_number))

		# else:

		# 	testing_docs.append("%s_%s" % (class_name, file_number))

# print(trainging_data)
# print(testing_data)

# train result = (V, prior, condprob)	
train_result = naive_bayes.TrainMultinomialNB(trainging_data)



training_dir = "./training_result" 

import os
if not os.path.exists(training_dir):
	os.mkdir(training_dir)

v = open(training_dir+"/v.txt","w")
v_parse = ",".join(train_result[0])
v.write(v_parse.encode('utf-8'))
v.close()

prior = open(training_dir+"/prior.txt","w")
prior.write("class,prob\n")
for c, value in train_result[1].items():
	prior.write("%s,%.25f\n" % (c, value))

prior.close()

# condprob[t][_class]
condprob = open(training_dir+"/condprob.txt","w")
condprob.write("term,class,prob\n")
for t, cs in train_result[2].items():
	for c, value in cs.items():
		condprob.write("%s,%s,%.25f\n" % (t.encode("utf-8"), c, value))

'''
ffff = open("result.txt","w")

for term, cles in train_result[2].items():
	for cl, condprob in cles.items():
		oooo = "%s: %s : %f\n" % (term.encode('utf-8'), cl, condprob)
		ffff.write(oooo)

ffff.close()
'''