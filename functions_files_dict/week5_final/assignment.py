punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def strip_punctuation(str1):
    """
    This function is used to remove punctuation characters in a 
    string.
    Return type: str
    """
    answer = str1
    for pun in punctuation_chars:
        answer = answer.replace(pun, '')
    return answer

def get_pos(sentence):
    """
    This function is used to count the positive words.
    Return type: int
    """
    answer = 0
    sentence = strip_punctuation(sentence)
    words = sentence.split()
    lookup = set(positive_words) # Create a hash set to speed up lookup
    for word in words:
        if word.lower() in lookup:
            answer += 1
    return answer

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(sentence):
    """
    This function is used to count the negative words.
    Return type: int
    """
    answer = 0
    sentence = strip_punctuation(sentence)
    words = sentence.split()
    lookup = set(negative_words)
    for word in words:
        if word.lower() in lookup:
            answer += 1
    return answer

def generate_csv_content():
    """
    This function is used to generate the content of csv file
    Return type: str
    """
    result = []
    i = 0
    with open("project_twitter_data.csv", "r") as fd:
        for line in fd:
            if i > 0:
                contents = line.split(',')
                text, retweets, replies = contents[0], contents[1], contents[2].strip()
                positive_score = get_pos(line)
                negative_score = get_neg(line)
                net_score = positive_score - negative_score
                result.append([retweets, replies, positive_score, negative_score, net_score])
            else:
                result.append(["Number of Retweets", " Number of Replies", " Positive Score", " Negative Score", " Net Score"])
            i += 1
    return result

def write_csv(result):
    """
    This function is used to write the csv file
    Return type: None
    """
    with open("resulting_data.csv", "w") as fd:
        for line in result:
            line = [str(x) for x  in line]
            line_content = ','.join(line) + '\n'
            fd.write(line_content)
        fd.close()

if __name__ == '__main__':
    result = generate_csv_content()
    write_csv(result)
