# -*- encoding:utf-8 -*-
'''

'''

def filer(fname):
    with file(fname, 'r') as f:
        contents = f.read().strip().split('\n')
        count, contents = int(contents[0]), contents[1:]
    return count, contents

def get_suspicious_person(count, contents):
    suspicous_persons = []
    j = 0
    for i in xrange(count):
        raw_sentence = contents[j].strip().split(' ')
        raw_sentence_length = \
                sum([len(word) for word in raw_sentence]) / float(len(raw_sentence))
        j += 1
        person_num = int(contents[j])
        j += 1
        sentences = {}
        for k in xrange(person_num):
            person, words = contents[j + k].split(':')
            words = words.strip().split(' ')
            avg_word_length = \
                    sum([len(word) for word in words]) / float(len(words))
            len_error = abs(raw_sentence_length - avg_word_length)
            sentences[person] = len_error
        j += person_num
        print sentences
        suspicous_person = min([(v, k) for k, v in sentences.items()])[1]
        suspicous_persons.append(suspicous_person)
    return suspicous_persons



    # for content in contents:
    #     if content.isdigit():
    #         if sentences:
    #             suspicous_person = min([(v, k) for k, v in sentences.items()])[1]
    #             suspicous_persons.append(suspicous_person)
    #         sentences = {}
    #     else:
    #         try:
    #             person, words = content.strip().split(':')
    #             words = words.split(' ')
    #             avg_word_length = \
    #                     sum([len(word) for word in words]) / float(len(words))
    #             max_word_length = max([len(word) for word in words])
    #             sentences[person] = abs(max_word_length - avg_word_length)
    #         except ValueError:
    #             pass
    # suspicous_person = min([(v, k) for k, v in sentences.items()])[1]
    # suspicous_persons.append(suspicous_person)
    # return suspicous_persons

def main():
    fname = 'input.txt'
    count, contents = filer(fname)
    suspicous_persons = get_suspicious_person(count, contents)
    text = ''
    for suspicous_person in suspicous_persons:
        text += suspicous_person + '\n'
    with file('output.txt', 'w') as f:
        f.write(text)

if __name__ == '__main__':
    main()
