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


def question_052():
    movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
    movie_rank.append("베트맨")
    print(f"리스트 데이터 :{movie_rank}")


def question_053():
    movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
    movie_rank.insert(1,  "슈퍼맨")
    print(f"리스트 데이터 :{movie_rank}")


def question_054():
    movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
    movie_rank.remove("럭키")
    print(f"리스트 데이터 :{movie_rank}")


def question_055():
    movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
    movie_rank.remove("럭키")
    movie_rank.remove("스플릿")
    print(f"리스트 데이터 :{movie_rank}")


def question_056():
    lang1 = ["C", "C++", "JAVA"]
    lang2 = ["Python", "Go", "C#"]
    langs = lang1 + lang2
    print(f"리스트 데이터 :{langs}")


def question_057():
    nums = [1,2,3,4,5,6,7]
    max_num = max(nums)
    min_num = min(nums)
    print(f"max_num :{max_num}")
    print(f"min_num :{min_num}")


def question_058():
    nums = [1,2,3,4,5]
    result = sum(nums)

    print(f"result :{result}")


def question_059():
    nums = [1,2,3,4,5]
    result = len(nums)
    print(f"result :{result}")


def question_060():
    nums = [1,2,3,4,5]
    result = sum(nums)
    average = result / len(nums)

    print(f"result :{average}")


def question_061():
    price = ["20102931", 100, 200, 300, 400]

    print(f"result :{price[1:]}")


def question_062():
    price = [1,2,3,4,5,6,7,8,9,10]

    print(f"result :{price[::2]}")


def question_063():
    price = [1,2,3,4,5,6,7,8,9,10]

    print(f"result :{price[1::2]}")


def question_064():
    nums = [1, 2, 3, 4, 5]
    reversed_nums = nums[::-1]
    print(f"result :{reversed_nums}")


def question_065():
    data = ["삼성전자", "LG전자", "카카오"]

    print(f"result :{data[0], data[2]}")


def question_066():
    data = ["삼성전자", "LG전자", "카카오", "대우", "MSI"]

    print("result: ", "".join(data))


def question_067():
    data = ["삼성전자", "LG전자", "카카오", "대우", "MSI"]

    print("result: ", "/".join(data))


def question_068():
    data = ["삼성전자", "LG전자", "카카오", "대우", "MSI"]

    print("\n".join(data))


def question_069():
    string = "삼성전자/LG전자/SK"
    interest = string.split("/")

    print(interest)


def question_070():
    data = [1, 9, 2, 3, 8, 6, 5, 10, 4, 7]
    data.sort()
    print(f"result: {data}")


def question_071():
    data = ()
    print(f"result: {type(data)}")


def question_072():
    data = ("닥터스트레인지", "스플릿", "럭키")
    print(f"result: {data}")


def question_073():
    _integer = (1)
    _tuple = (1, )
    print(f"result: {type(_integer)}")
    print(f"result: {type(_tuple)}")


def question_075():
    t1 = 1, 2, 3, 4
    print(f"result: {type(t1)}")


def question_076():
    t1 = ('a', 'B', 'c')
    print(f"result: {t1, type(t1)}")


def question_077():
    t1 = ('a', 'B', 'c')
    t1_listed = list(t1)
    print(f"result: {t1_listed, type(t1_listed)}")


def question_078():
    t1 = ['a', 'B', 'c']
    t1_typled = tuple(t1)
    print(f"result: {t1_typled, type(t1_typled)}")


def question_079():
    t1 = ('a', 'B', 'c')
    a, b, c = t1
    print(f"result: {a, b, c}")


def question_080():
    t1 = tuple(range(2, 100, 2))
    print(f"reult: {t1}")


def question_081():
    scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
    *a, _, _ = tuple(scores)
    print(f"{a}")


def question_082():
    scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
    _, _, *c = tuple(scores)
    print(f"{c}")


def question_083():
    scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
    _, *b, _ = tuple(scores)
    print(f"{b}")


def question_084():
    temp = {}
    print(f"{type(temp)}")


def question_085():
    temp = {"메로나": 1000, "플라포": 1200, "빵빠레": 1800}
    print(f"{temp}")


def question_086():
    temp = {"메로나": 1000, "플라포": 1200, "빵빠레": 1800}
    temp["죠스바"] = 1200
    temp["월드콘"] = 1500
    print(f"{temp}")


def question_087():
    temp = {"메로나": 1000, "플라포": 1200, "빵빠레": 1800}
    temp["죠스바"] = 1200
    temp["월드콘"] = 1500
    print(f"메로나 가격: {temp['메로나']}")


