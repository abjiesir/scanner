from  scapy.all  import  *
print('第一次扫描需要输入本机IP地址')
print('提示：本脚本只是针对前面4000个端口')
ip_local=input('请输入本机IP地址：')
def  scan(ip):
    p=IP(src=str(ip_local),dst=ip)/TCP(dport=(1,4000),flags='S')
    p1=sr(p,timeout=7)
    return  p1
if  __name__=='__main__':
    try:
        while  1:
            a=True
            ip_scan=input('请输入你想扫描的IP地址：')
            res1=scan(ip_scan)
            for  each  in  res1[0].res:
                if(each[1].haslayer(TCP)):
                    if(each[1].getlayer(TCP).fields['flags']=='SA'):
                        a=False
                        print('开放端口：'+str(each[1].getlayer(TCP).fields['sport']))
            if(a):
                print('没有扫描到TCP开放端口')
    except  Exception  as  e:
        print('错误信息：'+str(e))
