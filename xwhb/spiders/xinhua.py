import re
import scrapy


class XinhuaSpider(scrapy.Spider):
    name = "xinhua"
    start_urls = ["https://www.news.cn/"]

    rep_bgn = r"^https?://www\.news\.cn"
    rep_end = r"/\d{8}/[0-9a-f]{32}/c\.html$"

    # https://www.news.cn/20260214/66bdf8466f1d4290b629f3f8052227e2/c.html
    reo_default = re.compile(rep_bgn + rep_end)
    # https://www.news.cn/world/20260220/38be488821ae4d51a3435e3729bd50da/c.html
    reo_world = re.compile(rep_bgn + r"/world" + rep_end)
    # https://www.news.cn/politics/20260221/3e8212c297e74458b5c3d6a5a3ff2800/c.html
    reo_politics = re.compile(rep_bgn + r"/politics" + rep_end)
    # https://www.news.cn/politics/leaders/20260221/17558c6bddc345e4b237004b967d2638/c.html
    reo_leaders = re.compile(rep_bgn + r"/politics/leaders" + rep_end)
    # https://www.news.cn/photo/20260221/7a9f15d312c64857af84e6941c94de7a/c.html
    reo_photo = re.compile(rep_bgn + r"/photo" + rep_end)
    # https://www.news.cn/sports/20260221/56bec27aa11440f48b542858fe120f06/c.html
    reo_sports = re.compile(rep_bgn + r"/sports" + rep_end)
    # https://www.news.cn/tech/20260220/ed77add1ce12410594f9801d7ccac191/c.html
    reo_tech = re.compile(rep_bgn + r"/tech" + rep_end)
    # https://www.news.cn/local/20260221/91b475f81c324613a2db8e10a91c9676/c.html
    reo_local = re.compile(rep_bgn + r"/local" + rep_end)
    # https://www.news.cn/legal/20260221/d06b83e0b056495591b411ed25614203/c.html
    reo_legal = re.compile(rep_bgn + r"/legal" + rep_end)
    # http://www.news.cn/government/20260221/0659934e1c29441eaecc374540fb6ea4/c.html
    reo_government = re.compile(rep_bgn + r"/government" + rep_end)
    # https://www.news.cn/fortune/20260221/ebaf67de45d047f7b701a09c8871eb12/c.html
    reo_fortune = re.compile(rep_bgn + r"/fortune" + rep_end)
    # https://www.news.cn/gangao/20260221/5391ff060d1548bd892c86b53c3900b2/c.html
    reo_gangao = re.compile(rep_bgn + r"/gangao" + rep_end)
    # https://www.news.cn/comments/20260214/61ec77e436254793bebf3a13434e8d36/c.html
    reo_comments = re.compile(rep_bgn + r"/comments" + rep_end)
    # https://www.news.cn/talking/20260213/fea0a0caa60042348f6615eba8a307b6/c.html
    reo_talking = re.compile(rep_bgn + r"/talking" + rep_end)
    # https://www.news.cn/ci/20260214/5db6d6fdd66a4efbbbe2ea5a4e80b40f/c.html
    reo_ci = re.compile(rep_bgn + r"/ci" + rep_end)
    # https://www.news.cn/sikepro/20260211/bb526bc76d1a469683c7c8df0d8b2221/c.html
    reo_sikepro = re.compile(rep_bgn + r"/sikepro" + rep_end)
    # https://education.news.cn/20260212/c809844550314fd399cb467b07bf0229/c.html
    reo_education = re.compile(r"^https?://education\.news\.cn" + rep_end)
    # https://www.news.cn/money/20260213/678ad1c9a71b418ab1e287e8f755d1ef/c.html
    reo_money = re.compile(rep_bgn + r"/money" + rep_end)
    # https://www.news.cn/auto/20260210/53a7f3b999d0450b91caa944f393beec/c.html
    reo_auto = re.compile(rep_bgn + r"/auto" + rep_end)
    # https://www.news.cn/sci-tech/20260213/529ac9ff7be34e57aad1b2f57103b073/c.html
    reo_sci_tech = re.compile(rep_bgn + r"/sci-tech" + rep_end)
    # https://www.news.cn/digital/20260210/26222983aa794e83bfd6f980bc87e01b/c.html
    reo_digital = re.compile(rep_bgn + r"/digital" + rep_end)
    # https://www.news.cn/food/20260206/e804f44585c54273ac9538304e69c403/c.html
    reo_food = re.compile(rep_bgn + r"/food" + rep_end)
    # https://www.news.cn/info/20260202/b09e3f53e82b433d9b293e8cff0b8d87/c.html
    reo_info = re.compile(rep_bgn + r"/info" + rep_end)
    # https://www.news.cn/house/20260212/c25500e7ab9e4226b97a54be0dd5793f/c.html
    reo_house = re.compile(rep_bgn + r"/house" + rep_end)
    # https://www.news.cn/energy/20260209/74bb9cae1c92464291ed07247d024037/c.html
    reo_energy = re.compile(rep_bgn + r"/energy" + rep_end)
    # https://www.news.cn/travel/20260214/299d6f4f6e084cd6b2a5a97935d52814/c.html
    reo_travel = re.compile(rep_bgn + r"/travel" + rep_end)
    # https://www.news.cn/culture/20260213/be38059084f241c89cf36031a80d7680/c.html
    reo_culture = re.compile(rep_bgn + r"/culture" + rep_end)
    # https://www.news.cn/fashion/20260213/2920ab209aed420e99aa72893b94dcdf/c.html
    reo_fashion = re.compile(rep_bgn + r"/fashion" + rep_end)
    # https://city.news.cn/20260213/63d864a228a9467aa60ed9becf26752e/c.html
    reo_city = re.compile(r"^https?://city\.news\.cn" + rep_end)
    # https://www.news.cn/shuhua/20260213/99b87420bd2a44b391338d069e9dfe77/c.html
    reo_shuhua = re.compile(rep_bgn + r"/shuhua" + rep_end)

    reo_link = re.compile(r"^https?://.+\.news\.cn/")

    def parse(self, response):
        for href in response.css("a::attr(href)").getall():
            abs_url = response.urljoin(href)

            if abs_url.endswith("/c.html"):
                if self.reo_default.match(abs_url):
                    yield {"default": abs_url}
                elif self.reo_world.match(abs_url):
                    yield {"world": abs_url}
                elif self.reo_politics.match(abs_url):
                    yield {"politics": abs_url}
                elif self.reo_leaders.match(abs_url):
                    yield {"leaders": abs_url}
                elif self.reo_photo.match(abs_url):
                    yield {"photo": abs_url}
                elif self.reo_sports.match(abs_url):
                    yield {"sports": abs_url}
                elif self.reo_tech.match(abs_url):
                    yield {"tech": abs_url}
                elif self.reo_local.match(abs_url):
                    yield {"local": abs_url}
                elif self.reo_legal.match(abs_url):
                    yield {"legal": abs_url}
                elif self.reo_government.match(abs_url):
                    yield {"government": abs_url}
                elif self.reo_fortune.match(abs_url):
                    yield {"fortune": abs_url}
                elif self.reo_gangao.match(abs_url):
                    yield {"gangao": abs_url}
                elif self.reo_comments.match(abs_url):
                    yield {"comments": abs_url}
                elif self.reo_talking.match(abs_url):
                    yield {"talking": abs_url}
                elif self.reo_ci.match(abs_url):
                    yield {"ci": abs_url}
                elif self.reo_sikepro.match(abs_url):
                    yield {"sikepro": abs_url}
                elif self.reo_education.match(abs_url):
                    yield {"education": abs_url}
                elif self.reo_money.match(abs_url):
                    yield {"money": abs_url}
                elif self.reo_auto.match(abs_url):
                    yield {"auto": abs_url}
                elif self.reo_sci_tech.match(abs_url):
                    yield {"sci-tech": abs_url}
                elif self.reo_digital.match(abs_url):
                    yield {"digital": abs_url}
                elif self.reo_food.match(abs_url):
                    yield {"food": abs_url}
                elif self.reo_info.match(abs_url):
                    yield {"info": abs_url}
                elif self.reo_house.match(abs_url):
                    yield {"house": abs_url}
                elif self.reo_energy.match(abs_url):
                    yield {"energy": abs_url}
                elif self.reo_travel.match(abs_url):
                    yield {"travel": abs_url}
                elif self.reo_culture.match(abs_url):
                    yield {"culture": abs_url}
                elif self.reo_fashion.match(abs_url):
                    yield {"fashion": abs_url}
                elif self.reo_city.match(abs_url):
                    yield {"city": abs_url}
                elif self.reo_shuhua.match(abs_url):
                    yield {"shuhua": abs_url}
                else:
                    yield {"c_html": abs_url}
            else:
                yield {"ignored": abs_url}

            if self.reo_link.match(abs_url):
                yield scrapy.Request(abs_url, callback=self.parse)
