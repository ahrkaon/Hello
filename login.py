fail_count = 0
question = '당신의 생일은?'
answer = ''

print(question)
answer = input("보안질문에 대한 답을 정하세요 : ")
while True:
    id = input("아이디를 입력하세요 : ")
    pw = input("비밀번호를 입력하세요 : ")
    
    if 'superman' == id and '1234' == pw:
        print("환영합니다")
        break
    else:
        fail_count = fail_count + 1
        print('로그인 {}회 시도했습니다'.format(fail_count))
        
        if fail_count >= 3:
            print("본인확인이 필요합니다")
            print(question)
            a = input("질문의 답을 하시오 : ")
            if answer == a:
                print("비밀번호는 1234입니다")
            else:
                print("시스템을 종료합니다")
                break
        print()
    
        