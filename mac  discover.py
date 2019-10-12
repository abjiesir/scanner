from  scapy.all import   *
import  IPy
import  multiprocessing   as   mul
arr=[]
def  scan(ip,ip_local,a,count):
    packet=Ether(src='24:fd:52:b9:c1:c5',dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=str(ip),psrc=str(ip_local))
    res=srp(packet,timeout=2)
    a=int((a/count)*100)
    print('扫描进度-->'+str(a)+'%')
    return  res
if  __name__=='__main__':
    ip_local=input('请输入本机IP地址：')
    while  1:
        arr1=0
        a=0
        ip1=input('请输入局域网扫描IP：')
        net=input('请输入网关地址：')
        ip_all=IPy.IP(ip1).make_net(net)
        for  each  in  ip_all:
            arr1=arr1+1
        print('共有IP'+str(arr1)+'个')
        pool=mul.Pool(processes=5)
        print('正在初始化扫描进程....')
        for  ip  in   ip_all:
            a=a+1
            res=pool.apply_async(scan,(ip,ip_local,a,arr1))
            arr.append(res) 
        pool.close()
        pool.join()
        for   each  in   arr:
            each=each.get()
            if(each[0].res):
                if(each[0].res[0][1].haslayer(ARP)):
                    print(str(each[0].res[0][1].getlayer(ARP).fields['hwsrc'])+'---->'+str(each[0].res[0][1].getlayer(ARP).fields['psrc']))

