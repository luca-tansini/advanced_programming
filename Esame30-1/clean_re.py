import re

reg = re.compile("(?P<matched>((RE|AW|CHI|CH-S|REF): ?)+)",re.I)
wasreg = re.compile("\((?P<was>WAS: ?).*\)",re.I)

def wasspaced(str):
    m = re.search(wasreg,str)
    if(m):
        return str.replace(m.group('was'),'WAS: ')
    else:
        return str

def fixre(str):
    m = re.search(reg,str)
    if(m):
        parts = str.split(m.group('matched'))
        return parts[0] + 'Re: ' + re_subject(m.group('matched').join(parts[1:]))
    else:
        return str

def re_subject(str):
    return wasspaced(fixre(str))
