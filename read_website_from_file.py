from bs4 import BeautifulSoup
with open('cookie.txt', 'r') as input:
    print(BeautifulSoup(input.read(), "html.parser").find_all("div"))
