
def to_ascii(a):
    x = [ord(c) for c in a]
    return(x)

def to_text(a):
    return( ''.join(map(chr, a)))