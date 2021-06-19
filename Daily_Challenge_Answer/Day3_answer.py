import os
import requests

def restart():
  answer = str(input("Do you want to start over? y/n ")).lower()
  if answer == "y" or answer =="n":
    if answer == "n":
        print("k. bye!")
        return
    elif answer == "y":
      main()
  else:
    print("That's not a valid answer")
    restart()


def main():
  os.system('clear')
  print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")
  urls = str(input()).lower().split(",")
  for url in urls:
    url = url.strip()
    if "." not in url:
      print(url, "is not a valid URL.")
    else:
      if "http" not in url:
        url = f"http://{url}"
      try:
        request = requests.get(url)
        if request.status_code == 200:
          print(url,"is up!")
        else:
          print(url, "is down!")
      except:
          print(url, "is down!")
  restart()


main()

'''
restart 함수와 main 함수 두 개를 작성하여 프로그램을 완성시킵니다.
def restart()
restart 함수는 사용자가 URL 검사를 모두 마친 뒤 계속 프로그램을 돌릴건지 여기서 끝낼건지 물어본 다음 사용자가 계속하길 원하면 프로그램은 다시 시작되고 끝내길 원하면 그대로 종료되는 기능을 합니다.
먼저 input() 내장함수를 이용해 사용자에게 프로그램 재시작 여부를 묻습니다.
사용자들이 모두 "y", 또는 "n" 이라는 대답을 정확히 하라는 법은 없습니다. 대문자로 대답할 수도 있고 전혀 다른 문자로 대답할 수도 있습니다. 이러한 상황들을 모두 생각하여 코드를 짜야합니다.
먼저 input() 으로 받은 값을 str() 을 이용해 타입을 모두 문자열로 바꿔준 다음 .lower() 내장 함수를 이용해 모두 소문자로 바꿔줍니다.
if문 을 이용해 사용자에게 입력받은 값이 "y" 이면 main() 함수를 실행시켜주고 "n" 이면 프로그램을 종료 시킵니다.
만약 사용자에게 입력받은 값이 전혀 생뚱맞은 값이면 restart() 함수를 다시 실행시켜 올바른 값을 받도록 합시다.
위와 같이 함수 내에서 같은 함수를 호출하는 것을 재귀호출(recursive call)이라 합니다.
def main()
main 함수는 URL들을 입력받아 콤마(,)로 구분하여 리스트에 저장 후 request.status_code 를 사용하여 해당 URL이 온라인인지 오프라인인지 검사하여 결과값을 출력해 주는 기능을 합니다.
os.system('clear') 구문은 프로그램을 실행시킬 때마다 콘솔 창을 깨끗이 지우는 역할을 합니다.
참고 문서 : os.system( command )
URL들을 입력 받기 위해 urls = str(input()).lower().split(",") 라고 코딩 해줍니다.
입력받은 것들을 str() 을 사용하여 모두 문자열로 변환시켜주고, .lower() 을 사용하여 문자열들을 모두 소문자로 변환 시켜준 다음 마지막으로 .split(",") 을 사용하여 콤마로 구분하여 urls 리스트에 각각 저장 시켜줍니다.
for url in urls : 문을 사용해 URL들이 저장된 urls 리스트를 차례로 둘러보며 url = url.strip() 을 사용하여 앞 뒤 공백들을 모두 제거해 줍니다.
공백을 모두 제거한 url이 URL 형식이 맞는지 if문 을 활용해 검사해줍시다.
모든 URL들은 뒤에 .com , .co.kr 등등 .이 붙습니다.
따라서 모든 url들은 " . "이 포함되어야 합니다.
if "." not in url : 이 조건문에 걸리면 URL 형식이 아닙니다.
또한 사용자들은 URL을 입력할 때 앞에 "http://" 를 빼먹는 경우가 있으므로 이러한 경우도 잡아내야 됩니다.
이것 역시 if "http" not in url : 을 사용하여 만약 "http"가 url에 포함되어있지 않으면 url = f"http://{url}" 을 사용하여 앞에 "http"를 추가해줍시다.
이제 모든 URL 형식 검사가 끝났으므로 url이 온라인 상태인지 오프라인 상태인지 확인만 하면 됩니다.
requests 라이브러리의 .status_code 를 이용하면 해당 url이 온라인 상태인지 오프라인 상태인지 알 수 있습니다.
단, 존재하지 않는 url일 경우 프로그램이 에러를 내므로 try-except 문을 사용하여 에러 처리를 해줍니다.
try 문 안에는 url의 주소로 GET 요청을 보냅니다.
그리고 만약 status_code == 200 이면 해당 url은 정상작동하는 온라인 상태이므로 해당 결과를 출력해 줍니다.
만약 status_code 가 200 이외의 값이라면 정상작동하지 않는 오프라인 상태이므로 해당하는 결과를 출력해 줍니다.
except 문은 만약 프로그램이 에러가 나면 에러메세지 대신 except 문 안에 있는 코드를 실행합니다.
에러가 나면 정상작동하지 않는 상태와 같은 메세지를 출력 해줍니다.
'''