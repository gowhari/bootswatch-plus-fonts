import re
import sys
import ilio
import urllib.request


cssinp = sys.argv[1]
cssout = sys.argv[2]
outdir = sys.argv[3]


def get_urls(text):
    urls = re.findall('url\((https://fonts.gstatic.com/[a-zA-Z0-9/\.\-_]+)\)', text)
    assert len(urls) == text.count('@font-face'), (len(urls), text.count('@font-face'))
    return urls


def main():
    text = ilio.read(cssinp)
    urls = get_urls(text)
    for url in urls:
        filename = '-'.join(url.split('/')[-3:])
        urllib.request.urlretrieve(url, filename)
        text = text.replace(url, filename)
        print(filename)
    ilio.write(cssout, text)


if __name__ == '__main__':
    main()
