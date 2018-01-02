

def  Trimmer(sentence):
    # sentence = "I like scrambled eggs"
    lower = sentence.lower()
    mylist = lower.split()
    del mylist[0], mylist[0]
    b=" "
    all = b.join(mylist)
    return all