print("Ha Phuong xinh nhat the gioi, dang tiec em la cua chua te bong dem")

text = ["Ha phuong", "phuong ha", "my ha", "sunny luck", "luck my", "lucas luck", "happy lucas"]
parents = []
descendants = []
dict = {}

for a in text:
    tx = a.split()
    d = tx[0]
    p = tx[1]
    if p not in parents:
        parents.append(p)       
    descendants.append(d)


end_cond = len(parents)    #Cái này để end vòng lặp ở dưới

for i in range(len(parents)):
    ancestor = False       #mình chỉ cần xác định ancestor ở lần đầu thôi
    if i == 0:
        ancestor = True    #lần đầu nè :)
    for parent in parents:      #Nhảy vào từng phần tử của parents
        if parent not in descendants:      #Tại sao phải not in cả descendants và generations nhỉ, thử nghĩ xem :)           
            if ancestor:
                dict[parent] = 0              #Nếu là ancestor thì cho nó bằng 0
                ancestor = False              #Đổi lại biến bool để lần lặp sau không nhảy vào đây nữa
            parents.remove(parent)        
            for a in text:                    
                tx = a.split()
                d = tx[0]
                p = tx[1]
                if p == parent:
                    dict[d] = dict[parent] + 1
                    descendants.remove(d)         #remove descendant(s) này ra, để nếu chúng là parent thì if not tiếp tục chạy (đầu tiên chỉ có ancestor ở trong parents và không ở trong descendants)
            
for name in sorted(dict):
    print(name, dict[name])