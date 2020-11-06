 # -*- coding: utf-8 -*-

from stanfordcorenlp import StanfordCoreNLP
import numpy as np
import nltk
from nltk.corpus import stopwords
import re,random



"""
nlp.pos_tag(sentence) -> to get a list of pos tags

"""


# get token entity
def get_token_block_tree(nlp,text,top_K_tokens=[],customized_tokens=[]):
	text_tokens = []
	# sentences = re.split('[.|?|!]',text)
	sentences = nltk.sent_tokenize(text)
	for sent in sentences:
		if len(sent.strip())<4:
			continue
		if len(sent)>700:
			sent=sent[:695]
		# end punctuation
		end_punctuation = sent.strip()[-1]
		if end_punctuation not in ['.','!','?']:
			end_punctuation='.'
			sent = sent + end_punctuation
		# build tree
		layer2node_list = build_tree(nlp,sent)
		if layer2node_list==None:
			return top_K_tokens
		# tree pickup
		picked_tokens = tree_pick(layer2node_list,nlp,sent,entity_indexes=[],key_tokens = top_K_tokens+customized_tokens)
		if end_punctuation not in picked_tokens:
			picked_tokens.append(end_punctuation)

		text_tokens+=picked_tokens
	return text_tokens

def get_token_POS(nlp,sentence):
	token_tag_list = nlp.pos_tag(sentence)
	token_list,pos_lookup = [],{}
	for i in range(len(token_tag_list)):
		token,pos = token_tag_list[i]
		token_list.append(token)
		pos_lookup[i]=pos
	return token_list,pos_lookup


def get_token_dep(nlp,text):
	"""get the token list and dependency label dict for a input text
	Args:
		nlp: prepared StanfordParser object
		text: input text string, usually a sentence
	Return:
		token_list: a list of tokens
		dep_lookup: a dict of mapping, index:dependency_label
	"""
	token_list = nlp.word_tokenize(text)
	dep_lookup = {}
	tuple_list = nlp.dependency_parse(text)
	for tag,point,index in tuple_list:
		dep_lookup[index-1]=tag
	return token_list,dep_lookup


def write_file(file,content):
	"""write content to file 
	"""
	with open(file,'a',encoding='utf8') as fw:
		fw.write(content)
		fw.write('\n')




# test some parsing
if __name__ == '__main__':

	###### test #####
	texts=[
		'The encapsulation of rifampicin leads to a reduction of the Mycobacterium smegmatis inside macrophages.',  # The ** leads to a reduction of the *** END
		'The Norwalk virus is the prototype virus that causes epidemic gastroenteritis infecting predominantly older children and adults.', # The ** is the ** that causes *** END
		'It is widely agreed that the exposure to ambient air pollution may cause serious respiratory illnesses and that weather conditions may also contribute to the seriousness.', # the ** may cause *** END
		'In this report, ribavirin was shown to inhibit SARS coronavirus replication in five different cell types of animal or human origin at therapeutically achievable concentrations.',
		'Chronic hepatitis B virus infection is a major cause of chronic hepatitis, cirrhosis, and hepatocellular carcinoma worldwide.'
	]

	nlp = StanfordCoreNLP(r'/home/vbd667/resources/stanford-corenlp-full-2018-10-05')

	for txt in texts:
		print('=====================================')
		# fulltext

		token_list,pos_lookup = get_tokens_POS(nlp,txt)
		# print(token_list)
		print([pos_lookup[i] for i in range(len(token_list))])

		# label_sequence = []
		# token_list,dep_lookup = get_token_dep(nlp,txt)
		# for i,token in enumerate(token_list):
		# 	label_sequence.append((i,token, dep_lookup[i]))
		# 	print(token,' dep: ', dep_lookup[i])
		# print(label_sequence)
		# tokens = [token for index,token,dep in label_sequence]
		# deps = [dep for index,token,dep in label_sequence]
		# write_file('rules.txt', str(label_sequence))
		# write_file('rules.txt', str(tokens))
		# write_file('rules.txt', str(deps))
		# write_file('rules.txt', '\n')

		print('\n')

	nlp.close()
