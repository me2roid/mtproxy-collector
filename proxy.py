import requests

SOURCES = [
    ("MTPro.XYZ", "https://mtpro.xyz/api/?type=mtproto"),
    ("FreeProxyDB", "https://raw.githubusercontent.com/LoneKingCode/free-proxy-db/main/mtproto.txt")
]

def fetch_links():
    links = []
    for name, url in SOURCES:
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            if url.endswith(".txt"):
                for line in r.text.splitlines():
                    host, port, secret = line.strip().split(":")
                    links.append(f"https://t.me/proxy?server={host}&port={port}&secret={secret}")
            else:
                data = r.json()
                for item in data:
                    links.append(f"https://t.me/proxy?server={item['host']}&port={item['port']}&secret={item['secret']}")
            print(f"[✅] از {name} recieve : {len(links)} link")
        except Exception as e:
            print(f"[⚠️] error in  {name}: {e}")
    return list(dict.fromkeys(links))

def save_links(links):
    with open("mtproto_proxies.txt", "w") as f:
        for link in links:
            f.write(link + "\n")
    print(f"[✅] save : {len(links)}  link in mtproto_proxies.txt")

def main():
    links = fetch_links()
    save_links(links)

if __name__ == "__main__":
    main()