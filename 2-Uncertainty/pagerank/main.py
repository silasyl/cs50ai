import os
import random
import re
import sys
import numpy

DAMPING = 0.85
SAMPLES = 10000

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])

    # corpus = {"1.html": {"2.html", "3.html"}, "2.html": {}, "3.html": {"2.html"}}
    # corpus = {"1.html": {"2.html"}, "2.html": {}, "3.html": {}}

    res = iterate_pagerank(corpus,DAMPING)
    print(res)


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    probability = dict()

    # Damping factor:
    if (len(corpus[page]) == 0):
        for pages in corpus.keys():
            probability[pages] = 1/len(corpus)
        return probability
    link_prob = damping_factor / len(corpus[page])
    for link in corpus[page]:
        probability[link] = link_prob

    # 1 - Damping factor
    all_prob = (1 - damping_factor) / len(corpus)
    for pages in corpus.keys():
        if pages in probability:
            probability[pages] = probability[pages] + all_prob
        else:
            probability[pages] = all_prob

    return probability


def sample_pagerank(corpus, damping_factor, n):
    page_rank = dict()
    for pages in corpus.keys():
        page_rank[pages] = 0

    page = random.choice(list(corpus.keys()))
    page_rank[page] += 1

    for i in range(n-1):
        sample = transition_model(corpus,page,damping_factor)
        sample_page = list(sample.keys())
        sample_prob = list(sample.values())
        page = numpy.random.choice(sample_page, p=sample_prob)
        page_rank[page] += 1

    for pages in corpus.keys():
        page_rank[pages] /= n

    print(page_rank)


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_rank = dict()
    for pages in corpus.keys():
        page_rank[pages] = 1 / len(corpus)
    delta_page = dict()
    delta = 1
    while delta > 0.001:
        for page in corpus.keys():
            new_rank = calculate_pr(corpus, page, damping_factor, page_rank)
            delta_page[page] = abs(new_rank - page_rank[page])
            delta = max(delta_page.values())
            if delta < 0.001:
                break
            page_rank[page] = new_rank
        print(delta)
    return page_rank


def calculate_pr(corpus, p, d, pr):
    sum = 0
    for i in corpus.keys():
        if p in corpus[i]:
            sum += pr[i] / len(corpus[i])
    probability = (1 - d) / len(corpus) + d * sum
    return probability



if __name__ == "__main__":
    main()
