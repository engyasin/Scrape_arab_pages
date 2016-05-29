# -*- coding: utf-8 -*-
"""
Created on Fri May 27 18:53:26 2016
PC-Name : External

"""

import requests
import datetime

from bs4 import BeautifulSoup

# from windows 1256 (arabic) to utf-8
# runfile('windows1256_to_utf8.py')
from win1256_to_utf8 import convert

# it only starts from 3 to .. say 400
url_try = ''

f1 = open('The_Loosers_Storeis.txt','w+');
f1.write('Start_Scraping_the_site..\n')
f1.write('--------------------------\n')
f1.write(str(datetime.datetime.now()) + '\n')
f1.write('--------------------------\n')

for x in range(1,400):
    # take every url..
    url = 'http://example.com/article{}'.format(x)
    response = requests.get(url);
    
    # is connection OK
    if response.status_code == 200 :
        print '==== There\'s article {0} ==='.format(x)
        soup = BeautifulSoup(response.text , "html.parser",
                              from_encoding=" windows-1256 ");
        # here we got a page, 
        a = soup.find_all(class_= 'title')
        
        # we will take the first item , whatever

        
        if a :
            # there's a page
            s = a[0]
            title_raw = s.string
        else:
            title_raw = None;
            # just to escape the other if
            
        if title_raw:
            # we have a title 
            # convert to arabic:
            title = convert(title_raw);
            
            # write it to file:
            f1.write('\n')
            f1.write('\n =========== Article {0} ==========='.format(x))
            f1.write('\n')
            f1.write(title)
            
        else :
            print "===article {0} donnot have title,... Loosers==".format(x)
            # we don't have a title
            
            # mention that in the file with the number of article
            f1.write('\n')
            f1.write('\n ======== Article {0} Do\'nt have a title ========'.format(x))
        
    else:
        # connection fail for some reason
        f1.write('\n')
        f1.write('\n ======== Article {0} maybe do\'nt exist!(url) ========'.format(x))        



# We need to close the file :

f1.write('\n' + str(datetime.datetime.now()) + '\n')
f1.write('\n\n==============The END==============')
f1.close()





