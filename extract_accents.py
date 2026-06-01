from PIL import Image
import io, requests

url = 'https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/b2c6ea175577103.64f832c126d94.png'
r=requests.get(url)
img=Image.open(io.BytesIO(r.content)).convert('RGB')
img=img.resize((200,200))
pixels=list(img.getdata())

# Look for non-gray colors (saturation check)
accents = {}
for p in pixels:
    r2,g2,b2 = int(p[0]), int(p[1]), int(p[2])
    # check if it's not a shade of gray
    max_c = max(r2,g2,b2)
    min_c = min(r2,g2,b2)
    sat = max_c - min_c
    if sat > 20 and max_c < 240:
        key = (r2//20*20, g2//20*20, b2//20*20)
        if key not in accents:
            accents[key] = 0
        accents[key] += 1

print("=== ACCENT COLORS (non-gray) ===")
for c,count in sorted(accents.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f'  rgb({c[0]},{c[1]},{c[2]}) - {count}px')

# Also look at a few specific bottom areas for nav/buttons
# Sample the bottom 50 rows
w,h = img.size
bottom = []
for y in range(h-50, h):
    for x in range(w):
        bottom.append(pixels[y*w + x])
        
print("\n=== BOTTOM SECTION COLORS ===")
color_counts={}
for p in bottom:
    r2,g2,b2 = p[0]//10*10, p[1]//10*10, p[2]//10*10
    key=(r2,g2,b2)
    color_counts[key]=color_counts.get(key,0)+1
for c,count in sorted(color_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f'  rgb({c[0]},{c[1]},{c[2]}) - {count}px')
