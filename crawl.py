import os
from datetime import datetime
from pytz import timezone
from yes24 import parse,extract_book_data
from github_utils import get_github_repo,upload_github_issue

if __name__=="__main__":
    access_token=os.environ['MY_GITHUB_TOKEN']
    repository_name='githubAction'

    seoul_timezone=timezone('Asia/Seoul')
    today=datetime.now(seoul_timezone)
    today=today.strftime('%Y년 %m월 %d일')

    url='http://www.yes24.com/24/Category/NewProductList/001001019001?sumGb=04'
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

    soup=parse(url,headers)

    issue_title=f"yes24 신간 인문 도서 알림({today})"
    upload_contents=extract_book_data(soup)
    repo=get_github_repo(access_token,repository_name)
    upload_github_issue(repo,issue_title,upload_contents)
    print("done.")