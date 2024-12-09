import requests
import bs4

def download(url, output_filename):
    with open(output_filename, 'w') as file:
        txt = requests.get(url).text

        file.write(txt)


def make_pretty(url, output_filename):
    with open(output_filename, 'w') as file:

        soup_object = bs4.BeautifulSoup(requests.get(url).content, features="html.parser")

        file.write(soup_object.prettify())


def find_paragraphs(url, output_filename):
    with open(output_filename, 'w') as file:

        soup_object = bs4.BeautifulSoup(requests.get(url).content, features="html.parser")

        file.writelines([str(tag) + '\n' for tag in soup_object.find_all('p')])


def find_links(url, output_filename):
    with open(output_filename, 'w') as file:

        soup_object = bs4.BeautifulSoup(requests.get(url).content, features="html.parser")

        links = soup_object.find_all('a')

        print(links)

        hrefs = [link.get('href') + '\n' for link in links]

        file.writelines(hrefs)

