from PriceFinder import *

class BigWebPriceFinder(PriceFinder):
    def __init__(self):
        super().__init__()
        self.bigweb_endpoint = "https://bigweb.co.jp/ver2/yugioh_index.php"

    def find_prices(self, jp_name):
        url = self.bigweb_endpoint \
            + "?search=yes&type_id=9&action=search&shape=1&seriesselect=&tyselect=&colourselect=&langselect=&condiselect=&selecttext=" \
            +  urllib.parse.quote(self.format_japanese_name(jp_name))
        card_info = CardInfo(url)
        
        jp_name = self.format_name_for_search_engine(jp_name)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        try:
            divs = soup.find_all("div", {"class": "watermat abcd"})
        except AttributeError as err:
            self.logger.error("BigWebPriceFinder.find_prices", err)
            return result

        for div in divs:
            try:
                raw_name = div.find("a", {"href": "javascript:;"})
                scratch = div.find("abbr", {"title": "=キズ"})
                raw_price = div.find("span", {"class": "yendtr"})
                raw_rarity = div.find("abbr", {"title": re.compile(r'.*レア$|.*レル|.*ーマル|^=20SC$|^=PG$|^=Mil-Super$|^=KC-Ultra$')})
                price = self.format_price(raw_price)
                rarity = self.format_rarity(raw_rarity)
                name = re.search("\"《.+》\"", str(raw_name)).group().replace("《", "").replace("》", "").replace("\"", "")

                if jp_name != name:
                    continue

                if scratch is not None:
                    card = Card("-", jp_name, rarity, "Scratch", price)
                    self.logger.info("BigWebPriceFinder.find_prices", "name: {0} rarity: {1} condition {2} price: {3}".format(
                        jp_name,
                        rarity,
                        "Scratch",
                        price
                    ))
                else:
                    card = Card("-", jp_name, rarity, "Play", price)
                    self.logger.info("BigWebPriceFinder.find_prices", "name: {0} rarity: {1} condition {2} price: {3}".format(
                        jp_name,
                        rarity,
                        "Play",
                        price
                    ))
                
                card_info.add_card(card)
            except AttributeError as err:
                self.logger.error("BigWebPriceFinder.find_prices", err)

        return card_info
