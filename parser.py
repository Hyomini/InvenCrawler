from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "invenCrawler.settings")
import django
django.setup()
from parsed_data.models import Link
from parsed_data.models import Cmt
from parsed_data.models import Member

cmt_dict = {}


def page_parser(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('headless')
    options.add_argument('--disable-gpu')
    options.add_argument("lang=ko_KR")
    driver = webdriver.Chrome("C:\chromedriver.exe", options=options)
    driver.get(url)
    parser = BeautifulSoup(driver.page_source, "html.parser")
    return parser, driver


def cmtToNick(url):
    parser, driver = page_parser(url)
    n = parser.find_all('span', class_="nickname")
    c = parser.find_all('span', class_="content cmtContentOne")
    d = parser.find_all('span', class_="date")
    for i in range(len(n)):
        tmp = c[i].text.replace('\\xa0', ' ')
        c_tmp = d[i].text.replace('(', '')
        c_tmp = c_tmp.replace(')', '')
        if n[i].text not in cmt_dict:
            cmt_dict[n[i].text] = [(tmp, c_tmp, url)]
        else:
            cmt_dict[n[i].text] = cmt_dict.get(n[i].text, []) + [(tmp, c_tmp, url)]
    driver.close()


def get_href(url):
    boardList = {}
    parser, driver = page_parser(url)
    linkList = parser.find_all('a', class_='sj_ln')

    for link in linkList:
        boardList[link.text] = link['href']
    driver.close()
    return boardList

def getLink():
    tmp = Link.objects.all()
    link_list = []
    for t in tmp:
        link_list.append(t.link)
    return link_list

if __name__ == "__main__":
    target_link = "http://www.inven.co.kr/board/lol/4625"
    existing_links = []

    # DB에 저장되어 있는 게시물 링크 가져오기
    existing_links = getLink()


    # 인벤 LoL/e스포츠 게시판으로부터 게시물들의 href링크 가져오기
    # DB에 이미 있는 링크는 가져오지 않도록 조정 필요!!!
    start = time.time()
    board_list = get_href(target_link)
    getLinkTime = time.time()
    print(f'1페이지({len(board_list)})의 게시물 링크를 가져오는 시간: {(getLinkTime - start):.2f}s')

    # DB에 저장되어 있는 링크와 중복검사, 만약 중복된 링크가 있다면 삭제
    boards = list(board_list.values())
    for board in boards[:]:
        if board in existing_links:
            print(f'중복된 링크: {board}')
            boards.remove(board)

    # 게시물들의 댓글을 닉네임별로 수집
    for board in boards:
        cmtToNick(board)

    cmtTime = time.time()
    print(f'{len(boards)}개 게시글의 댓글 리스트를 가져와서 저장하는 시간: {(cmtTime - getLinkTime):.2f}s')
    print(cmt_dict)
    for t, l in board_list.items():
        try:
            Link(title=t, link=l).save()
        except:
            print("중복된 데이터입니다.")

    for n, c_list in cmt_dict.items():
        tmp_member = Member(nickname_text = n)
        try:
            tmp_member.save()
        except:
            print("중복된 id입니다.")
        for c in c_list:
            Cmt(nickname=tmp_member, comment=c[0], date=c[1], link=c[2]).save()

    print(f"게시물(개수:{len(boards)}) 및 댓글 업데이트가 완료되었습니다!")

