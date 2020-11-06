 # -*- coding: utf-8 -*-


from stanfordcorenlp import StanfordCoreNLP
import CoreNLP
import utils
from trietree import Trie
import nltk


class SPO_Extractor(object):

	def __init__(self,args):
		self.args = args
		self.nlp = StanfordCoreNLP(args.corenlp_path)
		self.trieTree = Trie()

	# private function
	def detect_index(self,token_list,trig_words):
		for i in range(len(token_list)-1):
			if token_list[i:i+len(trig_words)]==trig_words:
				return [i,i+len(trig_words)-1]
		return [-1]

	def reform_dependency_patterns(self,sent, trig_str):
		""" reform a sentence into syntactic dependency tag list with CAUSE label inside
		:type sent: string
		:type trig_str: string
		:rtype: list,list,int
		"""
		trig_words = trig_str.split(' ')
		# reform the sent: dependency tag list, term list
		label_list, term_list = [],[]

		token_list,dep_lookup = CoreNLP.get_token_POS(self.nlp,sent)
		cause_index = self.detect_index(token_list,trig_words)

	 
		for i in range(len(token_list)):
			 # generalize cause label
			if i in cause_index:
				if i==cause_index[0]:
					label_list.append(utils.CAUSE_LABEL)
					term_list.append(trig_str)
			else:
				label_list.append(dep_lookup[i])
				term_list.append(token_list[i])
		return label_list,term_list,cause_index


	def extract_spo_sentence(self,sent):
		""" Extract SPO triples from a sentence
		:type sent: string
		:rtype: list
		"""
		res = []
		for trig in utils.TRIGGERS:
			index = utils.contains(sent,trig)
			if index>0: 
				# print(trig,'==> ',sent)
				# print('trigger word:',sent[index:index+len(trig)])
				trig_str = sent[index:index+len(trig)].strip()
				label_list,term_list,cause_index = self.reform_dependency_patterns(sent,trig_str)
				# print(label_list)
				# deliver label_list to trie tree to search;
				for i in range(0,cause_index[0]-1):
					ans = self.trieTree.search(label_list[i:])
					if ans:
						# print(ans)
						sub = ' '.join([term_list[i+j] for j in ans[0]])
						cause_label = term_list[i+ans[1]]
						for objx in ans[2:]:
							obj = ' '.join([term_list[i+j] for j in objx])
							# add to res
							res.append([sub,cause_label,obj])
						# gready stop, avoid shorter subject
						break
				# avoid repeat detection, e.g. cause of and cause
				break
		return res

	def extract_spo_text(self,text):
		res = []
		sentences = nltk.sent_tokenize(text)
		for sent in sentences: 
			temp_res = self.extract_spo_sentence(sent)
			if temp_res: res+=temp_res
		return res


# if __name__ == '__main__':
# 	# Test
# 	a = 'The encapsulation of rifampicin leads to a reduction of the Mycobacterium smegmatis inside macrophages.'  # The ** leads to a reduction of the *** END
# 	b = 'The Norwalk virus is the prototype virus that causes epidemic gastroenteritis infecting predominantly older children and adults.' # The ** is the ** that causes *** END
# 	c = 'It is widely agreed that the exposure to ambient air pollution may cause serious respiratory illnesses and that weather conditions may also contribute to the seriousness.' # the ** may cause *** END
# 	d = 'In this report, ribavirin was shown to inhibit SARS coronavirus replication in five different cell types of animal or human origin at therapeutically achievable concentrations.'
# 	e = 'Chronic hepatitis B virus infection is a major cause of chronic hepatitis, cirrhosis, and hepatocellular carcinoma worldwide.'

# 	extractor = SPO_Extractor()
# 	print('a:',extractor.extract_spo_sentence(a))
# 	print('b:', extractor.extract_spo_sentence(b))
# 	print('c:',extractor.extract_spo_sentence(c))
# 	print('d:', extractor.extract_spo_sentence(d))
# 	print('e:',extractor.extract_spo_sentence(e))

