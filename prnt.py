import random
import string
import mechanize
import bs4
import os

# The random combinations will be stored here
combos = []

# Create a browser object form mechanize and add a realistic header to prevent a 403
browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# Fixes an issue that sometimes may come up where https: is missing
def fixSlash(img_url):
    if img_url[0] == "/":
        return "https:" + img_url
    else:
        return img_url

# Generates the 6 character alphanumeric combinations and adds them to the combos list
def generateRandom(amount):
    print("Generating random combinations")
    for i in range(amount):
        combos.append(''.join(random.choices(string.ascii_lowercase + string.digits, k=6)))

# Takes the combos list and sequentially loads each link and downloads the image
def tryRandom(tries):
    print("Grabbing images")
    samples = random.sample(combos, tries)
    for i in range(len(samples)):
        url = "https://prnt.sc/" + samples[i]
        browser.open(url)
        html = browser.response().read()
        temp = bs4.BeautifulSoup(html, features="html5lib")
        images = [img['src'] for img in temp.findAll('img') if img.has_attr('src')]
        image = images[0]
        image = fixSlash(image)
        picture = browser.retrieve(image, "pictures/" + samples[i] + ".jpg")
        print("Done with " + str(i+1) + "/" + str(amount))

if __name__ == "__main__":
    if not os.path.exists("pictures"):
        os.makedirs("pictures")
    amount = int(input("Enter amount of images to scrape: "))
    generateRandom(amount)
    print("Combinations generated!")
    tryRandom(amount)
    print("Done!")
