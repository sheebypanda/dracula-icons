import requests
from cairosvg import svg2png
from bs4 import BeautifulSoup

url = "https://draculatheme.com"
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

imgs = soup.find_all('img')

for img in imgs:
    svg_filename = img['src'].split('/')[5]
    print(f"Processing image {svg_filename}")
    icon = requests.get(url+img['src'])
    with open("./svg/"+svg_filename, 'wb') as out:
        out.write(icon.content)
    svg2png(url="./svg/"+svg_filename, write_to="./png/"+svg_filename[0:-4]+".png")
    