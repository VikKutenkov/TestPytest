# coding: utf-8
__author__ = 'Sky'

import requests
from lxml.html import fromstring

last_en='ax'
last_ru='а2'
k=1
alphabet_en = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q'
    ,'r','s','t','u','v','w','x','y','z'] # 26
alphabet_ru = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п'
    ,'р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я'] # 33
domain_com = ['.com','.net','.org','.ru','.info','.xyz','.site','.online','.рф','.io'
    ,'.space','.pro','.tech','.world','.dev','.one','.company','.studio','.technology'
    ,'.zone','.team','.international','.games','.guide','.community','.productions'
    ,'.computer','.place','.black','.game','.sky','.free','.open','.play','.dark'
    ,'.darkness','.night','.shadow']
domain_free = ['.tk','.ga','.cf','.gq','.ml'] # 5
domain_rus = ['.рус','.москва','.онлайн','.сайт','.орг']
profile = ['.livejournal.com'] # 5
numberbet = ['0','1','2','3','4','5','6','7','8','9'] # 10
symbolbet = [' ','-','_','.',r'/','\\'] # 5


def word(alpha,last,ru_en):
    """ строим слово """
    global last_en,last_ru
    ns=[]
    a=[]
    for s in last[::-1]:
        ns.append(alpha.index(s))

    while ns:
        n=ns.pop(0)+1
        if n<len(alpha):
            a.append(n)
            a=a+ns
            break
        else:
            a.append(0)
        if ns==[]:
            a.append(0)
    a.reverse()
    last=''
    for n in a:
        last=last+alpha[n]
    if ru_en=='в': last_ru=last
    elif ru_en=='w': last_en=last
    return last


def dom(l,domain):
    for ss in l:
        for s in domain:
            try:
                s='http://%s%s' % (ss,s)
                # response = requests.get(ss, verify=False, allow_redirects=False)
                response = requests.get(s, allow_redirects=True,timeout=10)
                requests.max_redirects=10
                print()
                response.raise_for_status()
                if response.history:
                    for hist in response.history:
                        print('   --->',hist.status_code, hist.url)
                print(response.status_code,'|',s,'|',response.url)
                tree = fromstring(response.content)
                title = tree.xpath('//title')
                description = tree.xpath('//meta[@property="og:description" or @name="description"]')
                print(title[0].text)
                print(description[0].attrib['content'])
            except requests.exceptions.ConnectionError:
                pass
            except IndexError:
                pass
            except Exception as e:
                print(e)


if __name__ == "__main__":
    l_en=[]
    l_ru=[]

    alpha_en=alphabet_en+numberbet+symbolbet
    alpha_ru=alphabet_ru+numberbet+symbolbet

    for i in range(k):
        l_en.append(word(alpha_en,last_en,'w'))
    for i in range(k):
        l_ru.append(word(alpha_ru,last_ru,'в'))
    for s in l_en:
        print(s)
    print()
    for s in l_ru:
        print(s)

    dom(l_en,domain_com)
    dom(l_en,domain_free)
    dom(l_en,profile)
    dom(l_ru,domain_rus)
