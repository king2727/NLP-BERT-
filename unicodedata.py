import unicodedata

# print(unicodedata.category(','), unicodedata.category('天'))

# 判断是否是汉字
def is_chinese(ch):
    if '\u4e00' <= ch <= '\u9fff':
        return True
    return False


# 判断是否是分隔符
def is_punctuation(ch):
    if ch in ("\n", "\t", "\r") or unicodedata.category(ch) in ("Zs", "Zp", "Zl"):
        return True
    return False


# 判断是否是标点符号
def is_biaodian(ch):
    cp = ord(ch)
    if (33 <= cp <= 47) or (58 <= cp <= 64) or (91 <= cp <= 96) or (123 <= cp <= 126):
        return True
    cat = unicodedata.category(ch)
    if cat.startswith('P'):
        return True
    return False


# 全角和半角转换
def strQ2B(ustring):
    rstring = ""
    for char in ustring:
        code = ord(char)
        if code == 12288:
            code = 32
        elif 65281 <= code <= 65374:
            code -= 65248
        rstring += chr(code)
    return rstring


