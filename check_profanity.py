import urllib

def read_text():
    quotes = open('movie_quotes.txt')
    read = quotes.read()
    quotes.close()
    check_profanity(read)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()

read_text()
