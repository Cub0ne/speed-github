
import requests
from bs4 import BeautifulSoup
import re 
import shutil
import os 
import datetime

# 需要获取ip的网址

sites =[ 
	"github.com",
	"www.github.com",
	"github.global.ssl.fastly.net",
	"assets-cdn.github.com",
	"documentcloud.github.com",
	"gist.github.com",
	"help.github.com",
	"nodeload.github.com",
	"raw.github.com",
	"status.github.com",
	"training.github.com",
	"ithubusercontent.com",
	"codeload.github.com",
	"avatars0.githubusercontent.com",
	"avatars1.githubusercontent.com",
	"avatars2.githubusercontent.com",
	"avatars3.githubusercontent.com",
	"avatars4.githubusercontent.com",
	"avatars5.githubusercontent.com",
	"avatars6.githubusercontent.com",
	"avatars7.githubusercontent.com",
	"avatars8.githubusercontent.com",
	"camo.githubusercontent.com",
	"cloud.githubusercontent.com",
	"gist.githubusercontent.com",
	"marketplace-screenshots.githubusercontent.com",
	"raw.githubusercontent.com",
	"repository-images.githubusercontent.com",
	"user-images.githubusercontent.com"
	]
	
addr2ip = {}

#获取网址的ip

def getIp(siteAdd):
	
	engine = "https://ipaddress.com/search/"
	headers = headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebkit/737.36(KHTML, like Gecke) Chrome/52.0.2743.82 Safari/537.36','Host':'movie.douban.com'
}	

	url = "http://ip.tool.chinaz.com/"+siteAdd
	try:
		res = requests.get(url)
		soup=BeautifulSoup(res.text,'html.parser')
		result=soup.find_all('span', class_="Whwtdhalf w15-0")
		trueip = None
		for c in result:
			ip = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", c.text)
			if len(ip)!= 0:
				trueip = ip[0] 
	except:
		print("查询"+siteAdd+" 时出现错误")
		return None
	
	return trueip	
	

# 生成数据表
def generateDict():

	for site in sites:
		ip = getIp(site)
		if ip != None:
			addr2ip[site] = ip
			print(ip+"\t"+site)
		

def chachong(line):
	flag = False
	for site in sites:
		if site in line:
			flag = flag or True
		else:
			flag = flag or False
	return flag 
	

# 更新host, 并刷新本地DNS

def updateHost():
	generateDict()
	today = datetime.date.today()
	f = open("hosts", "w")

	f.write("\n\n #*********************github "+str(today) +" 更新********************\n")
	for key in addr2ip:
		f.write(addr2ip[key]+"\t"+key+"\n")
	f.close()
	
updateHost()	