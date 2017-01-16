from bs4 import BeautifulSoup
import urllib

url = "http://www.billboard.com/charts/hot-100"

file = urllib.urlopen(url)

soup = BeautifulSoup(file.read(),"html.parser")

nos = soup.find_all('div',class_="chart-row__rank")
songs = soup.find_all('h2',class_="chart-row__song")
artists = soup.find_all('a',class_="chart-row__artist")


for i in range (0,len(nos)-1):
    print i,"\t" + songs[i].string + "\t\t" + artists[i].string.strip()

