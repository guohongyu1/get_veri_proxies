import requests,pandas
urls=('https://www.kuaidaili.com/free/inha/%s/'%i for i in range(1,2714))
for url in urls:
    t=pandas.read_html(url)[0].T
    for i in range(0,t.shape[1]):
        s={"%s"%t.values[3][i].lower():"%s:%s"%(t.values[0][i],t.values[1][i])}
        try:
            res=requests.get('http://www.baidu.com',proxies=s,timeout=5)
            if res.status_code==200:
                with open('vps.txt', 'a') as e: e.write("%s" % s)
        except Exception as e:pass