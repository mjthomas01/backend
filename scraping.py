# import module
import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'})

def getdata(url):
	r = requests.get(url, headers=HEADERS)
	return r.text


def html_code(url):


	htmldata = getdata(url)
	soup = BeautifulSoup(htmldata, 'html.parser')
	return (soup)


url = "https://www.amazon.in/JBL-Customized-Talk-Thru-FastPair-Warranty/dp/B0BHTK78SS/?_encoding=UTF8&pd_rd_w=1M4LI&content-id=amzn1.sym.6aeb164c-387d-440e-8808-65edf45c4683&pf_rd_p=6aeb164c-387d-440e-8808-65edf45c4683&pf_rd_r=EZ8FP4P24GAB3F9213WG&pd_rd_wg=rvOMi&pd_rd_r=c2aa4562-66e3-4e72-b623-41232819f89d&ref_=pd_gw_ci_mcx_mr_hp_atf_m"

soup = html_code(url)
# print(soup)
def cus_rev(soup):
	data_str = ""

	for item in soup.find_all("div", class_="a-expander-content reviewText review-text-content a-expander-partial-collapse-content"):
		data_str = data_str + item.get_text()

	result = data_str.split("\n")
	return (result)


rev_data = cus_rev(soup)
rev_result = []
for i in rev_data:
	if i == "":
		pass
	else:
		rev_result.append(i)
print(rev_result)
