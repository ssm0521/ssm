movies = ['해리포터', '슈퍼맨', '어벤져스', '기생충']
print()
print("********상영 중인 영화********")
for item in movies:#영화목록 출력
    print(item)
print("******************************")
print("예매하실 영화를 선택해주세요. :")
choice = input()
while choice not in movies:#리스트에 없는 값을 넣는 경우
    print("예매할 수 없는 영화입니다.")
    choice = input()
print("예매하실 영화로 ",choice,"을(를) 선택하셨습니다.")

aa = False #인원수 확인하기 위해 aa에 False를 넣습니다.

while(not aa):
    teen = int(input("청소년 인원 수를 입력해주세요: "))
    teensum = teen * 7000
    if teen < 0:
        print("잘못 입력하셨습니다. 다시 입력해주세요")
        teen = input()
    else:
        print("청소년표 %d개 가격은 %d원입니다."%(teen, teensum))

    adult = int(input("성인 인원 수를 입력해주세요: "))
    adultsum = adult*12000
    if adult < 0:
        print("잘못 입력하셨습니다. 다시 입력해주세요")
        adult = input()
    else:
        print("성인표 %d개 가격은 %d원입니다."%(adult, adultsum))
        aa = True

    if (teen + adult) == 0:#청소년, 성인 둘 다 0을 선택했을 때 취소
        print("예매를 취소합니다.")
        aa = True

people = teen + adult
allsum = teensum + adultsum
final = True

print("************최종 예매 확인************")
print("영화 제목 : %s"%choice)
print("관람 인원 : %d명"%people)
print("청소년 : %d명"%teen)
print("성인 : %d명"%adult)
print("청소년 %d명 성인 %d명 가격은 %d입니다."%(teen, adult, allsum))
print("**************************************")

print("예매하시겠습니까?(y/n): ")
last = input()
while final:
    if last == 'y':
        print("감사합니다. 즐거운 하루되세요!!")
        break
    elif last == 'n':
        print("예매가 취소되었습니다.")
        break
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
    
