from downloader import Downloader
import os

cookie = """
"device_session_id=84f9de9b-799e-410a-9694-abadea4700d4; first_landing=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26referrer%3D%26referring_username%3D; G_ENABLED_IDPS=google; PHPSESSID=e730c5a079a4a9c7586db9cf9ed545f0; show-like-copy=0; YII_CSRF_TOKEN=ZXBFWXZGMUlnSlgzdkhxSGFaZUtRcUFkbUpqb1RsZ2sKoY5lik2tJi3CJOPH1vgqsmGMkUhgf93TFe4lJReIgg%3D%3D; visitor_tracking=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26utm_term%3D%26referrer%3D%26referring_username%3D; skillshare_user_=c6db6abe4b62eaaa26fef0d6e5fae7e4c4b37931a%3A4%3A%7Bi%3A0%3Bs%3A8%3A%2216206803%22%3Bi%3A1%3Bs%3A32%3A%22vmitewnthuteljgbmm%40miucce.online%22%3Bi%3A2%3Bi%3A2592000%3Bi%3A3%3Ba%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A8%3A%2246581319%22%3Bs%3A10%3A%22login_time%22%3Bs%3A19%3A%222020-10-24%2017%3A07%3A50%22%3Bs%3A10%3A%22touch_time%22%3Bs%3A19%3A%222020-10-24%2017%3A08%3A43%22%3B%7D%7D; loc=%7B%22lat%22%3A%2240.7589%22%2C%22lng%22%3A%22-73.979%22%2C%22cid%22%3A%2231%22%2C%22city_name%22%3A%22Manhattan%22%2C%22city_district%22%3A%22%22%2C%22region%22%3Anull%2C%22region_code%22%3Anull%2C%22country_code%22%3A%22US%22%2C%22country%22%3A%22United%20States%22%7D; __stripe_mid=8ab9033c-fd50-4347-814c-135346acaf87b3995b; __stripe_sid=c25b2e9c-baf5-4085-a036-090db2c1df59f4ae44"
"""

dl = Downloader(cookie=cookie)

with open("urls.txt", "r") as file:
    for lineNum, line in enumerate(file):
        if line.strip() == "":
            continue
        dl.download_course_by_url(line.rpartition(" ")[2] if " " in line else line)
        print("Ripping line " + str(lineNum))




