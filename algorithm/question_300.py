def question_001():
    print(f"01|Hello World")


def question_002():
    print(f"02|Mary's cosmetic")


def question_003():
    print(f'03|신씨가 소리질렀다. "도둑이야"')


def question_004():
    print(f'04|"C:\Windows"')


def question_005():
    print("05|안녕하세요.\n만나서\t\t반갑습니다.")
    """ \n은 줄바꿈, \t는 탭 기능 """


def question_006():
    print(f'06|"C:\Windows"')


def question_007():
    print("07|", "오늘은", "일요일")
    """한줄씩 띄워서 출력됨"""


def question_008():
    print(f'08|naver/kakao/sk/samsung')
    print("08|", "naver", "kakao", "sk", "samsung", sep="/")


def question_009():
    print("09|", "first", end="");print("second")


def question_010():
    print("10|", 5/3)


def question_011():
    삼성전자 = 50000
    print(f"11|삼성전자 가격: {삼성전자*10}")


def question_012():
    시가총액 = 298000000000
    현재가 = 50000
    PER =15.79
    print(f"12|시가총액: {시가총액, type(시가총액)}")
    print(f"12|현재가: {현재가, type(현재가)}")
    print(f"12|PER: {PER, type(PER)}")


def question_013():
    s = "hello"
    t = "python"
    print(f"13|{s+'! ' +t}")


def question_014():
    print(f"14|{2+2*3}")


def question_015():
    a = 128
    b = "128"
    print(f"15|{a, type(a)}")
    print(f"15|{b, type(b)}")


def question_016():
    a = "128"
    print(f"16|{a, type(a)}")
    a = int(a) + 1
    print(f"16|{a, int(a), type(a)}")


def question_017():
    num = 100
    num = str(num)
    print(f"17|{num, type(num)}")


def question_018():
    a = "15.79"
    a = float(a) + 1.01
    print(f"18|{a, type(a)}")


def question_019():
    year = "2020"
    year = int(year)
    for i in range(0, 4):
        print(f"19|{year-i}")


def question_020():
    cost = 48584
    month = 36

    print(f"{cost * month}")


def question_021():
    letters = 'python'
    print(f"{letters[0], letters[2]}")


def question_022():
    letters = '24가 2210'
    print(f"{letters[-4:]}")


def question_023():
    letters = '홀짝홀짝홀짝'
    print(f"{letters[::2]}")


def question_024():
    letters = 'python'
    print(f"{letters[::-1]}")


def question_025():
    letters = '010-1111-2222'
    phone_number = letters.replace("-", " ")
    print(phone_number)


def question_026():
    letters = '010-1111-2222'
    print(f"{letters.replace('-', '')}")


def question_027():
    url = "http://sharebook.kr"
    url = url.split('.')
    print(f"{url[1]}")


def question_028():
    lang = 'python'
    lang[0] = 'P'
    print(lang)


def question_029():
    string = 'abcdfe2a354a32a'
    print(f"{string.replace('a','A')}")


def question_030():
    string = 'abcd'
    string.replace('b', 'B')
    print(f"{string}")


question_030()
