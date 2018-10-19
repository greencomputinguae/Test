import cv2
import numpy as np
def emptyfun():
    pass

def main() :
    img=np.zeros((512,512,3),np.uint8)

    windowname = "amir"
    cv2.namedWindow(windowname)
    cv2.createTrackbar('B',windowname,0,255,emptyfun)
    cv2.createTrackbar('R', windowname, 0, 255, emptyfun)
    cv2.createTrackbar('G', windowname, 0, 255, emptyfun)


    while(True):

        cv2.imshow(windowname, img)

        if cv2.waitKey(1) == 27:
            break

        blue = cv2.getTrackbarPos('B', windowname)
        green = cv2.getTrackbarPos('G', windowname)
        red = cv2.getTrackbarPos('R', windowname)
        img[:] = [blue, green, red]
    cv2.destroyAllWindows()

if __name__=="__main__" :
    main()


string="""
<html><head></head><body>
<h1>This is a test</h1>

<ul>
<li>Amir</li>
<li>zahra</li>
<li>ali</li>
<li>Gholi</li>
</ul>
<p>this is a paragraph</p>
<p class="subtitle">hi this is a class</p>

</body></html>
"""

simple_html= BeautifulSoup(string, 'html.parser')

print(simple_html.find('h1').string)

temp=simple_html.find_all('li')
list_string=[i.string for i in temp]
print(list_string)

para=simple_html.find_all('p')
para1=[i for i in para if 'subtitle' not in i.attrs.get('class', [])]
print(len(para1))
print(para1[0].string)

import requests
page=requests.get('http://www.example.com')
cont=BeautifulSoup(page.content, 'html.parser')





#------------------------------------------------







class page_structure:
    def __init__(self, page_content):
        self.qoute='div.container div.row div.col-md-8 div.quote span.text'
        self.author='div.container div.row div.col-md-8 div.quote span small.author'
        self.page_content=page_content

    def name(self):
        for i in self.page_content.find_all(self.qoute)
        out1=self.page_content.select_one(self.qoute)
        #result=out1.attrs['text']
        return  out1.string


page=requests.get('http://quotes.toscrape.com/')
page_html=BeautifulSoup(page.content, 'html.parser')
a=page_structure(page_html)
print(a.name())

