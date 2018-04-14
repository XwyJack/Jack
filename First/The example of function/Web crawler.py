from urllib import request

response = request.urlopen("http://taboo.com/")
fi = open("/home/macbookpro/crawler.txt", 'w')
page = fi.write(str(response.read()))



fi.close()

