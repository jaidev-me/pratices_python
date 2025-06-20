import random as r
import string as s
import json
url_dic = {}
host = "http://127.0.0.1:5000/"


def generate_short_url(length=8):
    randomstr = s.ascii_letters + s.digits
    Shorten = ''.join(r.choice(randomstr) for _ in range(length))
    return Shorten

def get_key(my_dic, val):
    data = my_dic.items()
    for key, value in data:
        if val == value:
            return key
        else:
             pass

import json

def return_url(input):
    with open("urls.json", "r") as urls_file:
        all_urls = json.load(urls_file)
        # print(all_urls)
        if input not in list(all_urls["urls"].values()):
            shorted_url = generate_short_url()
            url_dic[shorted_url] = input
            # print(url_dic)
            all_urls['urls'].update(url_dic)
            # print(updated_urls)
            with open("urls.json", "w") as urls_file:
              json.dump(all_urls, urls_file)
            print(f"\n==================> Your short URL is:  {host}{shorted_url}")
        else:
            shorted_url = get_key(all_urls["urls"], input)
            print(f"\n==================> Your short URL is:  {host}{shorted_url}")


while True:
    print("\n**********URL SHORTNER**********\n")
    url = input("Enter your long url or Type (0) for quit: ").strip()
    if url == "0":
        break
    else:
        if url:
            return_url(url)
        else:
            print(">>>>>>>>>>>>>>>>>>> Please Enter a URL...........")
    

print("*******************Thanks for using our URL SHORTNER*************************")