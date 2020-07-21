import pyshorteners
import webbrowser
link=input("Copy the link\n")
short=pyshorteners.Shortener()
x=short.tinyurl.short(link)
print(x)
webbrowser.open(x)
