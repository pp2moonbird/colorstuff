from PIL import Image, ImageDraw
import colorsys

# im = Image.open('1.png')
# size = 128, 128
# im.thumbnail(size, Image.ANTIALIAS)
# im.save('1_thumb.png', 'PNG')

colors = [
    (83,165,217,0),
    (210,133,132,0),
    (77,196,167,0),
    (250,173,65,0),
    (140,139,192,0)
]

base = 100

row = 5
size = base * len(colors), base * row

print(size)

im = Image.new('RGBA', size)

d = ImageDraw.Draw(im)

for i, color in enumerate(colors):
    print(i, color)
    d.rectangle([i * base, 0, (i + 1) * base, (i + 1) * base], color)



for i, color in enumerate(colors):
    base_color_hls = colorsys.rgb_to_hls(float(color[0]/255), float(color[1]/255), float(color[2]/255))
    print(base_color_hls)

    # increase and decrease saturation for each color
    color_2 = base_color_hls
    color_2 = color_2[0], color_2[1] * 1.25, color_2[2]
    color_2_rgb = colorsys.hls_to_rgb(color_2[0], color_2[1], color_2[2])
    color_2_rgb = int(color_2_rgb[0] * 255), int(color_2_rgb[1] * 255), int(color_2_rgb[2] * 255)
    d.rectangle([i * base, 1 * 100, (i + 1) * base, (i + 2) * base], color_2_rgb)

im.show()
im.save(r'..\result\result.png')