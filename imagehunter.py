'''
this is where I learned to find the images on google and download them not to mention process them for OpenCV
haar cascade training. 
'''



from bs4 import BeautifulSoup
import requests
import re
import urllib.request
import os
import argparse
import sys
import json
from PIL import Image
import cv2

class image_downloader(object):
    def __init__(self,word, max_pages,pos_neg):
        self.word=word
        word= word.split(' ')
        self.base = os.getcwd()
        image='+'.join(word)
        self.url = "https://www.google.co.in/search?q="+image+"&source=lnms&tbm=isch"
        self.header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
        self.word = '-'.join(word)
        self.ActualImages=[]
        self.pos_neg= pos_neg
        self.get_soup =BeautifulSoup(urllib.request.urlopen(urllib.request.Request(self.url,headers=self.header)),'html.parser')
        self.max_pages = max_pages

    def does_dir_exist(self):
        if not os.path.exists(self.base+'/'+self.pos_neg):
            os.makedirs(self.base+'/'+self.pos_neg)
        else:
            print('blue')

    def parsers(self):
        parser = argparse.ArgumentParser(description='Scrape Google images')
        parser.add_argument('-n', '--num_images', default=25, type=int, help='num images to save')
        parser.add_argument('-d', '--directory', default='/Users/hanweng/Desktop/'+self.word, type=str, help='save directory')
        args = parser.parse_args()
        return args

    def downloading(self):

        for a in self.get_soup.find_all("div",{"class":"rg_meta"}):
            link , Type =((json.loads(a.text)["ou"] ) ,(json.loads(a.text)["ity"]))
            #print ((json.loads(a.text)['ou'] ))
            self.ActualImages.append((link,Type))


    def filtering(self):
        for i , (img , Type) in (enumerate( self.ActualImages[0:self.max_pages])):
            try:
                raw_img = urllib.request.urlopen(img).read()
                print(raw_img)
            except urllib.error.URLError:
                continue
            try:
                f = open(os.path.join(self.base+'/'+self.pos_neg +str(i)+".jpg"), 'wb')
                f.write(raw_img)
                f.close()
                Image.open(self.base+'/'+self.pos_neg+str(i)+".jpg")
            except Exception as e:
                os.remove(self.base+'/'+self.pos_neg+str(i)+".jpg")


    def imageconverter(self):
        dictionary= open(self.base+'/img.txt', 'w')

        for i in range(self.max_pages):
            try:
                if os.path.isfile(self.base+'/'+self.pos_neg+str(i)+'.jpg') == True:
                    dictionary.write(self.pos_neg+str(i)+'.jpg\n')
                image_file = Image.open(self.base+'/'+self.pos_neg+str(i)+".jpg")
                image_file = image_file.resize((100, 100), Image.LANCZOS)
                image_file = image_file.convert('L') # convert image to black and white
                image_file.save(self.base+'/'+self.pos_neg+str(i)+".jpg")

            except Exception as e:
                print(e)
                continue
        dictionary.close()


    def render(self):
        self.get_soup()
        self.does_dir_exist()
        self.parsers()
        self.downloading()
        self.filtering()
        self.imageconverter()



def main(args):
    word='background'
    pos_neg = 'neg/'

    max_pages =int(100)
    image = image_downloader(word,max_pages, pos_neg)

    image.render()


if __name__ == '__main__':
    from sys import argv
    try:
        #sends the directory of this file
        main(argv)
    except KeyboardInterrupt:
        pass
    sys.exit()
