import os,base64

template = open("template.html").read()

def epkToBase64(epkname):
    epk = open(f"../packs/{epkname}.epk","rb").read()
    return base64.b64encode(epk).decode("utf-8")

luvre = epkToBase64("007")
117pvp = epkToBase64("1.17PvP")
18 = epkToBase64("1.8")
clown = epkToBase64("ClownPierce32x.epk")
fruitful = epkToBase64("FruitFul32x.epk")
latenci = epkToBase64("Latenci")
lemon = epkToBase64("Lemon")
nqouir = epkToBase64("NqouirFinnalyFixedsmh")
rkyfault = epkToBase64("RKYfault")
someguy1k = epkToBase64("Someguys1kpack")
urusai = epkToBase64("Urusai")
aether = epkToBase64("aether")
arm = epkToBase64("arm")
asda = epkToBase64("asda")
asdashort = epkToBase64("asda_short")
azura = epkToBase64("azura")
bda = epkToBase64("bda")
bear = epkToBase64("bear")
blue = epkToBase64("blue")
blue128x = epkToBase64("blue128x")
bluepack = epkToBase64("bluepack")
bedless = epkToBase64("bn550")
bombies = epkToBase64("bombies")
bombies80 = epkToBase64("bombies80k")
bones = epkToBase64("bones")
bonesnormalsword = epkToBase64("bonesnormalsword")
bonsai = epkToBase64("bonsai")
boxing = epkToBase64("boxing128x")
bubblerose = epkToBase64("bubblerose")
camellia = epkToBase64("camellia")
candy = epkToBase64("candy")
cobalt = epkToBase64("cobalt")
collid = epkToBase64("collide")
defaultfps = epkToBase64("defaultfps")
defaultnew = epkToBase64("defaultnew")
default = epkToBase64("defaultold")
dino = epkToBase64("dino")
drago = epkToBase64("drago")
dynamic = epkToBase64("dynamic")
eternity = epkToBase64("eternity")
faithful = epkToBase64("faithful")
frag = epkToBase64("frag")
gawr = epkToBase64("gawr")
heated = epkToBase64("heated")
kirby = epkToBase64("kirby")
lazy = epkToBase64("lazy")
leo = epkToBase64("leo")
lunar = epkToBase64("lunar")
luv = epkToBase64("luv")
magma = epkToBase64("magma")
mars = epkToBase64("mars")
miamiprivate = epkToBase64("miamiprivate")
mid = epkToBase64("mid")
modifiednew = epkToBase64("modifiednew")
nebula = epkToBase64("nebula")
nicofruit = epkToBase64("nicofruit")
novisfixed = epkToBase64("novisfixed")
orchid = epkToBase64("orchid")
plat = epkToBase64("plat")
prism = epkToBase64("prism")
purpled = epkToBase64("purpled")
rasplin = epkToBase64("rasplin")
rbwtory = epkToBase64("rbwtory")
refaultfixed = epkToBase64("refault fixed")
resent = epkToBase64("resent")
rhedd = epkToBase64("rhedd")
ricefault = epkToBase64("ricefault")
rosamie32x = epkToBase64("rosamie 32x")
rubellite = epkToBase64("rubellite")
sabor = epkToBase64("sabor")
san = epkToBase64("san")
sangRE = epkToBase64("sangRE")
shyguyfixed = epkToBase64("shyguyfixed")
simplybombies = epkToBase64("simplebombies")
skyline = epkToBase64("skyline")
solr2 = epkToBase64("solr2")
soup = epkToBase64("soup")
sunset = epkToBase64("sunset")
sup = epkToBase64("sup")
swiss = epkToBase64("swiss")
tightfault = epkToBase64("tightfault")
toxicaspec = epkToBase64("toxica spec")
tron16 = epkToBase64("tron 16")
twizzydefault = epkToBase64("twizzydefault")
venomv2 = epkToBase64("venomv2")
walifault = epkToBase64("walifault")
wemmbu = epkToBase64("wemmbu")
woody = epkToBase64("woody")
woody2 = epkToBase64("woody2)

def templatePatch(key, value):
    global template
    template = template.replace(key, value)

                     
//templatePatch("filename_epk", variableNameAbove
                
templatePatch("defaultold_epk", default)
templatePatch("007_epk", luvre)
templatePatch("1.17PvP", 117pvp)
                     
                     
templatePatch("classes_js", open("../classes.js").read())
templatePatch("eagswebrtc_js", open("../eagswebrtc.js").read())
templatePatch("classes_server_js", open("../classes_server.js").read())

templatePatch("_css_", open("../style.css").read())

templatePatch("_icon_", base64.b64encode(open("../favicon.png","rb").read()).decode("utf-8"))

templatePatch("_date_", os.popen("date").read())


open("../offline.html", "w").write(template)

print("generated offline.html at " + os.popen("date").read())