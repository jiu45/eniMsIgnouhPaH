print("Ha Phuong xinh nhat the gioi, dang tiec em la cua chua te bong dem")
text = ["Ha phuong", "phuong ha", "my ha", "sunny luck", "luck my", "lucas luck", "happy lucas"]
parents = []
descendants = []
ls = []
dict = {}

for a in text:
    tx = a.split()
    d = tx[0]
    p = tx[1]
    if p not in parents:
        parents.append(p)       
    descendants.append(d)

for parent in parents:
    if parent not in descendants:
        dict[parent] = 0
        ls.append(parent)
        break

members = len(descendants) + 1

for i in range(members):
    if len(ls) == members:
        break
    for tex in text:
        tx = tex.split()
        p = tx[1]
        d = tx[0]
        if p in ls:
            dict[d] = dict[p] + 1
            ls.append(d)
print(dict)
