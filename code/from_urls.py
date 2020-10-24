from downloader import Downloader
import os

cookie = """
"device_session_id=84f9de9b-799e-410a-9694-abadea4700d4; first_landing=utm_campaign%3D%26utm_source%3D%28direct%29%26utm_medium%3D%28none%29%26referrer%3D%26referring_username%3D; G_ENABLED_IDPS=google; show-like-copy=1; ss-ref=%7B%22teacher%22%3A%7B%226595003%22%3A%7B%22classId%22%3Anull%2C%22referralType%22%3A%22affiliate%22%7D%7D%7D; PHPSESSID=4a58bbdb178dc554abc67ddeec6d4a2a; YII_CSRF_TOKEN=S001eUx6bG9wMTJwWENXbFNGdFFEMVpBVVl4Y2dBSEeC9AQw6YnuZCVNOKVMejqVoULsXubiurRkJb3Bu7TgWA%3D%3D; visitor_tracking=utm_campaign%3Dstudent-referral-settings%26utm_source%3DShortUrl%26utm_medium%3Dstudent-referral-general%26referrer%3D%26referring_username%3D6519811; skillshare_user_=0fdb404df79e1d3bc6d1bd33280eaf6931e2d176a%3A4%3A%7Bi%3A0%3Bs%3A8%3A%2215662510%22%3Bi%3A1%3Bs%3A32%3A%22crgpxvexfpysqazncc%40twzhhq.online%22%3Bi%3A2%3Bi%3A2592000%3Bi%3A3%3Ba%3A2%3A%7Bs%3A8%3A%22username%22%3Bs%3A9%3A%22892389830%22%3Bs%3A10%3A%22login_time%22%3Bs%3A19%3A%222020-09-19%2019%3A56%3A18%22%3B%7D%7D; loc=%7B%22lat%22%3A%2253.4914%22%2C%22lng%22%3A%22-113.48%22%2C%22cid%22%3A%220%22%2C%22city_name%22%3A%22Edmonton%22%2C%22city_district%22%3A%22%22%2C%22region%22%3Anull%2C%22region_code%22%3Anull%2C%22country_code%22%3A%22CA%22%2C%22country%22%3A%22Canada%22%7D; CAPTIONS=off; __stripe_mid=8ab9033c-fd50-4347-814c-135346acaf87b3995b"
"""

dl = Downloader(cookie=cookie)

with open("urls.txt", "r") as file:
    for lineNum, line in enumerate(file):
        if line.strip() == "":
            continue
        dl.download_course_by_url(line.rpartition(" ")[2] if " " in line else line)
        print("Ripping line " + str(lineNum))



os.system('rclone -P copy "./data/" "euromisc:/Prof_Skillshare/"')