def question_088():
    temp = {"메로나": 1000, "플라포": 1200, "빵빠레": 1800}
    temp["죠스바"] = 1200
    temp["월드콘"] = 1500
    temp["메로나"] = 1300
    print(f"메로나 가격: {temp['메로나']}")


def question_089():
    temp = {"메로나": 1000, "플라포": 1200, "빵빠레": 1800}
    temp["죠스바"] = 1200
    temp["월드콘"] = 1500
    del temp["메로나"]
    print(f"메로나 가격: {temp['메로나']}")


def question_090():
    temp = {"메로나": 1000, "플라포": 1200, "빵빠레": 1800}
    temp["죠스바"] = 1200
    temp["월드콘"] = 1500
    del temp["메로나"]
    print(f"메로나 가격: {temp['메로나']}")
    # 메로나가 삭제되어 없는 키이기 때문에 에러 발생


def question_091():
    temp = {"메로나": [300, 20], "플라포": [400, 3], "빵빠레": [250, 100]}
    print(f"메로나 가격: {temp}")


def question_092():
    temp = {"메로나": [300, 20], "플라포": [400, 3], "빵빠레": [250, 100]}
    print(f"메로나 가격: {temp['메로나'][0]}")


def question_093():
    temp = {"메로나": [300, 20], "플라포": [400, 3], "빵빠레": [250, 100]}
    print(f"메로나 재고: {temp['메로나'][1]}")


def question_094():
    temp = {"메로나": [300, 20], "플라포": [400, 3], "빵빠레": [250, 100]}
    temp["월드콘"] = [500, 7]
    print(f"월드콘 추가: {temp}")


def question_095():
    icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
    temp = list(icecream.keys())
    print(f"keys_list: {temp}")


def question_096():
    icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
    temp = list(icecream.values())
    print(f"values_list: {temp}")


def question_097():
    icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
    temp = sum(icecream.values())
    print(f"values 합: {temp}")


def question_098():
    icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
    new_product = {'팥빙수': 2700, '아맛나': 1000}
    icecream.update(new_product)
    print(f"dict 합치기: {icecream}")


def question_099():
    keys = ("apple", "pear", "peach")
    vals = (300, 250, 400)

    result = dict(zip(keys, vals))
    print(f"zip, dict: {result}")


def question_100():
    date = ['09/05', '09/06', '09/07', '09/08', '09/09']
    close_price = [10500, 10300, 10100, 10800, 11000]

    result = dict(zip(date, close_price))
    print(f"zip, dict: {result}")


def question_101():
    pass
    # 파이썬에서 True 혹은 False를 갖는 데이터 타입은? bool 타입


def question_102():
    print(3==5)
    # False


def question_103():
    print(3 < 5)
    # True


def question_104():
    x = 4
    print(1 < x < 5)
    # True


def question_105():
    print((3 == 3) and (4 != 3))
    # 3은3과 같고 그리고 4는 3과 같지 않다
    # True


def question_106():
    pass
    # print(3 => 4)
    # 지원하지 않는 연산자 / 에러 발생


def question_107():
    if 4 < 3:
        print("Hello World")
    # 아무것도 출력하지 않음


def question_108():
    if 4 < 3:
        print("Hello World")
    else:
        print("Hi, there")
    # Hi there 출력


def question_109():
    if True:
        print("1")
        print("2")
    else:
        print("3")
    print("4")
    # 1,2,4 출력


def question_110():
    if True:
        if False:
            print("1")
            print("2")
        else:
            print("3")
    else:
        print("4")
    print("5")
    # 3,5 출력


def question_111():
    user_data = input("입력: ")
    print(f"{user_data*2}")


def question_112():
    user_data = int(input("숫자 입력: "))
    print(f"{user_data+10}")


def question_113():
    user_data = int(input("숫자 입력: "))
    if user_data%2 == 0:
        print(f"{user_data}는 짝수")
    else:
        print(f"{user_data}는 홀수")


def question_114():
    user_data = int(input("숫자 입력: "))
    user_data += 20
    if user_data <= 255:
        print(f"{user_data}")
    else:
        print(f"255")


def question_115():
    user_data = int(input("숫자 입력: "))
    user_data -= 20
    if user_data <= 0:
        print(f"0")
    elif user_data >= 255:
        print(f"255")
    else:
        print(f"{user_data}")


def question_116():
    user_data = input("입력: ")
    split_data = user_data.split(":")
    if int(split_data[1]) == 0:
        print(f"정각")
    else:
        print(f"정각이 아닙니다")
    """
    user_data = input("입력: ")
    if user_data[-2:] == "00":
        print(f"정각")
    else:
        print(f"정각이 아닙니다")
    """


