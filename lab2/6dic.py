d={
    "uwu":"fu",
    "skuf":"ggg",
    "adol":148,
    "skuf":"uwu"
}
print(d["adol"])
print(d)
print(len(d))
d={
    "uwu":"fu",
    "skuf":"ggg",
    "adol":148,
    "skuf":{3, 4,6,2,3}
}
print(d)
f=dict(x=5,y=3,i=9)
print(f["i"])
k=f.keys()
print(k)
f["p"]=45
print(k)
v=f.values()
print(v)
i=f.items()
print(i)

#remove
f.pop("i")
print(f)
f.popitem()
print(f)

#nested
g={
    "hg":{
        "po":45,
        "l":"light"
    },
    "kg":{
        "puo":66,
        "666":"sat"
    }
}
print(g)
l={
    "tet":"kira",
    "l":"vl"
}
kg={
        "puo":66,
        "666":"sat"
    }
mi={
    "l":l,
    "kg":kg
}
print(mi)
print(mi["l"]["tet"])
for e,r in mi.items():
    print(e)
    for b in r:
        print(b+':',r[b])