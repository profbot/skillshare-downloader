from downloader import Downloader
import os

cookie = """
"device_session_id=84f9de9b-799e-410a-9694-abadea4700d4; first_landing=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26referrer%3D%26referring_username%3D; G_ENABLED_IDPS=google; visitor_tracking=utm_campaign%3Dstudent-referral-orientation%26utm_source%3DShortUrl%26utm_medium%3Dstudent-referral-general%26utm_term%3D%26referrer%3D%26referring_username%3D6003006; PHPSESSID=6a820a18ab99332812b219bb8f618eba; show-like-copy=0; YII_CSRF_TOKEN=RlFNVUF1V1BjTzVXNlViejVqbEdoRXRiaHJCV291SkWh9YBWKWKHvhmJq41tNRkAfUBzoAEo0EmKcW0ZXwOq3g%3D%3D; ss-ref=%7B%22student%22%3A%226519811%22%7D; skillshare_user_=b42a4c02ff6b46cefd030f5489c2e679997449b0a%3A4%3A%7Bi%3A0%3Bs%3A7%3A%226203071%22%3Bi%3A1%3Bs%3A20%3A%22sklfnpzzo%40tryzoe.com%22%3Bi%3A2%3Bi%3A2592000%3Bi%3A3%3Ba%3A3%3A%7Bs%3A8%3A%22username%22%3Bs%3A7%3A%224765911%22%3Bs%3A10%3A%22login_time%22%3Bs%3A19%3A%222020-11-24%2022%3A45%3A47%22%3Bs%3A10%3A%22touch_time%22%3Bs%3A19%3A%222020-11-24%2022%3A46%3A09%22%3B%7D%7D; __stripe_mid=8ab9033c-fd50-4347-814c-135346acaf87b3995b; __stripe_sid=2775b5c1-9dad-4ed8-b8f8-02a4c750d62078c06c; ss-subscription-coupon=referral2m"
"""

dl = Downloader(cookie=cookie)

with open("urls1.TXT", "r") as file:
    for lineNum, line in enumerate(file):
        if line.strip() == "":
            continue
        dl.download_course_by_url(line.rpartition(" ")[2] if " " in line else line)
        print("Ripping line " + str(lineNum))




