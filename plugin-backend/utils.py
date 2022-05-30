import re 

def clean_code(code):
    # Remove \r and \n
    code = code.replace("\r", "")
    code = code.replace("\n", "")

    # Remove comments
    code = removeComments(code)

    return code

# From: 
def removeComments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurrences streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurrence single-line comments (//COMMENT\n ) from string
    return string


def flatten_list(zipped):
    return [item for sublist in zipped for item in sublist] # Flatten list

def remove_duplicate_labels(labels):
    d = {}
    for x, y in labels:
        if y not in d:
            d[y] = x
    
    return [(k, v) for k, v in d.items()]

