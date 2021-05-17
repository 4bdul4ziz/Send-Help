from html.parser import HTMLParser
import urllib.request


class LinkScrape(HTMLParser):

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    link = attr[1]
                    if link.find('http') >= 0:
                        print('- ' + link)


if __name__ == '__main__':
    url = input('Enter URL > ')
    request_object = urllib.request.Request(url)
    page_object = urllib.request.urlopen(request_object)
    link_parser = LinkScrape()
    link_parser.feed(page_object.read().decode('utf-8'))