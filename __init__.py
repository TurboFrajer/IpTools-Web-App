from flask import Flask, render_template, request, redirect
from netaddr import *
from datetime import datetime
import requests, json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/ipblacklist", methods=["GET",'POST'])
def ipblacklist():
    if request.method == "POST":
        blackinput = request.form['text']
        url4 = requests.get("<IPv4 list webpage")
        url6 = requests.get("<IPv6 list webpage>")
        url4.encoding = "utf-8"
        url6.encoding = "utf-8"
        text = url4.text + url6.text
        info = text.splitlines()
        found = [z.split()[0] for z in info]
        text1 = []
        text1.clear()
        for x in range(len(found)):
            
            try:
                IPNetwork(blackinput) == True

            except:
                print("Není IP adresa nebo rozsah.")
                text1.append("Není IP adresa nebo rozsah.")
                break

            if IPNetwork(blackinput) in IPNetwork(found[x]):        
                for y in range(len(info)):
                    if found[x] in info[y]:
                        tim = info[y].split()
                        print(f"Adresa {tim[0]} je blacklisted.")
                        text1.append(f"Adresa {tim[0]} je blacklisted.")
                        if tim[1] == "0":
                            print("Perma blacklisted.")
                            text1.append("Perma blacklisted.")
                            duvoda = " ".join(tim[2:])
                            print(f"Důvod: {duvoda}")
                            text1.append(f"Důvod: {duvoda}")
                            
                        elif tim[1].isnumeric() == True and tim[2].isnumeric() == True:
                            print(f"Blacklisted od: {datetime.fromtimestamp(int(tim[2]))}")
                            text1.append(f"Blacklisted od: {datetime.fromtimestamp(int(tim[2]))}")
                            bando = int(tim[1])+int(tim[2])
                            print(f"Blacklisted do: {datetime.fromtimestamp(bando)}")
                            text1.append(f"Blacklisted do: {datetime.fromtimestamp(bando)}")
                            duvodb = " ".join(tim[3:])
                            print(f"Důvod: {duvodb}")
                            text1.append(f"Důvod: {duvodb}")
                            
                        else:
                            print(info[y])
                            break
                break        
        else:
            print("Není blacklisted.")
            text1.append("Není blacklisted.")

        return render_template('ipblacklist.html', text1=text1)

    else:
        return render_template('ipblacklist.html')


@app.route("/internblacklist", methods=["GET",'POST']) 
def internblacklist():
    if request.method == "POST":
        interninput = request.form['text']
        list1 = []
        list2 = []
        list3 = []
        list4 = []    
        list5 = []
        list6 = []
        list7 = []
        list8 = []
        list9 = []
        list10 = []
        list11 = []
        list12 = []
        list13 = []
        list14 = []
        list15 = []
        list16 = []
        list17 = []
        listNOT = []
        ipicka = []               
        try: 
            headers = {"Content-Type": "application/x-www-form-urlencoded"}

            r = requests.post("<internal blacklist>", data=f"data={{\"action\": \"search\",\"ip\":\"{interninput.strip()}\"}}",headers=headers )

            parsed = json.loads(r.text)
            devices = parsed["devices"]
            listing = list(devices) 
            print(json.dumps(parsed, indent=4))
            #status
            ipicka.clear()
            ipicka.append("Testovaná doména:")
            ipicka.append(interninput.strip())
            #1
            list1.clear()
            list1.append("ID:" + listing[0]["identificator"])
            list1.append("Hostname:" + listing[0]["hostname"])
            list1.append("Status:" + listing[0]["status"])
            #2
            list2.clear()
            list2.append("ID:" + listing[1]["identificator"])
            list2.append("Hostname:" + listing[1]["hostname"])
            list2.append("Status:" + listing[1]["status"])
            #3
            list3.clear()
            list3.append("ID:" + listing[2]["identificator"])
            list3.append("Hostname:" + listing[2]["hostname"])
            list3.append("Status:" + listing[2]["status"])
            #4
            list4.clear()
            list4.append("ID:" + listing[3]["identificator"])
            list4.append("Hostname:" + listing[3]["hostname"])
            list4.append("Status:" + listing[3]["status"])
            #5
            list5.clear()
            list5.append("ID:" + listing[4]["identificator"])
            list5.append("Status:" + listing[4]["status"])                
            #6
            list6.clear()
            list6.append("ID:" + listing[5]["identificator"])
            list6.append("Status:" + listing[5]["status"])
            #7
            list7.clear()
            list7.append("ID:" + listing[6]["identificator"])
            list7.append("Status:" + listing[6]["status"])
            #8
            list8.clear()
            list8.append("ID:" + listing[7]["identificator"])
            list8.append("Status:" + listing[7]["status"])    
            #9
            list9.clear()
            list9.append("ID:" + listing[8]["identificator"])
            list9.append("Status:" + listing[8]["status"])    
            #10
            list10.clear()
            list10.append("ID:" + listing[9]["identificator"])
            list10.append("Status:" + listing[9]["status"])
            #11
            list11.clear()
            list11.append("ID:" + listing[10]["identificator"])
            list11.append("Status:" + listing[10]["status"])    
            #12
            list12.clear()
            list12.append("ID:" + listing[11]["identificator"])
            list12.append("Status:" + listing[11]["status"])
            #13
            list13.clear()
            list13.append("ID:" + listing[12]["identificator"])
            list13.append("Status:" + listing[12]["status"])
            #14
            list14.clear()
            list14.append("ID:" + listing[13]["identificator"])
            list14.append("Status:" + listing[13]["status"])    
            #15
            list15.clear()
            list15.append("ID:" + listing[14]["identificator"])
            list15.append("Status:" + listing[14]["status"])
            #16
            list16.clear()
            list16.append("ID:" + listing[15]["identificator"])
            list16.append("Status:" + listing[15]["status"])
            #17
            list17.clear()
            list17.append("ID:" + listing[16]["identificator"])
            list17.append("Status:" + listing[16]["status"])

        except:
            ipicka.clear()
            ipicka.append("Testovaná doména")
            ipicka.append(interninput.strip())
            listNOT.clear()
            listNOT.append("Není IP adresa nebo rozsah")
        
        return render_template('internblacklist.html', ipicka=ipicka, listNOT=listNOT, list1=list1, list2=list2, list3=list3, list4=list4, list5=list5, list6=list6, list7=list7, list8=list8, list9=list9, list10=list10, list11=list11, list12=list12, list13=list13, list14=list14, list15=list15, list16=list16, list17=list17)

    else:
        return render_template('internblacklist.html')





