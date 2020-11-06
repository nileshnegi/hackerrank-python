"""
HTML Parser - Part 2

You are given an HTML code snippet of `N` lines. Your task is to print the
single-line comments, multi-line comments and the data. Do not print data
if data == '\n'.
"""
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        data = data.split('\n')
        if len(data) > 1:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        
        for line in data:
            print(line.rstrip())


    def handle_data(self, data):
        if(data == '\n'):
            pass
        else:
            print(">>> Data")
            print(data)


html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()