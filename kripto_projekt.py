from bitcoinrpc.authproxy import AuthServiceProxy
from datetime import timedelta
import requests, matplotlib.pyplot as plt
import datetime


def main():
    brojac=0
    priceList=[]
    days=[]
    #spajanje na  server
    node_name="blockchain.oss.*****"
    port=*****
    rpc_user=*****
    rpc_password=******
    server =AuthServiceProxy("http://%s:%s@%s:%s"%(rpc_user,rpc_password,node_name,port))
     
    #podaci sa servera
    getinfo = server.getnetworkinfo()
    getblockinfo= server.getblockchaininfo() 
    getmininginfo= server.getmininginfo()
    

    print ("Host: %s , Port: %s"%(node_name,port))
    print ("Broj konekcija na server: ",getinfo["connections"])
    print ("Vrsta blockchaina: ",getblockinfo["chain"])
    print ("Visina bloka: ",getmininginfo["blocks"])
    print ("Zauzece diska: %.2f GB"%((getblockinfo["size_on_disk"]/(1024**3))))


 
  
    #zadaje se interval otkad dokad se dobije graf
    start=str(input("unesite pocetni datum u formatu yyyy-mm-dd: "))
    end=str(input("unesite krajnji datum u formatu yyyy-mm-dd: "))
    dan=str(input("unesite datum za koji zelite vrijednost u formatu yyyy-mm-dd: "))
    poveznica=("https://api.coindesk.com/v1/bpi/historical/close.json?")
    rez=(poveznica + 'start=' + start + '&'+ 'end='+end)
    #dan na koji se dobije vrijednost BTC
    datum=((poveznica + 'start=' + dan + '&'+ 'end='+end))
    specifican_dan=requests.get(datum).json()
    vrijednost=specifican_dan["bpi"][dan] 
    print ("Vrijednost BTC na datum",dan,"je ",vrijednost,"$")
   
    response= requests.get(rez).json()  
    date_time_obj = datetime.datetime.strptime(end, '%Y-%m-%d')
    kraj=date_time_obj.date()
    
    for i in range(1,(len(response["bpi"]))):
        dateInput=(kraj-timedelta(days=i))
        data=response["bpi"][str(dateInput)]
        priceList.append(data)
        days.append(str(dateInput))
        brojac+=1
    
    days.reverse()
    priceList.reverse()

    plt.plot(days,priceList)
    plt.xticks([days[0],days[round(brojac/5)],days[round(brojac/2)],days[round(brojac/1.2)],days[round(brojac-1)]])
    plt.ylabel("Cijena USD")
    plt.title("Cijena BTC kroz specificirani period")
    plt.grid(True)
    plt.show()



 
if __name__=="__main__":
    main()