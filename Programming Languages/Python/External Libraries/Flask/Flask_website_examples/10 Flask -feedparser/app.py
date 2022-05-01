import feedparser
from flask import render_template, request, Flask
# Note 1

app = Flask(__name__)
rss_feed = {'wsj': "https://feeds.a.dj.com/rss/RSSWSJD.xml",
            'cnbc': "https://www.cnbc.com/id/100003114/device/rss/rss.html",
            'washington_post': "http://feeds.washingtonpost.com/rss/politics?itid=lk_inline_manual_2"}


@app.route("/")
def get_news():
    
    if request.args.get('publication'):
        query = request.args.get('publication').lower() 
        if not query or query not in rss_feed: 
            publication = 'wsj'
            feed = feedparser.parse(rss_feed[publication])
            return render_template("view.html", articles=feed['entries'])
        
        publication = query
        feed = feedparser.parse(rss_feed[publication])
        return render_template("view.html", articles=feed['entries'])
    return render_template("view.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)


    @app.route("/")
def get_news():
    
    
    # if request.args.get('publication'):
    #     query = request.args.get('publication').lower() # Note 2
    #     print(f'Query is : {query}') # Note 4
    #     if not query or query not in rss_feed: # Note 3
    #         print('Publication is wsj') # Note 4
    #         publication = 'wsj'
    #     else:
    #         print('Publication is the query entry') # Note 4
    #         publication = query

    #     feed = feedparser.parse(rss_feed[publication])

    #     return render_template("view.html", articles=feed['entries'])
    # return render_template("view.html")