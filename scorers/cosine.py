from collections import Counter
import math
import re


def cosine_score(text_1, text_2):
    '''Find cosine score betweet two strings.

    :info: http://upload.wikimedia.org/math/f/3/ 6/f369863aa2814d6e283f859986a1574d.png

    :type text_1: string
    :param text_1: first input string

    :type text_2: string
    :param text_2: second input string

    :rtype return: float value
    :returns: cousine score
    '''
    vector_1 = vectorize(text_1)
    vector_2 = vectorize(text_2)

    # make word intersection
    intersection = set(vector_1.keys()) & set(vector_2.keys())

    # find the vector
    numerator = sum([vector_1[value] * vector_2[value]
                     for value in intersection])

    # makes squared values of the frequency
    sum_1 = sum([vector_1[value]**2 for value in vector_1.keys()])
    sum_2 = sum([vector_2[value]**2 for value in vector_2.keys()])

    denominator = math.sqrt(sum_1) * math.sqrt(sum_2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def vectorize(text):
    '''Turn text to list of words.

    :rtype return: returns dict of Counter
    :returns: word frequency
    '''
    word_regexp = re.compile(ur'\w+')
    words = word_regexp.findall(text)
    return Counter(words)
