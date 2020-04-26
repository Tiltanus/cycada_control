import requests
domen = ['3.136.160.251', '3.23.94.138']
port_id = ':5000'
while True:
    for ip in domen:
        response = requests.get("http://"+ip+port_id+"/status")
        if not response.json()['end']:
            with open('./control.txt', 'a') as file:
                file.write(ip+' '+str(response.json()['end'])+"\n")
            domen.remove(ip)