tweets = []
with open('tweet.txt','r',encoding="UTF-8") as oku:
    for satir in oku:
        tweets.append(satir.lstrip("http://dha.com.tr/"))
uzunluk = len(tweets)
i = 0
while i<uzunluk:
    print(tweets[i])
    i+=1