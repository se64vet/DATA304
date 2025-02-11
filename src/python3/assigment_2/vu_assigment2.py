

# Load text file to python
file_path = './paragraph.txt'
with open(file_path) as txt_file:
    text = txt_file.read()

    # 1. split text into sentences
    sentences = text.split('.')

    # 2. create a word list without whitespace or punctuation
    word_list = []
    for sentence in sentences:
        words = sentence.split()
        words = [w.strip(',.!').lower() for w in words]

        word_list += words
    
    # 3. create a set of words
    word_set = set(word_list)

    # 4. find hidden message
    indexes = [60, 26, 10, 10, 41, 35, 26, 44,48]
    message = ''
    for i in indexes:
        message += word_list[i][0]

    print('Number of sentences: ', len(sentences)) #10
    print('Unique word count: ', len(word_set)) #80
    print('Hidden message: ', message) #happycats