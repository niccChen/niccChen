"""Draw the animated Banff-inspired background for the profile banner."""
import math

from PIL import Image, ImageDraw

from build_assets import SCALE, WIDTH, HEIGHT, FONTS, BANNER_SECONDS, RESEARCH_INTERESTS, rect, text, mix


def background(t=0):
    art=Image.new("RGB",(340,155))
    d=ImageDraw.Draw(art)
    phase=math.tau*t/BANNER_SECONDS
    for y in range(155):
        d.line((0,y,339,y),fill=mix((226,242,250),(248,252,253),min(1,y/103)))

    # The whole composition is scenery: open sky, layered peaks, and a glacial lake.
    drift=round(math.sin(phase)*2)
    for x,y,w in [(22,35,36),(108,27,43),(173,39,24),(279,27,25)]:
        d.rectangle((x+drift,y,x+w+drift,y+1),fill="#ffffff")
        d.rectangle((x+8+drift,y-2,x+w-9+drift,y-1),fill="#ffffff")
    d.polygon([(0,94),(0,65),(15,53),(27,60),(38,42),(50,55),(63,36),(79,53),(95,49),(110,67),(126,46),(140,57),(158,38),(174,57),(189,48),(208,61),(224,42),(238,51),(251,34),(270,53),(286,43),(301,61),(320,42),(340,55),(340,108),(0,108)],fill="#d7e4eb")
    d.polygon([(0,105),(0,80),(18,69),(29,64),(41,53),(55,35),(65,44),(74,57),(81,70),(93,65),(104,53),(115,62),(124,78),(137,62),(145,46),(152,42),(163,56),(175,79),(186,64),(201,81),(216,69),(229,48),(244,28),(251,33),(258,45),(265,52),(279,75),(292,51),(301,46),(313,66),(324,37),(333,49),(340,59),(340,111)],fill="#c7d7df")
    for points,c in [
        ([(55,35),(56,53),(65,66),(70,84),(82,103),(50,108),(43,76),(46,58)],"#abc2cf"),
        ([(104,53),(108,71),(115,82),(126,106),(98,106),(98,80)],"#bacdd8"),
        ([(152,42),(156,67),(164,82),(173,106),(139,107),(142,78),(148,62)],"#aec5d2"),
        ([(244,28),(247,49),(256,65),(260,80),(278,107),(226,109),(230,70),(239,52)],"#a8c1d0"),
        ([(301,46),(303,66),(315,86),(321,109),(288,110),(290,78)],"#b4cbd7"),
        ([(324,37),(327,57),(336,71),(340,94),(340,110),(315,110),(319,67)],"#abc5d3")]:d.polygon(points,fill=c)
    for points in [
        [(55,35),(65,44),(69,49),(64,47),(61,53),(57,46),(54,48),(51,44),(46,48)],
        [(104,53),(112,59),(115,64),(109,62),(106,65),(102,59),(98,63)],
        [(152,42),(160,52),(162,57),(156,54),(154,60),(150,53),(146,56),(143,54)],
        [(244,28),(251,33),(258,45),(255,47),(250,43),(248,50),(243,42),(240,46),(235,44),(231,49)],
        [(301,46),(307,54),(310,60),(304,57),(301,61),(297,55),(294,58)],
        [(324,37),(331,47),(333,50),(329,49),(327,55),(324,49),(320,52),(318,48)]
    ]:d.polygon(points,fill="#ffffff")
    d.polygon([(244,42),(244,57),(249,69),(247,73),(242,61),(239,52),(240,46)],fill="#e4eef2")
    d.polygon([(152,53),(152,65),(155,74),(151,71),(148,60)],fill="#e9f2f6")
    for x,y,w in [(48,61,7),(58,73,5),(68,86,9),(96,77,6),(103,85,6),(137,78,8),(143,87,7),(159,89,6),(230,66,8),(226,78,10),(230,86,7),(250,79,6),(257,90,9),(290,73,9),(297,84,5),(319,78,9),(324,91,8)]:
        d.rectangle((x,y,x+w,y+1),fill="#d4e3e9")

    # Nearer valley walls at either side, with a broad lake through the center.
    d.polygon([(0,62),(9,59),(21,47),(31,59),(40,63),(50,76),(59,91),(80,105),(0,117)],fill="#b5cfd1")
    d.polygon([(21,47),(23,66),(33,75),(37,93),(52,106),(0,111),(0,82)],fill="#a3c3c3")
    d.polygon([(318,83),(328,68),(338,61),(340,57),(340,118),(299,105)],fill="#afcbd0")

    water=Image.new("RGB",art.size)
    wd=ImageDraw.Draw(water)
    for y in range(94,155):wd.line((0,y,339,y),fill=mix((174,224,225),(131,211,205),(y-94)/61))
    for points,c in [
        ([(120,96),(125,102),(135,108),(143,123),(149,127),(155,116),(158,108),(165,102),(165,96)],"#a6dadf"),
        ([(219,96),(231,105),(225,111),(235,124),(242,137),(250,142),(256,128),(266,116),(261,109),(271,101),(274,96)],"#a0d5d9"),
        ([(253,97),(260,105),(270,113),(279,122),(284,118),(291,107),(287,99)],"#b5e2e4")]:wd.polygon(points,fill=c)
    for i,(x,y,w) in enumerate([(109,101,19),(154,104,23),(202,102,19),(254,105,15),(92,110,30),(185,114,23),(232,118,27),(115,123,21),(273,124,19),(160,129,32),(209,134,21),(80,139,22),(249,143,29),(148,148,29),(288,150,19)]):
        dx=round(math.sin(phase+i*.71)*3)
        wd.line((x+dx,y,x+w+dx,y),fill=["#e5f7f6","#d4efee","#c2e7e7"][i%3])
        if i%3==0:wd.line((x+dx+7,y+2,x+w+dx-2,y+2),fill="#b3dddf")
    mask=Image.new("L",art.size,0)
    ImageDraw.Draw(mask).polygon([(92,94),(262,94),(275,102),(287,112),(305,123),(340,143),(340,155),(29,155),(47,140),(61,128),(74,117),(81,106)],fill=255)
    art.paste(water,(0,0),mask)
    d=ImageDraw.Draw(art)
    d.line([(85,99),(103,95),(137,94),(167,95),(196,94),(231,95),(259,95),(269,98)],fill="#e2f1f2")
    d.polygon([(0,92),(21,92),(46,94),(71,98),(89,103),(75,113),(68,126),(55,135),(41,146),(30,155),(0,155)],fill="#a5c6bd")
    d.polygon([(0,120),(26,116),(60,111),(76,108),(70,117),(60,124),(55,134),(38,145),(27,155),(0,155)],fill="#94bcb3")
    d.polygon([(276,101),(299,98),(320,91),(340,88),(340,155),(314,144),(294,131),(284,120)],fill="#a0c0b7")
    d.polygon([(303,138),(316,134),(331,140),(340,142),(340,155),(324,153)],fill="#c5d6d5")
    d.polygon([(312,141),(320,138),(331,143),(335,146),(320,146)],fill="#e1e9e6")

    def pine(x,y,h,c,highlight=False):
        d.rectangle((x,y-h,x+1,y),fill=c)
        for level in [.25,.43,.63,.82]:
            py=round(y-h+h*level);span=max(2,round(h*(.07+level*.18)))
            d.polygon([(x,y-h),(x-span,py),(x-1,py),(x-span-1,py+3),(x+span+1,py+3),(x+1,py),(x+span,py)],fill=c)
            if highlight:d.line((x,y-h+3,x-span+1,py),fill="#a8cbc1")
    for x,y,h in [(7,109,31),(18,110,23),(30,105,18),(42,104,17),(55,106,18),(66,104,13),(77,105,10),(283,106,10),(292,106,17),(305,103,22),(317,102,26),(331,104,31)]:pine(x,y,h,"#a6c7bc")
    for x,y,h in [(0,155,65),(14,155,55),(31,149,43),(47,136,32),(325,153,48),(339,155,63)]:pine(x,y,h,"#7fa99f",True)
    return art


