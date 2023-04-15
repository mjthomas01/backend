# import module
import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'})

# user define function
# Scrape the data
def getdata(url):
	r = requests.get(url, headers=HEADERS)
	return r.text


def html_code(url):

	# pass the url
	# into getdata function
	htmldata = getdata(url)
	soup = BeautifulSoup(htmldata, 'html.parser')

	# display html code
	return (soup)


url = "https://www.amazon.in/Redmi-Storage-Qualcomm%C2%AE-SnapdragonTM-Included/dp/B09QS8V5N8/ref=pd_rhf_d_cr_s_pd_crcbs_sccl_1_3/258-2529433-7357058?pd_rd_w=8MAn8&content-id=amzn1.sym.5d8cdd8d-be53-4391-b82d-376d461d85f0&pf_rd_p=5d8cdd8d-be53-4391-b82d-376d461d85f0&pf_rd_r=AKEGXH3C49CXFD07SHPM&pd_rd_wg=uIRv3&pd_rd_r=c731deca-fe49-4368-b6f8-08f1ec4a8173&pd_rd_i=B09QS8V5N8&psc=1"

soup = html_code(url)
# print(soup)
def cus_rev(soup):
	# find the Html tag
	# with find()
	# and convert into string
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
