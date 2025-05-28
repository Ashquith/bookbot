def wordcounter(contents):
    wordcount = len(contents.split())  
    return wordcount

def charactercounter(contents):
    listedchars = list(contents)
    dict = {}
    for c in listedchars:
        c = c.lower()
        if c in dict:
            dict[c] += 1
        else:
            dict[c] = 1
    return dict

def sort_on(dict):
    return dict["num"]

def sorter(unsorted_dict):
    sorted_dict = []
    
    for c in unsorted_dict:
        n = unsorted_dict[c]
        if c.isalpha():
            dict = {"char" : c, "num" : n}
            sorted_dict.append(dict)

    
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict