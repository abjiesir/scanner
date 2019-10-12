from  scapy.all  import  *


p=IP(dst='202.203.158.158')/ICMP()
p.show()
p1=sr(p,timeout=4)
print(p1)


'''
import  IPy
import  multiprocessing  as  mul
arr=[]
arr1=[]
arr2=[]
arr3=[]
def   scan(ip,ip_local):
    p=IP(src=str(ip_local),dst=str(ip))/ICMP(type=8)
    p1=sr(p,timeout=0.5)
    return   p1
if  __name__=='__main__':
    print('第一次需要输入本机IP地址')
    ip_local=input('请输入本机IP地址：')
    while  1:
        ip_scan=input('请输入你想要扫描的IP地址：')
        net=input('请输入你的网关：')
        process=input('请输入扫描的进程数目：')
        ip1=IPy.IP(str(ip_scan)).make_net(str(net))
        print('正在扫描》》》》》')
        try:
            pool=mul.Pool(processes=int(process))
            for  each  in  ip1:
                res=pool.apply_async(scan,(each,ip_local))
                arr.append(res)
            pool.close()
            pool.join()
            for   each  in  arr:
                packet=each.get()
                if(packet[0].res):
                    arr1.append(packet[0].res[0][1].getlayer(IP).fields['src'])
                    arr2.append(packet[0].res[0][1].getlayer(IP).fields['src'])
            look=input('查看历史结果请输入 1，仅查看本次结果输入 2：')
            if(look=='2'):
                for  each  in  arr1:
                    print(each)
            elif(look=='1'):
                for  each  in  arr2:
                    a=True
                    b=0
                    for  each1  in  arr2:
                        if(each==each1):
                            b=b+1
                    if(b>1):
                        a=False
                    if(a):
                        arr3.append(each)
                for  each  in  arr3:
                    print(each)
                                 
            else:
                print('请输入正确指令')
            arr=[]
            arr1=[]
        except  Exception  as e :
            print(e)
            '''
