"""Draw the animated Banff-inspired background for the profile banner."""
import math

from PIL import Image, ImageDraw

from build_assets import SCALE, WIDTH, HEIGHT, FONTS, rect, text, mix


def background(t=0):
    art=Image.new("RGB",(340,155))
    d=ImageDraw.Draw(art)
    phase=math.tau*t/8
    for y in range(155):
        d.line((0,y,339,y),fill=mix((50,54,79),(123,153,172),min(1,y/103)))

    # The whole composition is scenery: open sky, layered peaks, and a glacial lake.
    drift=round(math.sin(phase)*2)
    for x,y,w in [(22,35,36),(108,27,43),(173,39,24),(279,27,25)]:
        d.rectangle((x+drift,y,x+w+drift,y+1),fill="#909ab0")
        d.rectangle((x+8+drift,y-2,x+w-9+drift,y-1),fill="#909ab0")
    d.polygon([(0,94),(0,65),(15,53),(27,60),(38,42),(50,55),(63,36),(79,53),(95,49),(110,67),(126,46),(140,57),(158,38),(174,57),(189,48),(208,61),(224,42),(238,51),(251,34),(270,53),(286,43),(301,61),(320,42),(340,55),(340,108),(0,108)],fill="#7d8fa7")
    d.polygon([(0,105),(0,80),(18,69),(29,64),(41,53),(55,35),(65,44),(74,57),(81,70),(93,65),(104,53),(115,62),(124,78),(137,62),(145,46),(152,42),(163,56),(175,79),(186,64),(201,81),(216,69),(229,48),(244,28),(251,33),(258,45),(265,52),(279,75),(292,51),(301,46),(313,66),(324,37),(333,49),(340,59),(340,111)],fill="#a1adba")
    for points,c in [
        ([(55,35),(56,53),(65,66),(70,84),(82,103),(50,108),(43,76),(46,58)],"#647e94"),
        ([(104,53),(108,71),(115,82),(126,106),(98,106),(98,80)],"#788d9f"),
        ([(152,42),(156,67),(164,82),(173,106),(139,107),(142,78),(148,62)],"#6c839b"),
        ([(244,28),(247,49),(256,65),(260,80),(278,107),(226,109),(230,70),(239,52)],"#607c96"),
        ([(301,46),(303,66),(315,86),(321,109),(288,110),(290,78)],"#6b849a"),
        ([(324,37),(327,57),(336,71),(340,94),(340,110),(315,110),(319,67)],"#617d94")]:d.polygon(points,fill=c)
    for points in [
        [(55,35),(65,44),(69,49),(64,47),(61,53),(57,46),(54,48),(51,44),(46,48)],
        [(104,53),(112,59),(115,64),(109,62),(106,65),(102,59),(98,63)],
        [(152,42),(160,52),(162,57),(156,54),(154,60),(150,53),(146,56),(143,54)],
        [(244,28),(251,33),(258,45),(255,47),(250,43),(248,50),(243,42),(240,46),(235,44),(231,49)],
        [(301,46),(307,54),(310,60),(304,57),(301,61),(297,55),(294,58)],
        [(324,37),(331,47),(333,50),(329,49),(327,55),(324,49),(320,52),(318,48)]
    ]:d.polygon(points,fill="#e4e2e5")
    d.polygon([(244,42),(244,57),(249,69),(247,73),(242,61),(239,52),(240,46)],fill="#b9c6d1")
    d.polygon([(152,53),(152,65),(155,74),(151,71),(148,60)],fill="#c3ccd5")
    for x,y,w in [(48,61,7),(58,73,5),(68,86,9),(96,77,6),(103,85,6),(137,78,8),(143,87,7),(159,89,6),(230,66,8),(226,78,10),(230,86,7),(250,79,6),(257,90,9),(290,73,9),(297,84,5),(319,78,9),(324,91,8)]:
        d.rectangle((x,y,x+w,y+1),fill="#99afbf")

    # Nearer valley walls at either side, with a broad lake through the center.
    d.polygon([(0,62),(9,59),(21,47),(31,59),(40,63),(50,76),(59,91),(80,105),(0,117)],fill="#526e81")
    d.polygon([(21,47),(23,66),(33,75),(37,93),(52,106),(0,111),(0,82)],fill="#385969")
    d.polygon([(318,83),(328,68),(338,61),(340,57),(340,118),(299,105)],fill="#42677a")

    water=Image.new("RGB",art.size)
    wd=ImageDraw.Draw(water)
    for y in range(94,155):wd.line((0,y,339,y),fill=mix((63,151,162),(50,172,166),(y-94)/61))
    for points,c in [
        ([(120,96),(125,102),(135,108),(143,123),(149,127),(155,116),(158,108),(165,102),(165,96)],"#459aab"),
        ([(219,96),(231,105),(225,111),(235,124),(242,137),(250,142),(256,128),(266,116),(261,109),(271,101),(274,96)],"#438e9f"),
        ([(253,97),(260,105),(270,113),(279,122),(284,118),(291,107),(287,99)],"#65b4b9")]:wd.polygon(points,fill=c)
    for i,(x,y,w) in enumerate([(109,101,19),(154,104,23),(202,102,19),(254,105,15),(92,110,30),(185,114,23),(232,118,27),(115,123,21),(273,124,19),(160,129,32),(209,134,21),(80,139,22),(249,143,29),(148,148,29),(288,150,19)]):
        dx=round(math.sin(phase+i*.71)*3)
        wd.line((x+dx,y,x+w+dx,y),fill=["#7bcacb","#69b9bb","#5aaeb3"][i%3])
        if i%3==0:wd.line((x+dx+7,y+2,x+w+dx-2,y+2),fill="#54a3ac")
    mask=Image.new("L",art.size,0)
    ImageDraw.Draw(mask).polygon([(92,94),(262,94),(275,102),(287,112),(305,123),(340,143),(340,155),(29,155),(47,140),(61,128),(74,117),(81,106)],fill=255)
    art.paste(water,(0,0),mask)
    d=ImageDraw.Draw(art)
    d.line([(85,99),(103,95),(137,94),(167,95),(196,94),(231,95),(259,95),(269,98)],fill="#99bec5")
    d.polygon([(0,92),(21,92),(46,94),(71,98),(89,103),(75,113),(68,126),(55,135),(41,146),(30,155),(0,155)],fill="#2c565d")
    d.polygon([(0,120),(26,116),(60,111),(76,108),(70,117),(60,124),(55,134),(38,145),(27,155),(0,155)],fill="#244b54")
    d.polygon([(276,101),(299,98),(320,91),(340,88),(340,155),(314,144),(294,131),(284,120)],fill="#2b525c")
    d.polygon([(303,138),(316,134),(331,140),(340,142),(340,155),(324,153)],fill="#73838d")
    d.polygon([(312,141),(320,138),(331,143),(335,146),(320,146)],fill="#a3a9ae")

    def pine(x,y,h,c,highlight=False):
        d.rectangle((x,y-h,x+1,y),fill=c)
        for level in [.25,.43,.63,.82]:
            py=round(y-h+h*level);span=max(2,round(h*(.07+level*.18)))
            d.polygon([(x,y-h),(x-span,py),(x-1,py),(x-span-1,py+3),(x+span+1,py+3),(x+1,py),(x+span,py)],fill=c)
            if highlight:d.line((x,y-h+3,x-span+1,py),fill="#416c70")
    for x,y,h in [(7,109,31),(18,110,23),(30,105,18),(42,104,17),(55,106,18),(66,104,13),(77,105,10),(283,106,10),(292,106,17),(305,103,22),(317,102,26),(331,104,31)]:pine(x,y,h,"#315f66")
    for x,y,h in [(0,155,65),(14,155,55),(31,149,43),(47,136,32),(325,153,48),(339,155,63)]:pine(x,y,h,"#183f4a",True)
    return art


