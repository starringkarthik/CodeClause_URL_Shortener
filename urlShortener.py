import pyshorteners
long_url = input("Enter the URL to shorten: ")

#by using the default shortener (tinyurl)
type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)
print("The Shortened URL is: " + short_url)

#by using bitly api
type_bitly = pyshorteners.Shortener(api_key='2d1c136cad9f0793625ef878190a666eaa55221d')
short_url = type_bitly.bitly.short(long_url)
print("The Shortened URL is: " + short_url)
expand_url = type_bitly.bitly.expand(short_url)
print (expand_url)
