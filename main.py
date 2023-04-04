import re
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer


def open_file(book_name):
    with open(f"{book_name}", mode="r", encoding='utf-8') as file:
        return file.read()


def find_number_of_chapters(book):
    pattern = re.compile("Chapter \d+")
    match = re.findall(pattern, book)
    return len(match)


def matching_sentence(book, word):
    pattern = re.compile(f"[^.]*{word}[^.]*.")
    match = re.findall(pattern, book)

    for line in match:
        print("-> " + line)


def most_repetitive_word(book, top):
    nltk.download("stopwords")
    stop_words = stopwords.words("English")
    print(stop_words)
    book = book.lower()
    word_dict = dict()
    word_list = book.split()

    for word in word_list:
        if word not in stop_words:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

    word_count_list = [(value, key) for (key, value) in word_dict.items()]
    word_count_list.sort(reverse=True)
    print("Occurrence of words:", end="\n")
    for word in word_count_list[:int(top)]:
        print(f"{word[1]} -> {word[0]}")


def chapter_sentiment(book, chapter_no):
    pattern = re.compile("Chapter \d+")
    chapters = re.split(pattern, book)
    chapters = chapters[1:]
    nltk.download('vader_lexicon')
    sentiment_analyze = SentimentIntensityAnalyzer()
    sentiment_analyze_score = sentiment_analyze.polarity_scores(chapters[int(chapter_no)])
    if sentiment_analyze_score["pos"] > sentiment_analyze_score["neg"]:
        print(f"Chapter {chapter_no} has Positive Sentiment.")
    else:
        print(f"Chapter {chapter_no} has Negative Sentiment")


if __name__ == "__main__":
    book_path = input("Please enter book path and name -> ")
    book_text = open_file(book_path)
    chapters = find_number_of_chapters(book_text)
    print("------------------------------------------------------------")
    print(f"There are {chapters} chapters in this book.")
    print("------------------------------------------------------------")
    word_search = input("Enter which word would you like to search in this book -> ")
    print("------------------------------------------------------------")
    matching_sentence(book_text, word_search)
    print("------------------------------------------------------------")
    most_used_words = input("How many of top used words in this book would you like to see -> ")
    print("------------------------------------------------------------")
    most_repetitive_word(book_text, most_used_words)
    print("------------------------------------------------------------")
    chapter_no = input("Enter chapter number to find sentiment -> ")
    print("------------------------------------------------------------")
    chapter_sentiment(book_text, chapter_no)
