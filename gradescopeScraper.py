import requests
from bs4 import BeautifulSoup
from pprint import pprint

def countSubmissions(resp):
    soup = BeautifulSoup(resp.text, "html.parser")

    rows = [row for row in soup.find_all("tr")]
    tas = {}
    for row in rows[1:]:
        items = [item.text for item in row.find_all("td")]
        if items[2]:
            name = items[2]
            count = tas.get(name, 0)
            tas[name] = count + 1
        else:
            continue
    pprint(tas)
   

def getResponse(curl):
    cookies = curl["cookies"]
    headers = curl["headers"]
    url = curl["url"]
    response = requests.get(url=url, cookies=cookies, headers=headers)
    return response
    
if __name__ == "__main__":
    taCurl = {
        "cookies": {
            'saml_idp_logout_redirect_url': 'https%3A%2F%2Flogin.gatech.edu%2Fcas%2Flogout',
            '__stripe_mid': 'ac55a5e8-72ce-45a4-ac06-decf0d86e12ffeeb52',
            '_ga_7Z1WNTTCRG': 'GS1.1.1692733349.35.1.1692733365.0.0.0',
            '_ga': 'GA1.2.1791260984.1663871501',
            '_gid': 'GA1.2.522623943.1698977036',
            'signed_token': 'cm0rL0VyNk9oL2JzQWc0dmtKaHpzMXowdTVQNkZiUUIyaWtBaTZVdWxmZz0tLU9LV2NJZTQrNGV4VThuNFR4WDlSbHc9PQ%3D%3D--3f8b85e24789301f2c7bd7b484b3e45430f848b6',
            'remember_me': 'QWhPbUVQdVVxSU5WcytoWnNZOGhsZz09LS0yNTZyYUQrSEQyNGtLYUYwc1RnL0J3PT0%3D--36cea7bf1946a3cefed922be2d102d1c8443da8a',
            'apt.sid': 'AP-1BQVLBSZC216-2-1698977050893-31114911',
            'apt.uid': 'AP-1BQVLBSZC216-2-1698977050895-71452542.0.2.409a23b4-ab5f-44cb-ab4f-a98ec46d9e75',
            '__stripe_sid': '378d37ce-eaee-4aa2-b17d-5a9c9c5cb6b21dfee4',
            '_gradescope_session': 'WGZPSk12RG9NdXZ6RmM5eUhGYlcwN2lqZVU5Z0FVRkdJN0RkOEU3SlV6dklUTkpOZ2tuWWwrMVJlVXhEcXQ5NVFvTW04NjU5SS9yUjBYRXh1aVRBMkRFT0ZONzlMZ1pSREUyMUZrNGhZN1U5cFlVaTNLUEc4R1orSUh4b2lJZHFzLy9XZFhYOGkwR2dGZ0ZoOHR4V1pVTFlyd09nWTVEME5ZQ2MwVzBqYzVaSTdQckE2bXA1VDhSVkdRaWc1R3Vva1ZyZnI0dy9VZzAyenFiSGhhdkNCRXI5c05TM3QyQTJ1WHFIRWdVdDNEREtMSVJmdG01WW1VSGNySUgwdDFOa3hVQjluSU1jTFVzS1l6cEhvQmQ1R0p4dnlabUZYMWFSbFJSbDlXR0oxN3BlbzgwTDczc3hEaHZnSEU5T2hIeldndklBR2RoN0V5N0FuQmpqYTlkMXc2dGZEZDhneHcxUytLMFhvNmhQc1hTeENGUm9iR2c2V2tKeDdrMm1OWFlITDRxbUs0TDJ1dDBnWEJRdjBZZWJRWFRGUGlkOVZhNjcxZitlclZQeVFnN0psdkR1dVFvS2cxdkY3VHh5VEZMdXB3NUVEeHBvQzJsTXk2TURvemZMRkM2UlZiZGc4MGJ2cG41cFNWTkNWTTkxdUxqenRLcllMdDkrRWRIU3A2SjEwUzFBZVB2QTg4RFNlLzdaVXdOdVRmK1MxRHZyNVk2bjNkNTBuSDJEVkNrOWhlN05NQUFyMjMyMGhndWlITm02LS05WHV3TWFwNzM1a0xmS0tydUp4aXpRPT0%3D--c008c111f18c043a3187b7ee0d6ebab521cfa96d',
        },
        "headers": {
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': 'saml_idp_logout_redirect_url=https%3A%2F%2Flogin.gatech.edu%2Fcas%2Flogout; __stripe_mid=ac55a5e8-72ce-45a4-ac06-decf0d86e12ffeeb52; _ga_7Z1WNTTCRG=GS1.1.1692733349.35.1.1692733365.0.0.0; _ga=GA1.2.1791260984.1663871501; _gid=GA1.2.522623943.1698977036; signed_token=cm0rL0VyNk9oL2JzQWc0dmtKaHpzMXowdTVQNkZiUUIyaWtBaTZVdWxmZz0tLU9LV2NJZTQrNGV4VThuNFR4WDlSbHc9PQ%3D%3D--3f8b85e24789301f2c7bd7b484b3e45430f848b6; remember_me=QWhPbUVQdVVxSU5WcytoWnNZOGhsZz09LS0yNTZyYUQrSEQyNGtLYUYwc1RnL0J3PT0%3D--36cea7bf1946a3cefed922be2d102d1c8443da8a; apt.sid=AP-1BQVLBSZC216-2-1698977050893-31114911; apt.uid=AP-1BQVLBSZC216-2-1698977050895-71452542.0.2.409a23b4-ab5f-44cb-ab4f-a98ec46d9e75; __stripe_sid=378d37ce-eaee-4aa2-b17d-5a9c9c5cb6b21dfee4; _gradescope_session=WGZPSk12RG9NdXZ6RmM5eUhGYlcwN2lqZVU5Z0FVRkdJN0RkOEU3SlV6dklUTkpOZ2tuWWwrMVJlVXhEcXQ5NVFvTW04NjU5SS9yUjBYRXh1aVRBMkRFT0ZONzlMZ1pSREUyMUZrNGhZN1U5cFlVaTNLUEc4R1orSUh4b2lJZHFzLy9XZFhYOGkwR2dGZ0ZoOHR4V1pVTFlyd09nWTVEME5ZQ2MwVzBqYzVaSTdQckE2bXA1VDhSVkdRaWc1R3Vva1ZyZnI0dy9VZzAyenFiSGhhdkNCRXI5c05TM3QyQTJ1WHFIRWdVdDNEREtMSVJmdG01WW1VSGNySUgwdDFOa3hVQjluSU1jTFVzS1l6cEhvQmQ1R0p4dnlabUZYMWFSbFJSbDlXR0oxN3BlbzgwTDczc3hEaHZnSEU5T2hIeldndklBR2RoN0V5N0FuQmpqYTlkMXc2dGZEZDhneHcxUytLMFhvNmhQc1hTeENGUm9iR2c2V2tKeDdrMm1OWFlITDRxbUs0TDJ1dDBnWEJRdjBZZWJRWFRGUGlkOVZhNjcxZitlclZQeVFnN0psdkR1dVFvS2cxdkY3VHh5VEZMdXB3NUVEeHBvQzJsTXk2TURvemZMRkM2UlZiZGc4MGJ2cG41cFNWTkNWTTkxdUxqenRLcllMdDkrRWRIU3A2SjEwUzFBZVB2QTg4RFNlLzdaVXdOdVRmK1MxRHZyNVk2bjNkNTBuSDJEVkNrOWhlN05NQUFyMjMyMGhndWlITm02LS05WHV3TWFwNzM1a0xmS0tydUp4aXpRPT0%3D--c008c111f18c043a3187b7ee0d6ebab521cfa96d',
            'Referer': 'https://www.gradescope.com/courses/568977/assignments/3499140/grade',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
        },
        "url": 'https://www.gradescope.com/courses/568977/questions/28201238/submissions'
    }

    taResp = getResponse(taCurl)
    countSubmissions(taResp)
   