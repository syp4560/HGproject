import requests
res = requests.get("http://www.bookisland.co.kr/siteinfo/sell.html?num=3")
print("응답코드:", res.status_code)