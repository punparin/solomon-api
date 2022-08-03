from PriceFinder import *

class YuyuteiPriceFinder(PriceFinder):
    def __init__(self):
        super().__init__()
        self.yuyutei_endpoint = "https://yuyu-tei.jp/game_ygo/sell/sell_price.php"
        self.source = "Yuyu-tei"
        self.yuyutei_icon = "https://yuyu-tei.jp/img/ogp.jpg"

    def find_prices(self, jp_name):
        url = self.yuyutei_endpoint + "?name=" + urllib.parse.quote(self.format_japanese_name(jp_name))
        card_info = CardInfo(url)

        jp_name = self.format_name_for_search_engine(jp_name)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        divs = soup.find_all("div", {"class": re.compile(r'^group_box.*$')})

        for div in divs:
            raw_rarity = div.find("em", {"class": "gr_color"})
            rarity = self.format_rarity(raw_rarity.text)
            cards = div.find_all("li", {"class": re.compile(r'^card_unit rarity_.*$')})

            for card in cards:
                raw_card_id = card.find("p", {"class": "id"})
                raw_price = card.find("p", {"class": "price"})
                card_id = raw_card_id.text.strip()
                price = self.format_price(raw_price.text)
                
                card = Card(card_id, jp_name, rarity, "Play", price)
                card_info.add_card(card)

                self.logger.info("YuyuteiPriceFinder.find_prices", "name: {0} rarity: {1} condition {2} price: {3}".format(
                        jp_name,
                        rarity,
                        "Play",
                        price
                    ))

        return card_info