def question_117():
    user_data = input("입력: ")
    fruit = ["apple", "graph", "melon"]

    if user_data in fruit:
        print(f"정답입니다.")
    else:
        print(f"오답입니다.")


def question_118():
    user_data = input("입력: ")
    warn_investment_list = ["microsoft", "samsung", "apple"]

    if user_data in warn_investment_list:
        print(f"투자경고주")
    else:
        print(f"투자해도 됨")


def question_119():
    user_data = input("입력: ")
    fruit = {"spring": "strawberry", "summer": "tomato"}

    if user_data in fruit.keys():
        print(f"정답")
    else:
        print(f"오답")


def question_120():
    user_data = input("입력: ")
    fruit = {"spring": "strawberry", "summer": "tomato"}

    if user_data in fruit.values():
        print(f"정답")
    else:
        print(f"오답")


def question_121():
    user_data = input("입력: ")

    if user_data.islower():
        print(f"{user_data.upper()}")
    else:
        print(f"{user_data.lower()}")


def question_122():
    user_data = int(input("입력: "))

    if 81 <= user_data <= 100:
        print(f"score:{user_data}\ngrade: A")
    elif 61 <= user_data <= 80:
        print(f"score:{user_data}\ngrade: B")
    elif 41 <= user_data <= 60:
        print(f"score:{user_data}\ngrade: C")
    elif 21 <= user_data <= 40:
        print(f"score:{user_data}\ngrade: D")
    else:
        print(f"score:{user_data}\ngrade: E")


def question_123():
    user_data = input("입력: ")

    user_money = int(user_data.split(" ")[0])
    money = user_data.split(" ")[1]

    if money == "달러":
        print(f"{user_money * 1167}원")
    elif money == "위안":
        print(f"{user_money * 171}원")
    elif money == "엔":
        print(f"{user_money * 1.096}원")
    elif money == "유로":
        print(f"{user_money * 1268}원")
    else:
        print(f"변환 가능한 화폐가 아닙니다.")
"""
환율 = {"달러": 1167, 
        "엔": 1.096, 
        "유로": 1268, 
        "위안": 171}
user = input("입력: ")
num, currency = user.split()
print(float(num) * 환율[currency], "원")
"""


def question_124():
    num1 = int(input("입력: "))
    num2 = int(input("입력: "))
    num3 = int(input("입력: "))

    if num1 >= num2 and num1 >= num3:
        print(f"{num1}")
    elif num2 >= num1 and num2 >= num3:
        print(f"{num2}")
    else:
        print(f"{num3}")


def question_125():
    phone_number = input("입력: ")
    services = {
        "011": "SKT",
        "016": "KT",
        "019": "LGU",
        "010": "알수없음",
    }

    user_service = phone_number[:3]

    print(f"당신은 {services[user_service]} 사용자입니다.")


def question_126():
    post_number = input("입력: ")
    services = {
        "0": "강북구",
        "1": "강북구",
        "2": "강북구",
        "3": "도봉구",
        "4": "도봉구",
        "5": "도봉구",
        "6": "노원구",
        "7": "노원구",
        "8": "노원구",
        "9": "노원구",
    }

    user_post_name = post_number[2]

    print(f"{services[user_post_name]}")


def question_127():
    id_number = input("입력: ")
    services = {
        "1": "남자",
        "3": "남자",
        "2": "여자",
        "4": "여자",
    }

    user_sex = id_number.split("-")[1][0]

    print(f"{services[user_sex]}")


def question_128():
    id_number = input("입력: ")

    user_post = int(id_number.split("-")[1][-2:])
    print(user_post)
    if user_post <= 8:
        print(f"서울")
    elif 9 <= user_post <= 12:
        print(f"부산")
    else:
        print(f"그외지역")


def question_129():
    num = input("주민등록번호: ")
    calc1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
          int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10]) * 3 + \
          int(num[11]) * 4 + int(num[12]) * 5
    calc2 = 11 - (calc1 % 11)
    calc3 = str(calc2)

    if num[-1] == calc3[-1]:
        print("유효한 주민등록번호입니다.")
    else:
        print("유효하지 않은 주민등록번호입니다.")

import requests


def question_130():

    btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
    calc_price = int(btc['opening_price']) + (int(btc['max_price']) - int(btc['min_price']))

    if calc_price > int(btc['max_price']):
        print(f"상승장")
    else:
        print(f"하락장")

question_130()