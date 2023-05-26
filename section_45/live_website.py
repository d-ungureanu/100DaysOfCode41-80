from bs4 import BeautifulSoup
import requests

news_response = requests.get("https://news.ycombinator.com/news")

news_data = news_response.content

soup = BeautifulSoup(news_data, "html.parser")

# First article
# article_tag = soup.find(name="span", class_="titleline")
# article_text = article_tag.getText()
# print(article_text)
# article_link = article_tag.a.get("href")
# print(article_link)
# article_upvote = soup.find(name="span", class_="score").getText()
# print(article_upvote)

# All articles on the page
articles_tags = soup.find_all(name="span", class_="titleline")
articles_texts = []
articles_links = []
for article_tag in articles_tags:
    article_text = article_tag.getText()
    articles_texts.append(article_text)
    article_link = article_tag.a.get("href")
    articles_links.append(article_link)

articles_upvotes = [score.getText()
                    for score in soup.find_all(name="span", class_="score")]

articles_scores = [int(score.split(" ")[0]) for score in articles_upvotes]

max_score = max(articles_scores)
max_score_index = articles_scores.index(max_score)
print(
    f"TOP NEWS ITEM(with a score of {articles_scores[max_score_index]}) on HackerNews:")
print(articles_texts[max_score_index])
print(articles_links[max_score_index])

top3_news_items = sorted(
    zip(articles_scores, articles_texts, articles_links), reverse=True)[:3]
for entry in top3_news_items:
    print(entry)
