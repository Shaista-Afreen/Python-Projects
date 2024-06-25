#Install necessary library
#pip install pyshorteners

import pyshorteners


def create_short_url(original_url):
    url_shortener = pyshorteners.Shortener()
    shortened_url = url_shortener.tinyurl.short(original_url)
    return shortened_url

link_to_shorten = input("Enter any URL: ")
shortened_link = create_short_url(link_to_shorten)
print("The shortened URL is : "+ shortened_link)