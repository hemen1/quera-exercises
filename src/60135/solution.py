from bs4 import BeautifulSoup


def process(name):
    with open(name, 'r') as f:
        html_text = f.read()
    soup = BeautifulSoup(html_text)
    return len(soup.find_all('a'))
print(process("htmlsampletest1.html"))
print(process("htmlsampletest2.html"))
