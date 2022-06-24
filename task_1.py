import re


def domain_name(url):
    domain_lvl = re.split(r'\.', url)
    if domain_lvl[0] == 'www':
        return domain_lvl[1]
    return re.split(r'//', domain_lvl[0])[1]


if __name__ == '__main__':
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
