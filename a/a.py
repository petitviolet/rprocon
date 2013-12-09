# -*- encoding:utf-8 -*-
'''

'''

def filer(fname):
    with file(fname, 'r') as f:
        contents = f.read().strip().split('\n')
    problems = []
    # counts = contents[0]
    for content in contents[2::2]:
        problems.append(content.strip().split(' '))
    return problems

def adder(numbers):
    row_num = {}
    max_num = 0
    for number in numbers:
        row = number[0]
        row_num.setdefault(row, 0)
        row_num[row] += int(number)
        max_num = max(max_num, row_num[row])
    return max_num

def main():
    fname = 'input.txt'
    problems = filer(fname)
    results = [adder(nums) for nums in problems]
    text = ''
    for result in results:
        text += str(result) + '\n'
    with file('output.txt', 'w') as f:
        f.write(text)
    print results

if __name__ == '__main__':
    main()
