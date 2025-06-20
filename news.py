import requests
import time
import json

print("\n\n-----------***Welcome to the News TV***---------------")
while True:
    topic = input("\n-----Which type of news are you interested in: ")
    day = int(input("\n-----Enter the date of this month on which you want to see the news: "))
    date = time.strftime(f"%m-{day}-%Y")

    url = f'https://newsapi.org/v2/everything?q={topic}&from={date}&sortBy=popularity&apiKey=43cbdaf3c1aa4267a6c10b9656662a47'

    res = requests.get(url)
    news = json.loads(res.text)
    if news['totalResults'] == 0:
         print("\n\n---->Oops we not found any results! Please try to search one day before news OR Type valid choice<----")
    for art in news['articles']:
        print(f"\n\n*Author:--- {art['author']}\n")
        print(f"*Topic:--- {art['title']}\n")
        print(f"*This artical was published on:--- {art['publishedAt']}\n")
        print(f"*Description:--- {art['content']}\n")
        print(f"*You can read full news here:--- {art['url']}\n")   
        choice = input("-----Press any key to Load more news or Press (0) zero to Quit: ")
        try:
            if int(choice) == 0:
                break 
        except:
            pass
        print('\n------------------------------------------------------------------------')
    choice = input("\n-----Press any key to explore or search more news topics or Press (0) zero to Quit: ")
    try:
        if int(choice) == 0:
                break 
    except:
        pass
print("\n**Bayee! Have a nice day**\n")