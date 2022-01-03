import urllib.request
from fake_useragent import UserAgent

# UserAgent 객체 생성
agent = UserAgent()

# urllib은 urlretrieve함수를 이용해서 한 번에 파일로 저장
url = ''

# 파일을 저장할 경로
path = './Crawling/download.jpg'

# opener 객체를 생성해서 헤더를 먼저 수정해줍니다
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', agent.chrome)]
urllib.request.install_opener(opener)

# 이제는 urlretrieve를 이용해서 다운로드 한 파일을 바로 생성할 수 있습니다
urllib.request.urlretrieve( url, path )