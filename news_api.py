import requests

print("                S.R NEWS                    ")
query=input("What news are you interested to read ?\n" )
api="af29d5a954224257b4ab5dc0cf2299ab"
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-06-17&sortBy=publishedAt&apiKey={api}"
print(url)
r =  requests.get(url)

data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")