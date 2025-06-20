from flask import Flask, redirect
import json
app = Flask(__name__)

@app.route(f"/<short_url>", methods=["GET"])
def redirectl(short_url):
    with open("urls.json", "r") as urls_file:
        all_urls = json.load(urls_file)
        longurl = all_urls["urls"].get(short_url)
        if longurl:
            return redirect(longurl)
        else:
            return "<h1>URL not found 404</h1>"
        

if __name__ == "__main__" :

    app.run(debug=True)
