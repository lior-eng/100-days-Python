from bs4 import BeautifulSoup
import requests
import lxml # if html.parser doesn't work

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name= "span", class_= "titleline")
article_texts = []
article_links = []

for tag in articles:
    text = tag.getText()
    article_texts.append(text)
    link = tag.select_one(selector="a").get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_= "score")]
highest_upvoted_index = article_upvotes.index(max(article_upvotes))

print(article_texts[highest_upvoted_index])
print(article_links[highest_upvoted_index])
print(article_upvotes[highest_upvoted_index])










# with open("./Web Development Projects/Day-45/website.html",
#           mode= "r",
#           encoding="utf-8") as HTMLFile:
#     contents = HTMLFile.read()
# print(contents)

# soup = BeautifulSoup(contents, "html.parser")