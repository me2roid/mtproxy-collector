
# MTProto Proxy Collector

A simple Python script to collect free **MTProto Telegram proxy links** from multiple public sources.

## 🔍 Features

- Collects proxies from:
  - [MTPro.xyz](https://mtpro.xyz/)
  - [Free Proxy DB GitHub](https://github.com/LoneKingCode/free-proxy-db)
- Outputs proxy links in this format (compatible with Telegram one-click connect):
  ```
  https://t.me/proxy?server=IP&port=PORT&secret=SECRET
  ```

## 🚀 How to Use

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/mtproto-collector.git
cd mtproto-collector
```

### 2. Install dependencies
```bash
pip install requests
```

### 3. Run the script
```bash
python fetch_mtproto.py
```

### 4. Output
- A file named `mtproto_proxies.txt` will be created with 100+ fresh proxy links.

---

## 🔁 Optional: Auto-refresh Every 5 Minutes

To keep fetching new proxies every 5 minutes, wrap the script like this:

```python
import time

while True:
    links = fetch_links()
    save_links(links)
    time.sleep(300)  # wait 5 minutes
```

---

## 📂 .gitignore (Recommended)
Add this to `.gitignore` file to avoid uploading cache/output files:
```
__pycache__/
mtproto_proxies.txt
```

---

## 📜 License

MIT License – Free to use, modify, and share.

> Feel free to contribute or share your own proxy sources. Enjoy!

---

## 🏴 Signature


```
                                      ┏┓    • ┓
                                 ┏┳┓┏┓┏┛┏┓┏┓┓┏┫
                                 ┛┗┗┗ ┗━┛ ┗┛┗┗┻

                        created & powered by >>>  ME2ROID  <<<
```
