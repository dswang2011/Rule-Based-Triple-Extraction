
# Overview
This is a small rule-based SPO extraction project. It extracts CAUSE EFFECT triples from free texts. The extraction is mainly based on a trie tree, constructed from all rule patterns. 


# Lib Requirements
pip install numpy
pip install stanfordcorenlp
pip install nltk


# Brief explanation of the implementaion
1. trie tree rule side:
	1) Extract rules by generalizing the sequencial of patterns: (greedy) tags + keyword + tags + (end_tag) 
	2) Input the rules into a trie tree for future searching of rules

2. free text side
	1) I list a couple of key words as relations of CAUSE EFFECT triggers, and use rolling hash algorithm to effectively matching them from texts. 
	2) if triggered, generating sequencial of tag patterns and search the rules in a greedy way


# discussion
tags can be POS or dependency labels. I believe the POS tags + keywords is the best way to generalize rules; 


# python file explanation
1. utils.py: has the method contains() is used to match keywords
2. trietree.py: is to initialize, insert and search a rules or pattern
3. spo.py: has the most essential methods for the extraction of SPOs for input sentence or text.


# How to run (two use cases)
Before that, you need to set basic paras: change the parameters of input output and corenlp path in main.py file, then

1. "python main.py --run_mode test", test the five cases, the extracted SPO will be printed directly on the console screen  
2. "python main,py --run_mode extract", extract all triples for XMLs, the output will be the file path you set. 


# Time complexity discuss for an input sentence
keyword trigger -> O(N+L)*K where N is the number of words, and L is the length of trigger keyword and K is number of keywords;
Trie tree search -> O(N^2) where N is number of words, usually we early stop the search either we found a rule or when it reaches the CAUSEL_LABEL

# Rule discuss
The recall is low, but the accuracy is good. Basically there are two ways to improve the coverage.
1) The rules are easy to generate. we can easily generate generalized patterns easily with some human annotation to generate rules.
2) Further generalize the rules to more generic version.

Personally I prefer the first solution because it is easier to generate rule patterns meanwhile annotation is not difficult. If we could accumulate certain amount of rules, it will improve recall while maintain high precision.

