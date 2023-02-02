def unique_words(file):
    data = file.read()
    words = data.split(' ')
    resulted_words = []
    unrepeated_words= []
    for word in words:
        if word in resulted_words and word not in unrepeated_words:
            unrepeated_words.append(word)
        else:
            resulted_words.append(word)
    return unrepeated_words

def count_the_article(file):
    data = file.read()
    words = data.split()
    return len(words)

def sorted_words(file):
    data = file.read()
    words = data.split()
    words.sort(key=lambda item: (-len(item), item))
    return words


def character_word_count(file):
    data = file.read()
    words = data.split()
    counts = dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

def starts_with_vow(file):
    data = file.read()
    words = data.split()
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    vowel_words = []
    for word in words:
        if word.startswith(vowels):
            vowel_words.append(word)
    return vowel_words

def rare_words(file,dictt,book_words):
    data = file.read()
    words = data.split()
    book_words.append(words)
    list_rare = (x for x in words if x not in dictt)
    return list(list_rare)                                                                                                                                                                                                                                                                                  

def unused_word(book_words,dictt):
    list_rare = (x for x in dictt if x not in book_words)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    list(list_rare)                                                                            
    unused_dict = dict()
    for word in list_rare:
        if word in unused_dict:
            unused_dict[word] += 1                                                                                                                                                                  
        else:
            unused_dict[word] = 1
    return unused_dict


dictt = []
book_words = []
with open("/home/sweta/openbook1-SwetaSukul/20k.txt","r") as localfile:
    data = localfile.read()
    dictt = data.split()

with open("/home/sweta/openbook1-SwetaSukul/Book1.txt","r") as localfile:
    print(unique_words(localfile))
with open("/home/sweta/openbook1-SwetaSukul/Book1.txt","r") as localfile:
    print("Number of words in book = "+ str(count_the_article(localfile)))
with open("/home/sweta/openbook1-SwetaSukul/Book1.txt","r") as localfile:
    print(sorted_words(localfile))
with open("/home/sweta/openbook1-SwetaSukul/Book1.txt","r") as localfile:
    print(character_word_countlocalfile(localfile))
with open("/home/sweta/openbook1-SwetaSukul/Book1.txt","r") as localfile:
    print(starts_with_vow(localfile))
with open("/home/sweta/openbook1-SwetaSukul/Book1.txt","r") as localfile:                                                                                                                                
    print(rare_words(localfile,dictt,book_words))
   

with open("/home/sweta/openbook1-SwetaSukul/Book2.txt","r") as localfile:
    print(rare_words(localfile,dictt,book_words))

with open("/home/sweta/openbook1-SwetaSukul/Book3.txt","r") as localfile:
    print(rare_words(localfile,dictt,book_words))

print(unused_word(book_words,dictt))