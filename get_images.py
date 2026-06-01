import requests, re

urls = [
    'https://unsplash.com/photos/XaBNnChxDCg',
    'https://unsplash.com/photos/IALMcAl3qYs',
    'https://images.unsplash.com/photo-1616486338812-3dadae4b4ace',
]

for url in urls:
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        m = re.search(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"', r.text)
        if m:
            direct_url = m.group(1)
            print(f'{url} -> {direct_url}')
        else:
            print(f'No og:image found for {url}')
    except Exception as e:
        print(f'Error for {url}: {e}')
