from bs4 import BeautifulSoup
import urllib

url = "https://en.wikipedia.org"

topic = raw_input("Enter the topic you want Data on : ")

file = urllib.urlopen(url+"/wiki/" + topic)

soup = BeautifulSoup(file.read(),"html.parser")

p1 = soup.find('div',id="mw-content-text")
p1 = p1.find('p',recursive=False)
print p1.get_text()

p2 = p1.find_next('p')
print p2.get_text()

file.close()
