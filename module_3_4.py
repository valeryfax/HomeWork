
# def single_root_words (root_word, *other_words):
#     same_words = []
#     upper.slovo = root_word.
#
#     for slovo in other_words:
#         if root_word in slovo or slovo in root_word:
#             same_words.append(slovo)
#     print(same_words)

def single_root_words(root_word, *other_words):
    same_words = []

    upper_word = root_word.upper()
    for word in other_words:
        if upper_word  in  word.upper():
            same_words.append(word)
    print(same_words)
     







single_root_words( 'rich' , 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')








