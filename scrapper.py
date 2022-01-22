import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.nike.com/ca/launch?s=upcoming'

#URL = 'https://www.nike.com/launch?s=upcoming'

def findProducts():
    URL = 'https://www.nike.com/ca/launch?s=upcoming'

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    productList = []

    soupListOne = soup.findAll(attrs={"ncss-brand u-uppercase fs20-sm fs24-md fs28-lg"})

    soupListTwo = soup.findAll(attrs={"ncss-brand u-uppercase text-color-grey mb-1-sm mb0-md mb-3-lg fs12-sm fs14-md"})

    #for i in range(0, len(soupList)):
     #   #print(soupList[i].get_text())
      #  productList.append(soupList[i].get_text(strip=True))

    for i in range(0, len(soupListOne)):
        #print(soupList[i].get_text())
        productList.append(soupListTwo[i].get_text(strip=True)+" "+soupListOne[i].get_text(strip=True))
    

    #print(productList)
    return productList

def findProductsImgs():
    URL = 'https://www.nike.com/launch?s=upcoming'

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    productImgs = []

    imgCode = soup.findAll(attrs={"image-component"})
    #upcoming-section bg-white ncss-row prl2-md prl5-lg pb4-md pb6-lg
    
    for i in range(0, len(imgCode)):
        if imgCode[i]['alt'] == 'image':
            #print(imgCode[i].get('src'))  
            productImgs.append(imgCode[i].get('src'))

    #print(productImgs)
    return productImgs
    #print(soup.prettify())

def writeToFile(lis, fileName):
    f = open(fileName,'w')
    for i in range(len(lis)):
        f.write(lis[i])
        #f.write('\n')
    f.close()

def compareInv(fileName):
    f = open(fileName,'r')
    lis = f.readlines()
    print(len(lis))
    f.close()
    oldInv = []
    for i in range(len(lis)):
        oldInv.append(lis[i].strip('\n'))
    newInv = findProducts()

    print(oldInv)
    print(newInv)
    newItems = []

    for i in range(len(newInv)):
        print(bool(newInv[i] not in oldInv))
        print(newInv[i])
        if newInv[i] not in oldInv:
            newItems.append(newInv[i])
    
    if len(newItems) > 0:
        return newItems

def sendMail(items):
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('ethanvar6@gmail.com', 'pczkevcxblhgpasd')

    subject = 'New items from nike snkrs'
    body = f"{items}"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('ethanvar6@gmail.com','mycoolandslammingusername@gmail.com',msg)

    print("email sent")

    server.quit()

def main():
    f = open("shoes.txt",'r')
    filee = f.readlines()
    filesize = len(filee)
    f.close()

    if  filesize < 0:
        products = findProducts()
        writeToFile(products, "shoes.txt")

    else:
        newItems = compareInv("shoes.txt")
        allItems = findProducts()
        allImgs = findProductsImgs()

        if len(newItems) > 0:

            for i in range(len(allItems)):
                if allItems[i] not in newItems:
                    allItems.remove(allItem[i])
                    allimgs.remove(allImgs[i])
            
            newProds = ""
        
            for i in range(len(allItems)):
                newProds += f"{allItems[i]}    {allImgs[i]}\n"
            
            writeToFile(newProds, "shoes.txt")    
            print(newProds)



#pczkevcxblhgpasd
#products = findProducts()
#productImgs = findProductsImgs() 
#writeToFile(products, "shoes.txt")
#print(compareInv("shoes.txt"))
#products = findProducts()
#writeToFile(products, "shoes.txt")
#findProducts()
main()
