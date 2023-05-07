import requests
import os
from bs4 import BeautifulSoup

url = "http://www.ansible.com.cn/"
folder = 'txt/ansible'

res = requests.get(url)

soup = BeautifulSoup(res.text, 'html.parser')

# 如果当前目录没有ansible目录，则创建
if not os.path.exists(folder):
    os.mkdir(folder)

# 获取所有class为reference的a标签
links = soup.select('a.reference')

for link in links:
    inner_url = url + link['href']
    # 过滤掉url中包含#的链接
    if '#' in inner_url:
        continue

    # 读取文章内容，utf-8编码
    html_content = requests.get(inner_url).content
    
    inner_soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')

    # 获取文章内容
    content = inner_soup.select('div.section')[0].text
    content = content.replace('¶', '')
    
    # 获取文章标题
    title = inner_soup.select('h1')[0].text
    # 去掉标题中的‘¶’符号
    title = title.replace('¶', '')

    # 保存到文件中, utf-8编码
    with open(folder + '/' + title + '.txt', 'w', encoding='utf-8') as f:
        f.write(content)
        f.write('\n\n')