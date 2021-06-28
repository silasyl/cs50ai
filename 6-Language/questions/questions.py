import string
import nltk
import sys
import os
import math

FILE_MATCHES = 1
SENTENCE_MATCHES = 1


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):
    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    dictionary = {}
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        with open(file_path) as f:
            content = f.read()
            dictionary[file] = content

    return dictionary


def tokenize(document):
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.

    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    document = nltk.word_tokenize(document)
    words = []
    for w in document:
        w = w.lower()
        if w not in string.punctuation:
            if w not in nltk.corpus.stopwords.words("english"):
                words.append(w)

    return words


def compute_idfs(documents):
    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.

    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    idfs = {}
    n_documents = len(documents)
    for filename in documents:
        for word in documents[filename]:
            if word not in idfs:
                f = sum(word in documents[file] for file in documents)
                idf = math.log(n_documents / f)
                idfs[word] = idf

    return idfs


def top_files(query, files, idfs, n):
    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    tfidfs = {}
    for file in files:
        tfidf = 0
        for word in query:
            if word in files[file]:
                tf = files[file].count(word)
                tfidf += tf * idfs[word]
        tfidfs[file] = tfidf

    filenames = dict(sorted(tfidfs.items(), key=lambda item: item[1], reverse=True))
    list = []
    for f in range(n):
        first, *filenames = filenames
        list.append(first)

    return list


def top_sentences(query, sentences, idfs, n):
    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    s_idfs = {}
    for sentence in sentences:
        idf = 0
        for word in query:
            if word in sentences[sentence]:
                idf += idfs[word]
        s_idfs[sentence] = idf

    sorted_sentences = dict(sorted(s_idfs.items(), key=lambda item: item[1], reverse=True))
    list = []
    for s in range(n):
        first, *sorted_sentences = sorted_sentences
        second, *rest = sorted_sentences
        if first == second:
            qtd1 = 0
            qtd2 = 0
            for word in query:
                if word in first:
                    qtd1 += 1
                if word in second:
                    qtd2 += 1
            qtd1 = qtd1 / len(first)
            qtd2 = qtd2 / len(second)
            if qtd1 >= qtd2:
                list.append(first)
                list.append(second)
                first, *sorted_sentences = sorted_sentences
            else:
                list.append(second)
                list.append(first)
                first, *sorted_sentences = sorted_sentences
        else:
            list.append(first)

    return list


if __name__ == "__main__":
    main()
