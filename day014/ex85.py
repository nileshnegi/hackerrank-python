"""
HTML Parser - Part 1

You are given an HTML code snippet of `N` lines. Your task is to print
start tags, end tags and empty tags separately, along with their attributes.
"""
from html.parser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : {}".format(tag))
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))
    
    def handle_endtag(self, tag):
        print("End   : {}".format(tag))
    
    def handle_startendtag(self, tag, attrs):
        print("Empty : {}".format(tag))
        for attr in attrs:
            print("-> {} > {}".format(attr[0], attr[1]))
    
    def handle_comment(self, data):
        pass

if __name__ == '__main__':
    parser = MyHTMLParser()

    for _ in range(int(input())):
        parser.feed(input())
