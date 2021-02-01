import requests as req
import xmltodict, json
import wget
import os
import random

logo = """•---------------•-------•--------------------•
| rule34-parser | v 0.1 | MIT License        |
•---------------•-------•--------------------•
| https://github.com/Hell13Cat/rule34-parser |
•--------------------------------------------•\n"""
root_dir = os.getcwd()
try:
    os.mkdir(root_dir + "/down")
except:
	pass
def download(url, filename):
	wget.download(url, filename)
	return filename

def dirs_create(name):
    root_dir = os.getcwd()
    try:
        os.mkdir(root_dir + "/down/" + name)
    except:
        pass

def load_url(url, tag):
    dirs_create(tag)
    root_dir = os.getcwd()
    filename = root_dir + "/down/" + tag + "/" + (url.split("/"))[-1]
    download(url, filename)

def get_json(url):
    cont = (req.get(url)).content
    o = xmltodict.parse(cont)
    return json.loads(json.dumps(o))

def list_tag(num, tag):
    tags = tag.replace("(", "%28").replace(")", "%29").replace(" ", "+")
    json_l = get_json("https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=" + str(num) + "&tags=" + tags)
    posts_all  = json_l["posts"]["post"]
    return_data = []
    for post in range(int(num)):
        return_data.append([json_l["posts"]["post"][post]["@tags"], json_l["posts"]["post"][post]["@file_url"]])
    return return_data

print(logo)
tag = input("TAG> ")
num = input("COUNTS> ")
os.system('cls' if os.name == 'nt' else 'clear')
print(logo+"Loading url's...")
list_url = list_tag(int(num), tag)
text_info = ""
count = 0
for one_url in list_url:
	os.system('cls' if os.name == 'nt' else 'clear')
	count += 1
	print(logo+"File "+str(count)+"/"+str(len(list_url)))
	load_url(one_url[1], tag)
	text_info = text_info + "> " + one_url[1] + "\n" + one_url[0] + "\n\n"
os.system('cls' if os.name == 'nt' else 'clear')
open("./down/"+tag+" - "+str(random.randrange(1, 25000, 1))+".txt", "w").write(text_info)
print(logo+str(len(list_url))+" files downloads")