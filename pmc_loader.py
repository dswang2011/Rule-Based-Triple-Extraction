import re, glob
from html import unescape

def list_files(my_path):
    return glob.glob(my_path + '/*.nxml')

def get_abstract(s):
    res = re.findall(r"<abstract.*?</abstract.*?>",s)
    txts = []
    for e in res:
        txt = re.sub(r"<.*?>", " ", e.strip())
        txt = unescape(txt)
        txts.append(txt)
    return '.'.join(txts)

def get_title(s):
    res = re.findall(r"<article-title.*?</article-title.*?>",s)
    txts = []
    for e in res:
        txt = re.sub(r"<.*?>", " ", e.strip())
        txt = unescape(txt)
        return txt
    return '.'.join(txts)


def load_all_pmc(my_folder):
    """ read all PMC abstract of a folder
    :type my_folder: string 
    :rtype: dict -> {id: (abstract,title)}
    """
    files = list_files(my_folder)
    data = {}
    for f in files:
        # print(f)
        # start = f.rfind('\\')
        # end = f.rfind('.')
        # file_name = f[start+1:end]
        file_name = f[-15:-5]
        # print(file_name)
        res = []
        with open(f,"r") as handler:
            content = handler.read()
            res = get_abstract(content)
            title = get_title(content)
            data[file_name] = (content,title)
    return data


# test loader
if __name__ == "__main__":
    data = load_all_pmc("/home/vbd667/code/rule-based-extraction/causaly_assignment_Wang_Dongsheng")
    count = 0
    for file, content in data.items():
        count+=1

        print(str(count),'=====file: ', file, '\n')
        print(content)
        if count>1: break