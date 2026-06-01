from PIL import Image
import io, requests

# Check image 2 and 3 for button colors
urls = [
    'https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/ba72e5175577103.64f832c127e22.png',
    'https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/e7fa0a175577103.64f832c124c89.png',
]
for idx, url in enumerate(urls):
    r=requests.get(url)
    img=Image.open(io.BytesIO(r.content)).convert('RGB')
    img=img.resize((150,150))
    pixels=list(img.getdata())
    # Find saturated / bold colors
    bold = {}
    for p in pixels:
        r2,g2,b2 = int(p[0]), int(p[1]), int(p[2])
        max_c = max(r2,g2,b2)
        min_c = min(r2,g2,b2)
        sat = max_c - min_c
        if sat > 30:
            key = (r2//20*20, g2//20*20, b2//20*20)
            if key not in bold:
                bold[key] = 0
            bold[key] += 1
    print(f'=== Image {idx+1} Bold Colors ===')
    for c,count in sorted(bold.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f'  rgb({c[0]},{c[1]},{c[2]}) - {count}px')
    print()
