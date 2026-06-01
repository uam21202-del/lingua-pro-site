from PIL import Image
import io, requests

urls = [
    'https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/ba72e5175577103.64f832c127e22.png',
    'https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/f75ccb175577103.64f832c123cf5.png',
    'https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/a9d234175577103.64f832c125ca0.png',
]
for url in urls:
    r=requests.get(url)
    img=Image.open(io.BytesIO(r.content)).convert('RGB')
    img=img.resize((50,50))
    pixels=list(img.getdata())
    color_counts={}
    for p in pixels:
        r2,g2,b2 = p[0]//10*10, p[1]//10*10, p[2]//10*10
        key=(r2,g2,b2)
        color_counts[key]=color_counts.get(key,0)+1
    sorted_c=sorted(color_counts.items(), key=lambda x: x[1], reverse=True)[:8]
    name = url.split('/')[-1]
    print(f'--- {name} ---')
    for c,count in sorted_c:
        print(f'  rgb({c[0]},{c[1]},{c[2]}) - {count}px')
    print()
