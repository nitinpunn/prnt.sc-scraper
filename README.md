# prnt.sc Scraper

This is a Python script to scrape images from prnt.sc

## Background

Prnt.sc uses a simple 6 character alphanumeric sequential code for each image. Therefore it is extremely easy to scrape for images.
For more information about this: https://medium.com/@ntipun/a-case-of-poor-url-generation-b7013e3d5fa6

## Usage

The prnt.py file and the pictures folder should be in the same directory and pictures directory must exist.
If the pictures folder does not exists, it will be created.

Mechanize and BeautifulSoup are needed for this and can be installed by the following commands:
```python
pip3 install beautifulsoup4
pip3 install mechanize 
```

## Known issues on macOS

If you encounter an error such as 
```
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)>
```
The solution is here: https://stackoverflow.com/questions/27835619/urllib-and-ssl-certificate-verify-failed-error

## License
[MIT](https://choosealicense.com/licenses/mit/)
