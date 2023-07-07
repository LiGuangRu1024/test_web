# 时间：2023/7/4 17:00
# 人员: 莉光哈哈哈
import requests
from jsonpath import jsonpath
from hamcrest import *
from requests.auth import HTTPBasicAuth


class TestDemo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.get("http://httpbin.testing-studio.com/get", params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post("http://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post("http://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()["json"]["level"] == 1

    def test_hogwarts_json(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert r.json()["category_list"]["categories"][0]["name"] == "提问区"
        assert jsonpath(r.json(), "$..name")[0] == "提问区"
        print(jsonpath(r.json(), "$..name"))

    def test_hamcrest(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert_that(r.json()["category_list"]["categories"][0]["name"], equal_to("提问区"))

    def test_cookie(self):
        # url = "http://httpbin.testing-studio.com/cookies"
        # header = {
        #     "Cookie": "hogwarts=school",
        #     'User-Agent': 'hogwarts'
        # }
        # r = requests.get(url=url, headers=header)
        # print(r.request.headers)
        url = "http://httpbin.testing-studio.com/cookies"
        header = {
            'User-Agent': 'hogwarts'
        }
        cookie_data = {
            "hogwarts": "school",
            "teacher": "AD"
        }
        r = requests.get(url=url, headers=header, cookies=cookie_data)
        print(r.request.headers)

    def test_auth(self):
        r = requests.get(url="http://httpbin.testing-studio.com/basic-auth/uesr/123456", auth=HTTPBasicAuth("uesr", "123456"))
        print(r)
        print(r.text)