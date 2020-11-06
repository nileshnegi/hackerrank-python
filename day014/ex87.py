"""
Detect HTML Tags, Attributes and Attribute Values

The first line contains an integer `N`, the number of HTML code lines.
The next `N` lines contain HTML code.
Print the HTML tags, attributes and attribute values in order of their
occurrence from top to bottom in the snippet. Format your answers as
explained in the problem statement.
"""
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print("-> {} > {}".format(attr[0], attr[1]))
    
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print("-> {} > {}".format(attr[0], attr[1]))
    
    def handle_comment(self, data):
        pass


if __name__ == '__main__':
    parser = MyHTMLParser()

    for _ in range(int(input())):
        parser.feed(input())
