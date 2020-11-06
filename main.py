 # -*- coding: utf-8 -*-

import numpy as np
import pmc_loader
from spo import SPO_Extractor
import utils
import argparse

"""
main function.
"""


def test_five_sentences(args):
	# Test
	a = 'The encapsulation of rifampicin leads to a reduction of the Mycobacterium smegmatis inside macrophages.'  # The ** leads to a reduction of the *** END
	b = 'The Norwalk virus is the prototype virus that causes epidemic gastroenteritis infecting predominantly older children and adults.' # The ** is the ** that causes *** END
	c = 'It is widely agreed that the exposure to ambient air pollution may cause serious respiratory illnesses and that weather conditions may also contribute to the seriousness.' # the ** may cause *** END
	d = 'In this report, ribavirin was shown to inhibit SARS coronavirus replication in five different cell types of animal or human origin at therapeutically achievable concentrations.'
	e = 'Chronic hepatitis B virus infection is a major cause of chronic hepatitis, cirrhosis, and hepatocellular carcinoma worldwide.'

	extractor = SPO_Extractor(args)
	print('a:',extractor.extract_spo_sentence(a))
	print('b:', extractor.extract_spo_sentence(b))
	print('c:',extractor.extract_spo_sentence(c))
	print('d:', extractor.extract_spo_sentence(d))
	print('e:',extractor.extract_spo_sentence(e))

def extract_from_folder(args):
	data = pmc_loader.load_all_pmc(args.data_path)
	extractor = SPO_Extractor(args)
	count = 0
	for pmc_id, (abstract,title) in data.items():
		SPOs = extractor.extract_spo_text(abstract+'.'+title)
		if SPOs:
			# for spo in SPOs:
			# 	print(spo)
			utils.write_to_file(args.output_file,title.strip() +','+pmc_id + ','+pmc_id+'.nxml' +  ','+str(SPOs))
			
		# break
			# count+=1
			# if count>10: break



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='run the main extraction.')
	parser.add_argument('--data_path', default="/home/vbd667/code/rule-based-extraction/PMD")
	parser.add_argument('--corenlp_path', default="/home/vbd667/resources/stanford-corenlp-full-2018-10-05")
	parser.add_argument('--output_file', default = "spo_output.txt")
	parser.add_argument('--run_mode', default = "test")	# or extract
	args = parser.parse_args()

	if args.run_mode == 'test':
		test_five_sentences(args)
	if args.run_mode == 'extract':
		extract_from_folder(args)

