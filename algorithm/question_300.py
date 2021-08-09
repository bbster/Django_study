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


def question_031():
    a = '3'
    b = '4'
    print(f"{a+b}")


def question_032():
    a = 'hi'
    print(f"{a*3}")


def question_033():
    a = '-'
    print(f"{a*80}")


def question_034():
    a = 'python'
    b = 'java'
    print(f"{(a+b)*4}")


def question_035():
    name1 = "김민수"
    age1 = 10
    name2 = "이철희"
    age2 = 13

    print("이름: %s, 나이: %d" % (name1, age1))
    print("이름: %s, 나이: %d" % (name2, age2))


def question_036():
    name1 = "김민수"
    age1 = 10
    name2 = "이철희"
    age2 = 13

    print("이름: {}, 나이: {}".format(name1, age1))
    print("이름: {}, 나이: {}".format(name2, age2))


def question_037():
    name1 = "김민수"
    age1 = 10
    name2 = "이철희"
    age2 = 13

    print(f"이름: {name1}, 나이: {age1}")
    print(f"이름: {name2}, 나이: {age2}")


def question_038():
    상장주식수 = "5,969,782,550"
    rep_data = int(상장주식수.replace(",", ""))

    print(f"주식수: {rep_data}, data_type: {type(rep_data)}")


def question_039():
    분기 = "2020/03(E) (IFRS연결)"
    slicing_data = 분기.split("(")
    slicing_data2 = 분기[:7]

    print(f"slicing_data: {slicing_data[0]}")
    print(f"slicing_data2: {slicing_data2}")


def question_040():
    data = "    삼성전자     "
    strip_data = data.strip()

    print(f"strip_data(공백제거): {strip_data}")


def question_041():
    ticker = "btc_krw"
    upper_ticker = ticker.upper()

    print(f"upper_data(소문자=>대문자):{ticker} => {upper_ticker}")


def question_042():
    ticker = "BTC_KRW"
    lower_ticker = ticker.lower()

    print(f"upper_data(소문자=>대문자):{ticker} => {lower_ticker}")


def question_043():
    data = "hello"
    captialize_data = data.capitalize()

    print(f"cap_data(=맨앞자리 => 대문자):{data} => {captialize_data}")


def question_044():
    data = "보고서.xlsx"
    endswith_data = data.endswith("xlsx")

    print(f"endswith_data(해당문자로 끝나는지 체크):{endswith_data}")


def question_045():
    data = "보고서.xlsx"
    endswith_data = data.endswith(("xlsx", "xls"))

    print(f"endswith_data(해당문자로 끝나는지 체크):{endswith_data}")


def question_046():
    data = "2020_보고서.xlsx"
    startswith_data = data.startswith("2020")

    print(f"startswith_data():{startswith_data}")


def question_047():
    data = "hello world"
    split_data = data.split(" ")

    print(f"공백기준으로 나눠보기:{split_data}")


def question_048():
    ticker = "btc_krw"
    split_ticker = ticker.split("_")

    print(f"btc와 krw 나누기:{split_ticker}")


def question_049():
    data = "2020-05-20"
    split_data = data.split("-")

    print(f"년원일 split:{split_data}")


def question_050():
    data = "039485        "
    strip_data = data.rstrip()

    print(f"오른쪽 공백 제거:{strip_data}")


def question_051():
    movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
    print(f"리스트 데이터 :{movie_rank}")
question_051()
