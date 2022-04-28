# solomon-api

is an API retrieving Yugioh OCG cards' price by scraping data from [bigweb](https://bigweb.co.jp/) and [YUYU-TEI](https://yuyu-tei.jp/).

## Usage

| Params | Description              | Example              |
| ------ | ------------------------ | -------------------- |
| name   | Card's name in japanese  | ユニオン・キャリアー |
| source | Either bigweb or yuyutei | bigweb               |

`curl http://localhost/api/cards?name=ユニオン・キャリアー&source=yuyutei`

```json
{
  "cards": [
    {
      "condition": "Play",
      "id": "LVP3-JP011",
      "jp_name": "ユニオン・キャリアー",
      "price": "2980",
      "rarity": "SCR"
    },
    {
      "condition": "Play",
      "id": "LVP3-JP011",
      "jp_name": "ユニオン・キャリアー",
      "price": "980",
      "rarity": "UR"
    }
  ],
  "url": "https://yuyu-tei.jp/game_ygo/sell/sell_price.php?name=%E3%83%A6%E3%83%8B%E3%82%AA%E3%83%B3%E3%83%BB%E3%82%AD%E3%83%A3%E3%83%AA%E3%82%A2%E3%83%BC"
}
```

## For development

### Setup development environment

```sh
virtualenv venv
# For fish
source venv/bin/activate.fish
# For shell
source venv/bin/activate
pip install -r requirements.txt
```

### Environment variables

```env
# .env
DISCORD_TOKEN=<TOKEN>
```

### Running on local

```sh
# Run on machine
python src/main.py

# Run on docker
earthly +compose-up
earthly +compose-down
```
