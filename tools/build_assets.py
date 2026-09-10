"""Rebuild the profile banner, local badges, and README with Python + Pillow."""
from pathlib import Path
from copy import deepcopy
import math
import xml.etree.ElementTree as ET

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
PREVIEW = ROOT / ".preview"
PREVIEW.mkdir(exist_ok=True)
SCALE = 2
WIDTH, HEIGHT = 680, 310


def font(name, size):
    options = {
        "pixel": [ASSETS / "fonts/PixelifySans.ttf"],
        "sans": [Path("/System/Library/Fonts/Supplemental/Arial.ttf"), Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")],
        "mono": [Path("/System/Library/Fonts/Menlo.ttc"), Path("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf")],
    }
    for path in options[name]:
        if path.exists():
            f = ImageFont.truetype(str(path), round(size * SCALE))
            if name == "pixel":
                f.set_variation_by_axes([500])
            return f
    raise FileNotFoundError(f"Install a font for {name}: {options[name]}")


FONTS = {"pixel": font("pixel", 58), "small": font("mono", 11), "body": font("sans", 13)}
P = dict(edge="#62608b", frame="#8982ad", sky="#282443", night="#302b4e", moon="#ebe1ff", star="#cec1ee", cloud="#5d5686", desk="#b7a5d2", deskedge="#7e7198", cat="#ded6f0", catshade="#b5a6cd", ear="#a18daf", screen="#20223a", code="#a9d9cf", leaf="#9dbdb9", pot="#d8a7ba")


def rect(draw, x, y, w, h, color):
    draw.rectangle((round(x*SCALE), round(y*SCALE), round((x+w)*SCALE)-1, round((y+h)*SCALE)-1), fill=color)


def text(draw, position, value, f, color, tracking=0):
    x, y = position
    if not tracking:
        draw.text((round(x*SCALE), round(y*SCALE)), value, font=f, fill=color, anchor="lt")
        return
    for letter in value:
        draw.text((round(x*SCALE), round(y*SCALE)), letter, font=f, fill=color, anchor="lt")
        x += draw.textlength(letter, font=f)/SCALE + tracking


def mix(a, b, t):
    return tuple(round(x*(1-t)+y*t) for x, y in zip(a, b))


def base_banner():
    img = Image.new("RGB", (WIDTH*SCALE, HEIGHT*SCALE))
    d = ImageDraw.Draw(img)
    top, bottom = (28,28,56), (51,50,85)
    for y in range(HEIGHT*SCALE):
        d.line((0,y,WIDTH*SCALE,y), fill=mix(top,bottom,y/(HEIGHT*SCALE)))
    for y in range(11, HEIGHT, 22):
        for x in range(11, WIDTH, 22):
            rect(d,x,y,1,1,"#45415f")
    rect(d,0,40,WIDTH,1,"#45415d")
    for x,c in [(18,"#b9a3f7"),(29,"#8277b0"),(40,"#605887")]:
        rect(d,x,17,5,5,c)
    text(d,(59,14),"niccChen / GitHub",FONTS["small"],"#c4c2df")
    text(d,(WIDTH-31,13),"↗",FONTS["small"],"#a3dfdc")
    text(d,(29,76),"EMORY UNIVERSITY",FONTS["small"],"#a3dfdc",1.5)
    text(d,(32,111),"Yiyun Chen",FONTS["pixel"],"#20203c")
    text(d,(29,108),"Yiyun Chen",FONTS["pixel"],"#f3f0ff")
    text(d,(29,180),"Machine Learning & Applied AI",FONTS["body"],"#f3f0ff")
    text(d,(29,209),"Computer Science · Applied Mathematics",FONTS["small"],"#c4c2df")
    text(d,(29,278),"Research · Engineering",FONTS["small"],"#c4c2df")
    text(d,(591,278),"@niccChen",FONTS["small"],"#aaa8c6")
    return img


def draw_scene(img, t):
    d=ImageDraw.Draw(img)
    ox, oy = WIDTH-270, HEIGHT-267
    def r(x,y,w,h,c): rect(d,ox+x,oy+y,w,h,P.get(c,c))
    def disk(x,y,radius,color):
        for i in range(-radius,radius+1,3):
            half=int(math.sqrt(radius*radius-i*i)//3)*3
            r(x-half,y+i,max(3,half*2),3,color)
    def star(x,y,opacity):
        c=mix((48,43,78),(206,193,238),opacity)
        r(x,y,3,9,c);r(x-3,y+3,9,3,c)
    phase=t*math.tau/6.7
    r(30,33,189,139,"edge");r(33,30,183,142,"edge");r(36,36,177,129,"frame");r(42,42,165,117,"sky");r(42,111,165,48,"night")
    disk(172,70,18,"moon");disk(181,63,17,"sky")
    for i,(x,y) in enumerate([(60,60),(102,77),(136,52),(190,111),(66,103),(116,118),(151,91)]):
        star(x,y,.45+.35*(.5+.5*math.sin(phase+i*1.7)))
    drift=round(math.sin(phase)*4)*3
    cloud=mix((48,43,78),(93,86,134),.52)
    r(51+drift,133,57,6,cloud);r(60+drift,127,24,6,cloud);r(157-drift,142,39,6,cloud);r(166-drift,136,18,6,cloud)
    r(119,39,5,123,"frame");r(39,101,171,4,"frame");r(30,165,189,6,"edge");r(24,171,201,6,"frame")
    r(30,226,192,5,"#2a2948");r(12,205,231,9,"deskedge");r(9,199,237,6,"desk");r(24,214,6,14,"deskedge");r(228,214,6,14,"deskedge")
    tail=round(math.sin(phase))*3
    r(180,177,15,18,"catshade");r(192,168+tail,6,24-tail,"catshade");r(195,162+tail,9,9,"catshade")
    r(144,162,39,37,"catshade");r(139,170,42,29,"cat");r(140,129,39,33,"cat");r(134,135,51,24,"cat");r(140,159,39,6,"cat")
    r(134,114,6,27,"cat");r(140,120,6,15,"cat");r(146,126,6,9,"cat");r(179,114,6,27,"cat");r(173,120,6,15,"cat");r(167,126,6,9,"cat")
    r(138,123,5,9,"ear");r(176,123,5,9,"ear")
    blink=6.4 < t < 6.6
    r(145,141,4,2 if blink else 6,"screen");r(170,141,4,2 if blink else 6,"screen");r(158,150,4,3,"ear");r(140,151,6,3,"pot");r(174,151,6,3,"pot")
    r(61,157,78,39,"edge");r(58,160,84,33,"edge");r(64,163,72,27,"screen")
    r(70,169,12,3,"code");r(88,169,24,3,"frame");r(76,176,30,3,"frame");r(112,176,12,3,"pot");r(76,183,18,3,"code")
    if math.sin(phase*2)>-.3:r(97,183,3,3,"code")
    r(55,196,90,3,"frame");r(49,199,102,3,"frame")
    r(18,175,18,21,"pot");r(21,172,12,3,"moon");r(36,178,6,12,"pot");r(36,181,3,6,"sky")
    steam=round(math.sin(phase)*2)*2
    r(24+steam,154,3,9,"#aba0c7");r(27+steam,151,3,3,"#aba0c7")
    r(213,181,18,18,"pot");r(210,178,24,4,"moon");r(221,154,3,24,"leaf");r(212,156,9,6,"leaf");r(224,149,9,6,"leaf");r(215,149,6,9,"leaf");r(225,160,6,6,"leaf")
    for i,(x,y,size) in enumerate([(320,64,2),(286,248,1),(644,57,1)]):
        c=mix((45,43,77),(220,205,255),.25+.6*(.5+.5*math.sin(phase+i*2)))
        rect(d,x,y,size,5*size,c);rect(d,x-2*size,y+2*size,5*size,size,c)
    return img


def build_banner():
    from workspace_banner import make_frame

    frames=[make_frame(i/10) for i in range(80)]
    frames[0].save(ASSETS/"banner-work-life-static.png",optimize=True)
    palette=frames[0].quantize(colors=192,method=Image.Quantize.MEDIANCUT)
    indexed=[im.quantize(palette=palette,dither=Image.Dither.NONE) for im in frames]
    indexed[0].save(ASSETS/"banner-work-life.gif",save_all=True,append_images=indexed[1:],duration=100,loop=0,optimize=True,disposal=1)
    samples=[frames[i].resize((680,310),Image.Resampling.LANCZOS) for i in [0,26,53,79]]
    contact=Image.new("RGB",(1360,620),"white")
    for i,im in enumerate(samples):contact.paste(im,((i%2)*680,(i//2)*310))
    contact.save(PREVIEW/"banner-contact-sheet.png")
    print("Banner:", (ASSETS/"banner-work-life.gif").stat().st_size, "bytes;",len(frames),"frames")


SKILLS=[
    ("Languages",[("Python","python"),("C#","csharp")]),
    ("ML & vision",[("PyTorch","pytorch"),("OpenCV","opencv"),("SciPy",None),("scikit-image",None)]),
    ("Data & viz",[("NumPy","numpy"),("pandas","pandas"),("Matplotlib",None),("Jupyter","jupyter")]),
    ("Engineering",[("RAG",None),("MCP",None),(".NET",None),("Avalonia",None)]),
]
NS="http://www.w3.org/2000/svg"
ET.register_namespace("",NS)


def slug(label):return label.lower().replace("#","sharp").replace(".","dot").replace(" ","-")


def build_badges():
    widths={}
    label_font=font("sans",12)
    for _,skills in SKILLS:
        for label,icon in skills:
            width=math.ceil(label_font.getlength(label)/SCALE)+20+(21 if icon else 0)
            widths[label]=width
            for theme,background,line,foreground in [("light","#faf9ff","#e6e7ee","#6b5aaa"),("dark","#222533","#333b4c","#c2b4f0")]:
                svg=ET.Element(f"{{{NS}}}svg",width=str(width),height="30",viewBox=f"0 0 {width} 30",role="img")
                ET.SubElement(svg,f"{{{NS}}}title").text=label
                ET.SubElement(svg,f"{{{NS}}}rect",x=".5",y=".5",width=str(width-1),height="29",rx="6",fill=background,stroke=line)
                if icon:
                    source=ET.parse(ASSETS/f"icons/{icon}.svg").getroot()
                    nested=ET.SubElement(svg,f"{{{NS}}}svg",x="9",y="7.5",width="15",height="15",viewBox=source.get("viewBox","0 0 128 128"))
                    for child in source:nested.append(deepcopy(child))
                labelnode=ET.SubElement(svg,f"{{{NS}}}text",x="30" if icon else "10",y="19",fill=foreground,attrib={"font-family":"Arial, Helvetica, sans-serif","font-size":"12"})
                labelnode.text=label
                ET.ElementTree(svg).write(ASSETS/f"badges/{slug(label)}-{theme}.svg",encoding="utf-8",xml_declaration=False)
    return widths


def build_readme(widths):
    content='''<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="./assets/banner-work-life-static.png">
  <img src="./assets/banner-work-life.gif" alt="Yiyun Chen — Machine Learning & Applied AI — Emory University. A light pixel workspace with a laptop, research notes, coffee, and a plant overlooking Banff-inspired mountains and a turquoise lake." width="100%">
</picture>

<p align="center">
  <a href="https://www.linkedin.com/in/yiyun-chen-1a4a542bb/">LinkedIn ↗</a> &nbsp; · &nbsp;
  <a href="mailto:yiyun.chen@emory.edu">Email ↗</a> &nbsp; · &nbsp;
  <a href="https://github.com/niccChen">GitHub ↗</a>
</p>

## 01 / About

I'm Yiyun (Nicole) Chen, an undergraduate at **Emory University** studying Computer Science and Applied Mathematics & Statistics.

My research interests include **clinical NLP, multimodal reasoning, and probabilistic forecasting**. My applied AI work includes RAG pipelines and document intelligence.

## 02 / Technical skills

<table>
'''
    for category,skills in SKILLS:
        content+=f"  <tr>\n    <td><strong>{category.replace('&','&amp;')}</strong></td>\n    <td>\n"
        for label,_ in skills:
            name=slug(label)
            content+=f'''      <picture><source media="(prefers-color-scheme: dark)" srcset="./assets/badges/{name}-dark.svg"><img src="./assets/badges/{name}-light.svg" alt="{label}" height="30" width="{widths[label]}"></picture>
'''
        content+="    </td>\n  </tr>\n"
    content+='''</table>

---

<p align="center">
  <sub>Research &amp; collaboration · <a href="mailto:yiyun.chen@emory.edu">yiyun.chen@emory.edu</a></sub>
</p>
'''
    (ROOT/"README.md").write_text(content)


if __name__=="__main__":
    build_banner()
    build_readme(build_badges())
