"""
XML 1 - Find the Score

Output a single line, the integer score of the given XML document.
This integer score is calculated by the sum of the score of each element.
For any element, this score is equal to the number of attributes it has.
"""
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    if node.attrib == {}:
        return sum([get_attr_number(child) for child in node])
    else:
        return len(node.attrib) + sum([get_attr_number(child) for child in node])

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
