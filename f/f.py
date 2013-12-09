# -*- encoding:utf-8 -*-
'''

'''

def filer(fname):
    with file(fname, 'r') as f:
        contents = f.read().strip().split('\n')
        count, contents = int(contents[0]), contents[1:]
    return count, contents


def arrange_keys(count, contents):
    alphabets = [a for a in 'abcdefghijklmnopqrstuvwxyz']
    j = 0
    all_overlaps, all_chars = [], []
    for i in xrange(count):
        num = int(contents[i + j])
        if i + j + num > len(contents):
            break
        result = extract_chars(contents, i, j)
        chars, overlap_chars = result if result else None
        chars.sort(key=lambda x: len(x))
        j += num
        all_overlaps.append(overlap_chars)
        all_chars.append(chars)
    all_chars.sort(key=lambda x: len(x))
    print all_chars


def extract_chars(contents, i, j):
    num = int(contents[i + j])
    sentences = contents[i+j+1: i+j+1+num]
    chars = []
    overlap_chars = []
    for sentence in sentences:
        if len(sentence) > 10:
            return False
        chars.append([word for word in sentence])
    for k in xrange(num-1):
        for l in xrange(1, num-k):
            overlap_char = set(chars[k]) & set(chars[k + l])
            if not overlap_char:
                continue
            for already_added in overlap_chars:
                if set(already_added).issuperset(overlap_char)\
                        or set(already_added).issubset(overlap_char):
                            break
            else:
                overlap_chars.append(overlap_char)
    print 'overlap_chars => ', overlap_chars
    print 'chars => ', chars
    return [chars, overlap_chars]

def main():
    fname = 'sample.txt'
    count, contents = filer(fname)
    results = arrange_keys(count, contents)
