# -*- encoding:utf-8 -*-
'''

'''

def filer(fname):
    with file(fname, 'r') as f:
        contents = f.read().strip().split('\n')
        count, contents = int(contents[0]), contents[1:]
    return count, contents

def judge_include(count, contents):
    j = 0
    for i in xrange(count):
        num = int(contents[i + j])
        _boxes = contents[i + j + 1: i + j + 1 + num]
        boxes = []
        for box in _boxes:
            x, y, w, h = box.strip().split(' ')
            boxes.append([(x, y), (x + w, y + h)])
        del _boxes
        j += num
        box_num = len(boxes)
        union_boxes = set()
        for k in box_num:
            for l in box_num:
                A, B = boxes[k], boxes[l]
                if is_intersect(A, B):
                    union_box = [(min())]
                    union_boxes.add(set(A, B))



def is_intersect(A, B):
    for a, b in zip(zip(*A), zip(*B)):
        if not (min(a) <= max(b) and min(b) <= max(a)):
            return False
    return True
