import requests
from bs4 import BeautifulSoup

# Save result in csv File:
csvFile = open('vcards.csv', 'a')
    
# Get total pages
URL = 'http://okt.ir/?page=show-vcard-v&tpage=1'
source = requests.get(URL)
soup = BeautifulSoup(source.content, 'html.parser')
navigationElements = soup.find_all("a", {"class": 'page-numbers'})
pageCount = len(navigationElements) + 1
print ("===> Totla Pages: ", pageCount)

# Get All vcards
for id in range(pageCount):
    URL = "http://okt.ir/?page=show-vcard-v&tpage=" + str(id+1)
    print ("===> Get VCards From:  ", URL)

    ##
    source = requests.get(URL)
    soup = BeautifulSoup(source.content, 'html.parser')
    vcards = soup.find_all("div", {"class": 'atbd_single_listing'})
    vcardsCount = len(vcards)
    print ("===> Totla Vcard per URL: ", vcardsCount)
    for vcard in vcards:
        vcardTitleElement = vcard.find('h4', class_='atbd_listing_title')
        vcardDataElement = vcard.find('div', class_='atbd_listing_data_list')
        vcardImageElement = vcard.find('img', class_='k_img_item_user')

        vcardTitle = vcardTitleElement.text.strip().replace(',', '-')
        vcardData = vcardDataElement.text.strip().replace(',', '-').replace('\n\n\n', ',')
        vcardImageSrc = vcardImageElement['src']
        vcardImageAlt = vcardImageElement['alt']

        vcardCSVRow = vcardTitle + "," + vcardData + "," + vcardImageSrc + "," + vcardImageAlt + "\n\r"  

        csvFile.write(vcardCSVRow)
        print ("===> CSV ROW:  ", vcardCSVRow)

csvFile.close()

        
