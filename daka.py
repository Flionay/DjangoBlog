# import request
data = {
	"collectChildId": "8a8a8a837f73e415017f88e830020bb3",
	"collectId": "8a8a8a837f73e415017f88e814700bb2",
	"data": {
		"cn": "是",
		"cn_text": "是",
		"jkmys": "绿色",
		"jkmys_text": "绿色",
		"mj": "否",
		"mj_text": "否",
		"stzk": "健康",
		"stzk_text": "健康",
		"szd": "370212",
		"szd_text": "山东 - 青岛市 - 崂山区",
		"tw": "37.2℃及以下",
		"tw_text": "37.2℃及以下",
		"ysbl": "否",
		"ysbl_text": "否",
		"yxgl": "否",
		"yxgl_text": "否",
		"zgfxq": "否",
		"zgfxq_text": "否"
	},
	"id": null
}
url = "https://gms.qust.edu.cn/efm/collection/submitCollectionData"


header = None
'''
POST /efm/collection/submitCollectionData HTTP/2
Host: gms.qust.edu.cn
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:98.0) Gecko/20100101 Firefox/98.0
Accept: */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
X-Requested-With: XMLHttpRequest
Content-Length: 456
Origin: https://gms.qust.edu.cn
Connection: keep-alive
Referer: https://gms.qust.edu.cn/login/enterMain/efm/collection/enterListMyCollection?categoryId=mrjkdk
Cookie: JSESSIONID=CF8807D284EFCD957D77E2890246A758; https%3A%2F%2Fgms.qust.edu.cn%2F=%7B%22admHistory%22%3A%7B%222019090015%22%3A%5B%7B%22url%22%3A%22login%2FenterMain%2Fefm%2Fcollection%2FenterListMyCollection%3FcategoryId%3Dmrjkdk%22%2C%22name%22%3A%22%E5%81%A5%E5%BA%B7%E6%89%93%E5%8D%A1%22%7D%2C%7B%22url%22%3A%22login%2FenterMain%2Fgrzxgl%2FenterGrzx%22%2C%22name%22%3A%22%E4%B8%AA%E4%BA%BA%E4%B8%AD%E5%BF%83%22%7D%5D%7D%7D
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
TE: trailers
'''