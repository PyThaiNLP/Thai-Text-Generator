# -*- coding: utf-8 -*-
from pathlib import Path
import os
from tqdm import tqdm
import requests
from collections import defaultdict
import zipfile

home = str(Path.home())
path = os.path.join(home, "thaitextgenerator")
Path(path).mkdir(parents=True, exist_ok=True)

def download(url, p):
    yn = input("you want to download %s ? (y Yes, n is No) ".format(url))
    if yn=="y":
        response = requests.get(url, stream=True) # by https://stackoverflow.com/a/10744565/11952699
        with open(p, "wb") as handle:
            for data in tqdm(response.iter_content()):
                handle.write(data)

def get_path(name)->str:
    return os.path.join(path, name)

def load_tnc_unigram()->dict:
    corpus_path = get_path("tnc_freq.txt")
    if Path(corpus_path).is_file()==False:
        download("https://github.com/korakot/thainlp/raw/master/tnc_freq.txt",corpus_path)
    data = defaultdict(int)
    with open(corpus_path,"r",encoding="utf-8") as f:
        for i in f.readlines():
            _temp = i.strip().split("\t")
            data[_temp[0]] = int(_temp[-1])
    return data

def load_tnc_bigram()->dict:
    corpus_path = get_path("201705_2gram.txt")
    if Path(corpus_path).is_file()==False:
        download("http://www.arts.chula.ac.th/ling/wp-content/uploads/tnc201705_2gram.zip",get_path("tnc201705_2gram.zip"))
        with zipfile.ZipFile(get_path("tnc201705_2gram.zip"),"r") as zip_ref:
            zip_ref.extractall(path)
    data = defaultdict(int)
    with open(corpus_path,"r",encoding="utf-8") as f:
        for i in f.readlines():
            _temp = i.strip().split("	")
            data[(_temp[0],_temp[1])] = int(_temp[-1])
    return data

def load_ttc_unigram()->dict:
    corpus_path = get_path("ttc_freq.txt")
    if Path(corpus_path).is_file()==False:
        download("https://github.com/korakot/thainlp/raw/master/ttc_freq.txt",corpus_path)
    data = defaultdict(int)
    with open(corpus_path,"r",encoding="utf-8") as f:
        for i in f.readlines():
            _temp = i.strip().split("\t")
            if _temp[0]!=" ":
                data[_temp[0]] = int(_temp[-1])
            else:
                data["<s/>"] = int(_temp[-1])
    return data