from django.shortcuts import render
from newsapi import NewsApiClient 






# Create your views here.

def news_view(request):
    newsapi = NewsApiClient(api_key='f1ec08366ab44e6a8880dcd70c6a4d2a')
    topnews = newsapi.get_everything(sources= 'bbc-news, the-verge, techchrunch, cnn, bloomberg, google-news', sort_by='popularity', language='en')


    latest_news = topnews['articles']


    title=[]
    desc=[]
    url=[]
    author=[]
    date=[]
    img=[]
    source=[]



    for i in range(len(latest_news)):
        news = latest_news[i]

        title.append(news['title'])
        desc.append(news['description'])
        url.append(news['url'])
        author.append(news['author'])
        date.append(news['publishedAt'])
        img.append(news['urlToImage'])
        source.append(news['source']['name'])

        all_news = zip(title, desc, url, author, date, img, source)



        context = { 
                  'all_news': all_news,
                  }


    return render(request, 'news.html', context)


