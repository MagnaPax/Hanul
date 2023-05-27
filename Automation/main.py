import internet_banking_hanul as banking

if __name__ == '__main__':
    print('시작')

    url = "https://www.hanulbanking.co.kr"
    url = "https://www.google.com"


    bank = banking.internetBanking()
    bank.setURL(url)
    result = bank.checkConnection()

    if result == False:
        print('서버 연결에 실패했습니다.')
        exit()

    print('서버 연결에 성공했습니다.')
