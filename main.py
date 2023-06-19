import wikipediaapi


def read_titles(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


def get_article(title):
    wiki_wiki = wikipediaapi.Wikipedia('pl')
    page_py = wiki_wiki.page(title)
    if page_py.exists():
        return page_py.text
    else:
        return None


def letter_count():
    total_letter_count = 0
    article_count = 0

    for title in read_titles('small.txt'):
        article = get_article(title)
        print(article)
        if article:
            total_letter_count += len(article)
            article_count += 1

    average_letter_count = total_letter_count / article_count
    return average_letter_count


average_count = letter_count()
print("Średnia liczba liter na artykuł: ", average_count)
