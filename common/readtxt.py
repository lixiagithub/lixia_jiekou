def get():
    reslut = []
    f=open("./case/baidu/case.txt","r")
    all=f.readlines()
    for item in all:
        dictone={}
        reslut_all=item.split("|")
        dictone["url"]=reslut_all[0]
        dictone['data']=reslut_all[1]
        dictone['headers']=reslut_all[2]
        dictone['assert']=reslut_all[3]
        dictone['method']=reslut_all[4].split("\n")[0]
        reslut.append(dictone)
    return reslut