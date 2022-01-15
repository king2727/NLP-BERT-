def make_chain(textsz):
    index = 1
    chain = {}
    for text in textsz:
        words = text.split()
        for word in words[1:]:
            key = words[index-1]
            