#coding=UTF-8
# from terms_extracter.terms_extracter import terms_extracter
import math

# selectFeatures: Likelihood method 
# 	@V = [v1, v2, v3, ...]
# 	@classes_docs = { class1: [doc1, doc2,...], class2: [doc1', doc2',...],..}
# 	@de_v = { doc_1 :[v1, v2, v3,...], doc_2: [v1', v2', v3',...],...}
# 	@k = number
def selectFeatures(V, classes_docs, feature_class, ds_v, k):

	# save to all documment in each class to `all_document` 
	all_document = list(d for (_c, _ds) in classes_docs.iteritems() for d in _ds)
	
	# count total document number
	N = len(all_document)

	# `llr` is a dictionary to store result, each element is the score of certain term
	# i.e `llr` = { term1: point1, term2: point2,...}
	llr = list()

	_class_documents = classes_docs[feature_class]

	# culutate likelihood for every term in V
	for t in V:
		n11 = 0
		n10 = 0
		n01 = 0
		n00 = 0

		# go through all document
		for _d in all_document:

			# check if the document belong to the current class
			if _d in _class_documents:

				# check if term in document
				if t in ds_v[_d]:
					n11 += 1
				else:
					n10 += 1
			else:

				# check if term in document
				if t in ds_v[_d]:
					n01 += 1
				else:
					n00 += 1

		# calcuate llr
		A = float(n11+n01)/ N
		B = float(n11)/(n11+n10)
		C = float(n01)/(n01+n00)
		numerator = math.pow(A, n11)*math.pow(1-A, n10)*math.pow(A, n01)*math.pow(1-A, n00)
		denominator = math.pow(B, n11)*math.pow(1-B, n10)*math.pow(C, n01)*math.pow(1-C, n00)
		temp = -2.0 * math.log((numerator)/(denominator))
		
		llr.append((t, temp))

	new_V = list()

	# sort by score
	llr = sorted(llr, key=lambda x:x[1],reverse = True)

	# `new_v` is a list, storing top k score terms 

	for i in range(0,k):
		new_V.append(llr[i][0])

	return new_V

# Training
# 	@classes_docs = { class1: [doc1, doc2,...], class2: [doc1', doc2',...],..}
def TrainMultinomialNB(classes_docs, feature_class):
	
	# `V` is a set used to store Vocabularies in all documents of each class 
	V = set()

	# `N` is total number of documents in all classes 
	N = 0  

	# `de_v` is a dictionary used to store vocabularies in each doucment, where index is document id
	# ie `de_v` = { doc_1 :[v1, v2, v3,...], doc_2: [v1', v2', v3',...],...}
	ds_v = dict()

	# go through each class
	for _class, documents in classes_docs.iteritems():

		# sum up document number is each class
		N = N + len(documents)

		# go through documents in each class to extract terms
		for document in documents:

			f = open("./docs/%s.txt" % document, "r")
			terms = f.read().decode('utf-8')
			ds_v[document] = terms.split(",")
			V.update(ds_v[document])
	
	# `prior` is a dictionary to store prior of each class
	# i.e `prior` = {class1: prior1, class2: prior2,...}
	prior = dict()

	# `condrob` is a two dimensional dictionary, storing condprob of each term in each class
	# i.e `condrob` = { term1:{class1: condprob1_1, class2: condprob1_2,...}, term2:{...},...}
	condprob = dict()

	# do select feature
	new_V = selectFeatures(V, classes_docs, feature_class, ds_v, 100)
	# new_V = V

	# go through each class
	for _class, documents in classes_docs.iteritems():
		
		# count doucument numbers in current class
		N_c = len(documents)

		# calcuate prior of current class 
		prior[_class] = float(N_c) / N

		# `text_c` is used to store all terms in doucments of current class 
		text_c = list()
		for document in documents:
			text_c = text_c + ds_v[document]

		# `T_ct` is used to store the frequency of each term in `new_V` appearing in `text_c`
		T_ct = dict()
		for t in new_V:
			T_ct[t] = text_c.count(t)

		# calcuate condprob
		denominator = len(text_c) + len(new_V)
		for t in new_V:

			if t not in condprob:
				condprob[t] = dict()

			condprob[t][_class] = float(T_ct[t] + 1) / denominator

	# return result
	return (new_V, prior, condprob)


# Testing
# 	@classes_docs = { class1: [doc1, doc2,...], class2: [doc1', doc2',...],..}
# 	@V = [v1, v2, v3, ...]
#	@prior = {class1: prior1, class2: prior2,...}
#	@condrob = { term1:{class1: condprob1_1, class2: condprob1_2,...}, term2:{...},...}
#	@d = test document id
def ApplyMultinomialNB(classes_docs, V, prior, condprob, d):

	# extract terms of doucument d
	f = open("./docs/%s.txt" % d, "r")
	terms = f.read().decode('utf-8')
	W = terms.split(",")
			
	# score is a dictionary to record the score of each class
	score = dict()

	# go through all class
	for _class, documents in classes_docs.iteritems():
		
		score[_class] = math.log(prior[_class])
		for t in W:
			
			if t in condprob:
				print(condprob[t])

				score[_class] += math.log( condprob[t][_class] )

	#return the class with bigger score
	return max(score, key=score.get)

