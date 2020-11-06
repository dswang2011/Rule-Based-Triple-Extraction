 # -*- coding: utf-8 -*-



CAUSE_LABEL = 'CAUSE_LABEL'
TRIGGERS = [' results in ', ' result in ', ' cause of ', ' causes ',' cause ', ' leads to ', ' lead to ', ' inhibit ',' inhibits ', ]  # replace with label VERB_CAUSE


# O(m+n), rolling hash
def contains(text, keywords):
    """
    :type text: str
    :type keywords: str
    :rtype: int
    """
    # approach: use rolling hash, calculate new hash value from last one
    base = 401 # randomly choose a big enough prime number as base

    m = len(text)
    n = len(keywords)

    # hash function: (a_1)x^(n-1) + (a_2)x^(n-2) + ... + a_n
    def hashing(S):
        s = len(S)
        return sum([ord(S[i]) * (base ** (s - 1 - i)) for i in range(s)])

    # calculate new hash value by previous hash value
    # new_value = (H - (a_1)x^(n-1)) * x + a_(n+1)
    def rolling_hashing(old_hash, old_value, new_value):
        return (old_hash - ord(old_value) * (base ** (n - 1))) * base + ord(new_value)

    n_hash = hashing(keywords)
    m_hash = hashing(text[0:n]) # get hash for first substring

    # the pattern matches first substring
    if m_hash == n_hash:
        return 0

    for i in range(1, m - n + 1):
        m_hash = rolling_hashing(m_hash, text[i - 1], text[i + n - 1])
        if m_hash == n_hash:
            return i

    return -1


def write_to_file(file_path,content):
    with open(file_path,'a',encoding='utf8') as fw:
        fw.write(content)
        fw.write('\n')



