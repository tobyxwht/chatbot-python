# new chatbot
import nltk
def first_greet():
    from nltk.corpus import opinion_lexicon
    negative_words = set(opinion_lexicon.negative())
    positive_words = set(opinion_lexicon.positive())

    bad_list = list(negative_words)
    good_list = list(positive_words)

    name = input(f"hi whats your name? ")
    feeling = input(f"hi, {name} how are you? ")

    while True:
        if feeling.lower() in bad_list:
            print("why arent you good? ")
            break
        elif feeling.lower() in good_list:
            print("glad to hear! ")
            break
first_greet()

