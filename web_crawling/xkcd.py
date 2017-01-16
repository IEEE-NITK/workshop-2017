from bs4 import BeautifulSoup
import urllib

url = "http://xkcd.com/"

n=input("Enter the number of images you want to download : ")
for i in range(1,n+1):
    file = urllib.urlopen(url+str(i)+"/")
    soup = BeautifulSoup(file.read(),"html.parser")

    comic=soup.find('div',id='comic')
    image = comic.img['src']

    img_url = image.strip('/')
    file.close()

    file = urllib.urlopen("http://"+img_url)

    with open("image"+str(i),"wb") as store:
        store.write(file.read())

    file.close()