def make_frame(t):
    img=background(t).resize((WIDTH*SCALE,HEIGHT*SCALE),Image.Resampling.NEAREST)
    # A graded navy scrim keeps the established typography clear over the scenery.
    overlay=Image.new("RGBA",img.size,(0,0,0,0))
    od=ImageDraw.Draw(overlay)
    for x in range(img.width):
        u=max(0,min(1,(x/img.width-.18)/.57))
        smooth=u*u*(3-2*u)
        alpha=round(255*(.08+.55*(1-smooth)))
        od.line((x,0,x,img.height),fill=(12,24,39,alpha))
    img=Image.alpha_composite(img.convert("RGBA"),overlay).convert("RGB")
    d=ImageDraw.Draw(img)
    rect(d,0,0,WIDTH,40,"#1d2b3a")
    rect(d,0,40,WIDTH,1,"#43596b")
    for x,c in [(18,"#a6c9d4"),(29,"#759cab"),(40,"#547281")]:rect(d,x,17,5,5,c)
    text(d,(59,14),"niccChen / GitHub",FONTS["small"],"#c5d5df")
    text(d,(WIDTH-31,13),"↗",FONTS["small"],"#a3dfdc")
    text(d,(29,76),"EMORY UNIVERSITY",FONTS["small"],"#b2e3e0",1.5)
    text(d,(32,111),"Yiyun Chen",FONTS["pixel"],"#263e4c")
    text(d,(29,108),"Yiyun Chen",FONTS["pixel"],"#f3f4fa")
    text(d,(29,180),"Machine Learning & Applied AI",FONTS["body"],"#f3f4fa")
    text(d,(29,209),"Computer Science · Applied Mathematics",FONTS["small"],"#d6e2eb")
    text(d,(29,278),"Research · Engineering",FONTS["small"],"#d6e2eb")
    text(d,(591,278),"@niccChen",FONTS["small"],"#e0edf0")
    return img

