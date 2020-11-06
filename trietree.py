 # -*- coding: utf-8 -*-

"""
This is to create a trie tree to store the rules. Given a syntactic dependency patterns, it saves a unique path in this trie tree for future searching.  
There is a strong benefit in terms of time complexity. I.e., if we have a rule pattern with maximum length of 15, search onet time takes. O(15*N).
"""


# generalized cause label
CAUSE_LABEL = 'CAUSE_LABEL'

class Trie(object):

    def __init__(self):
        self.trie = {}
        """
        Initialize the rules here, 5 rules first
        """
        # rule1= ['det', 'nsubj', 'case', 'nmod', CAUSE_LABEL , 'det', 'nmod', 'case', 'det', 'compound', 'nmod', 'case']
        ans1 = [[0,1,2,3],4,[9,10]]
        # rule2 = ['det', 'compound', 'nsubj', 'cop', 'det', 'compound', 'ROOT','nsubj', CAUSE_LABEL, 'amod', 'dobj', 'acl'] 
        ans2  = [[0,1,2], 8, [9,10]]
        # rule3 = ['det', 'nsubj', 'case', 'amod', 'compound', 'nmod', 'aux', CAUSE_LABEL, 'amod', 'amod', 'dobj', 'cc']  
        ans3 = [[1,2,3,4,5],7, [8,9,10]]
        # rule4 = ['nsubjpass', 'auxpass', 'ROOT', 'mark', CAUSE_LABEL, 'compound', 'compound','dobj'] 
        ans4 = [[0],4,[5,6]]
        # rule5 = ['amod', 'compound', 'compound', 'compound', 'nsubj', 'cop', 'det', 'amod', CAUSE_LABEL, 'amod', 'nmod', 'punct', 'conj', 'punct', 'cc', 'amod', 'conj','advmod']
        ans5 = [[0,1,2,3,4],8, [9,10],[12],[15,16]]

        # self.add_dep_rules(rule1,ans1)
        # self.add_dep_rules(rule2,ans2)
        # self.add_dep_rules(rule3,ans2)
        # self.add_dep_rules(rule4,ans3)
        # self.add_dep_rules(rule5,ans3)


        # POS rules 
        prule1 = ['DT', 'NN', 'IN', 'NN', CAUSE_LABEL, 'DT', 'NN', 'IN', 'DT', 'NN', 'NN', 'IN']
        prule2 = ['DT', 'NNP', 'NN', 'VBZ', 'DT', 'NN', 'NN', 'WDT', CAUSE_LABEL , 'JJ', 'NN', 'VBG']
        prule3 = ['DT', 'NN', 'TO', 'JJ', 'NN', 'NN', 'MD', CAUSE_LABEL , 'JJ', 'JJ', 'NNS', 'CC']
        prule4 = ['NNP', 'VBD', 'VBN', 'TO', CAUSE_LABEL, 'NN', 'NN', 'NN','IN']
        prule5 = ['JJ', 'NN', 'NN', 'NN', 'NN', 'VBZ', 'DT', 'JJ', CAUSE_LABEL, 'JJ', 'NN', ',', 'NN', ',', 'CC', 'JJ', 'NN', 'RB']
        
        prule6 = ['NN', 'NN', 'MD', CAUSE_LABEL, 'DT', 'JJR', 'NN', 'NN', ',']
        ans6 = [[0,1],3,[5,6,7]]
        prule7 = ['NN', 'NNS', 'MD', CAUSE_LABEL, 'NN', 'IN', 'JJR', 'NNS', 'IN']
        ans7 = [[0,1],3,[4,5,6,7]]
        prule8 = ['FW', 'FW', 'VBZ', 'DT', 'JJ', 'NN', 'WDT', CAUSE_LABEL, 'NN', 'IN']
        ans8 = [[0,1],7,[8]]
        prule9 = [ 'NN', 'NN', 'NN', CAUSE_LABEL, 'JJ', 'NNP', 'NN', ',']
        ans9 = [[0,1,2],3,[5,6]]
        prule10 = ['NNP', CAUSE_LABEL, 'JJ', 'NN', 'WDT']
        ans10 = [[0],1,[2,3]]
        prule11 = ['NN', 'NN', CAUSE_LABEL, 'DT', 'RBS', 'JJ', 'NNS', 'IN']
        ans11 = [[0,1],2,[6]]
        prule12 = ['JJ', 'NN', 'IN', 'NN', 'NN', CAUSE_LABEL, 'DT', 'JJ', 'JJ', 'JJ', 'NN', 'IN']
        ans12 = [[0,1,2,3,4],5,[7,8,9,10]]
        prule13 = ['NNP', 'NN', CAUSE_LABEL, 'JJ', 'NN', 'JJ', 'JJ', 'NN', '-LRB-', 'NN', '-RRB-', '.']
        ans13 = [[0,1],2,[3,4,5,6,7,8,9,10]]
        prule14 = ['IN', 'JJ', 'JJ', 'NN', '-LRB-', 'NN', '-RRB-', CAUSE_LABEL, 'JJ', 'NN', 'IN']
        ans14 = [[1,2,3,4,5,6],7,[8,9]]
        prule15 = ['NN', CAUSE_LABEL, 'JJ', 'NN', 'NN', ',']
        ans15 = [[0],1,[3,4]]
        prule16 = ['NNP','HYPH','NNP','NNP',CAUSE_LABEL, 'JJ','NN','NNS','CC']
        ans16 = [[0,1,2,3],4,[5,6,7]]

        self.add_pos_rules(prule1,ans1)
        self.add_pos_rules(prule2,ans2)
        self.add_pos_rules(prule3,ans3)
        self.add_pos_rules(prule4,ans4)
        self.add_pos_rules(prule5,ans5)
        self.add_pos_rules(prule6,ans6)
        self.add_pos_rules(prule7,ans7)
        self.add_pos_rules(prule8,ans8)
        self.add_pos_rules(prule9,ans9)
        self.add_pos_rules(prule10,ans10)
        self.add_pos_rules(prule11,ans11)
        self.add_pos_rules(prule12,ans12)
        self.add_pos_rules(prule13,ans13)
        self.add_pos_rules(prule14,ans14)
        self.add_pos_rules(prule15,ans15)
        self.add_pos_rules(prule16,ans16)

    def add_pos_rules(self,rule,ans):
        end_tokens = ['IN','VBG','CC','IN','RB',',','.','WDT']
        for new_end in end_tokens:
            self.insert(rule[:-1]+[new_end],ans)

    def add_dep_rules(self,rule,ans):
        end_tokens = ['acl','punct','cc','advmod','case']
        for new_end in end_tokens:
            self.insert(rule[:-1]+[new_end],ans) 	


    def insert(self, pattern, ans):
        """Inserts a rule pattern into the trie.
        :type pattern: list
        :rtype: None
        """
        trie = self.trie
        for label in pattern:
            if label not in trie:
                trie[label] = {}
            trie = trie[label]
        trie['*']=ans


    def search(self, pattern):
        """Search and returns if the pattern matches a rule in the trie.
        :type pattern: list
        :rtype: result
        """
        res = []
        trie = self.trie
        for label in pattern:
            if label not in trie:
                break
            trie = trie[label]
            # find the longest path when found a pattern
            if '*' in trie:
                res = trie['*']
        return res




