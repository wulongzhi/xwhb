# 新闻汇编

``` Shell
python -m venv .venv

.\.venv\Scripts\Activate.ps1 # PowerShell
source .venv/Scripts/activate # Git Bash

deactivate
```

``` Shell
pip list

pip install scrapy
```

``` Shell
scrapy startproject xwhb .

scrapy crawl xinhua
scrapy crawl xinhua -O xinhua.json
scrapy crawl xinhua -o xinhua.jsonl
```