def draw_interest(img, t):
    """Scroll one pixel-font interest at a time through a clipped text slot."""
    slot_width, slot_height = 446, 42
    seconds_per_interest = BANNER_SECONDS / len(RESEARCH_INTERESTS)
    index = int(t // seconds_per_interest) % len(RESEARCH_INTERESTS)
    elapsed = t % seconds_per_interest
    # Hold each keyword for 2.3 s, then roll upward for 0.7 s.
    progress = max(0.0, (elapsed - (seconds_per_interest - .7)) / .7)
    shift = round(slot_height * progress * progress * (3 - 2 * progress))
    layer = Image.new("RGBA", (slot_width*SCALE, slot_height*SCALE))
    ld = ImageDraw.Draw(layer)
    text(ld, (0, 7-shift), RESEARCH_INTERESTS[index], FONTS["focus"], "#294c5a")
    if shift:
        text(ld, (0, 7+slot_height-shift), RESEARCH_INTERESTS[(index+1) % len(RESEARCH_INTERESTS)],
             FONTS["focus"], "#294c5a")
    img.paste(layer, (29*SCALE, 174*SCALE), layer)
    d = ImageDraw.Draw(img)
    for i in range(len(RESEARCH_INTERESTS)):
        rect(d, 29+i*9, 231, 3, 3, "#547f84" if i == index else "#c2d9d6")


def make_frame(t):
    img=background(t).resize((WIDTH*SCALE,HEIGHT*SCALE),Image.Resampling.NEAREST)
    # A soft white wash makes the landscape a light background for dark typography.
    overlay=Image.new("RGBA",img.size,(0,0,0,0))
    od=ImageDraw.Draw(overlay)
    for x in range(img.width):
        u=max(0,min(1,(x/img.width-.18)/.57))
        smooth=u*u*(3-2*u)
        alpha=round(255*(.20+.58*(1-smooth)))
        od.line((x,0,x,img.height),fill=(250,253,253,alpha))
    img=Image.alpha_composite(img.convert("RGBA"),overlay).convert("RGB")
    d=ImageDraw.Draw(img)
    rect(d,0,0,WIDTH,40,"#f5fafb")
    rect(d,0,40,WIDTH,1,"#dce9eb")
    for x,c in [(18,"#91b9b5"),(29,"#b3cdcc"),(40,"#d3e3e5")]:rect(d,x,17,5,5,c)
    text(d,(59,14),"niccChen / GitHub",FONTS["small"],"#617d85")
    text(d,(WIDTH-31,13),"↗",FONTS["small"],"#698e91")
    text(d,(29,69),"EMORY UNIVERSITY",FONTS["small"],"#5e7c82",1.5)
    text(d,(32,99),"Yiyun Chen",FONTS["pixel"],"#ffffff")
    text(d,(29,96),"Yiyun Chen",FONTS["pixel"],"#294c5a")
    text(d,(29,155),"RESEARCH INTERESTS",FONTS["small"],"#5e7c82",.6)
    draw_interest(img, t)
    text(d,(29,278),"Research · Engineering",FONTS["small"],"#456873")
    text(d,(591,278),"@niccChen",FONTS["small"],"#3d666d")
    return img
