import requests

# E-posta listesini içeren dosyanın adı
file_name = "extracted_emails.txt"

# POST isteği yapılacak URL
post_url = "https://mail.com.tr/message/send/format/html"  # İlgili URL'yi güncelleyin

# Diğer verileri ve başlıkları (headers) burada belirtin
headers = {
    'Cookie': 't=f_l.tr; ms=57692c855395e5820811debb8e081e1b; _ga_9K9MFVHHN9=GS1.1.1698154037.3.1.1698154916.0.0.0; _ga=GA1.1.1416591069.1698140118; vid=1634121417-0-6154711257691699243; __gads=ID=9fc22252a9060ee9-229e023503e300f3:T=1698140116:RT=1698154032:S=ALNI_MbMJIjVBByqDJDTM1SIofoIDutOpg; __gpi=UID=00000ca199049a78:T=1698140116:RT=1698154032:S=ALNI_MZUjbNXqwatDIaNar_XoExDMH5tPw; __utma=33577149.1416591069.1698140118.1698146315.1698146315.5; __utmc=33577149; __utmz=33577149.1698140123.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); cto_bundle=P4fxoF9uUU9xWGFkVXB0NFNEMlNLN0kyS1hmWHliREY3WmgxNm9VZE1sck92VkRWVk15c0RzNGNHbnE0VmxPUTFOTzkxd2diNmNwbmt5YkxEamxWN0hpNlg4ZGF3RGtaS1o2czIlMkZ5bEpIMXkwSEx0ZGkwbkxOdnU0aU42cGhabnRRR3pNaFVUMXZNaE9KRkpkNEE2WkFWSmliZyUzRCUzRA; current_page=mailbox/inbox; __utmb=33577149.3.10.1698147784',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
    'Accept': 'application/json, text/javascript, */*',
    'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://mail.com.tr',
    'Referer': 'https://mail.com.tr/idx'
}

# E-posta listesini dosyadan okuyun ve her e-postayı gönderin
with open(file_name, "r") as file:
    email_list = [line.strip() for line in file]
    

for email in email_list:
    
    data = {
        "token": "6537c638eb7b0_b5a82ba96428f375527c5fb40f636c7e6537c638eb7ee",
        "readresponse": 0,
        "saveattachments": 1,
        "saveinsent": 1,
        "linkattachments": 0,
        "to": f"{email}",  
        "subject": "#FREEPALESTINE 🇵🇸",
        "message": "<img src='https://img.tv100.com/rcman/Cw850h478q95gc/storage/files/images/2023/10/22/kapak-fn56_cover.jpg' width='275' height='250'><img src='https://www.gercektaraf.com/images/haberler/2023/10/israil-gazze-de-1030-cocugu-oldurdu-9707.jpg' width='275' height='250'><img src='https://trthaberstatic.cdn.wp.trt.com.tr/resimler/2128000/saldiri-gazze-aa-2128967_2.jpg' width='275' height='250'><img src='https://trthaberstatic.cdn.wp.trt.com.tr/resimler/2120000/rimal-a-2121838.jpg' width='275' height='250'><style>img {float:left;}</style><br><p>Palestine is under the occupation of the Israeli state. Innocent civilians, including children and babies, are being ruthlessly killed in Palestine. What crimes have these children, babies, and civilians committed to justify such merciless killings by the Israeli government? How can babies and children be considered terrorists and be brutally killed? Stand against the ruthless attacks in Palestine, for it is only babies, children, and civilians who are losing their lives. 'If you can feel pain, you are alive. If you can feel the pain of others, you are human. - Lev Tolstoy.' No case in which innocent babies, children, and civilians are being killed can be considered a just one. Oppose this ruthless genocide, so that the innocent, babies, and children do not perish. Imagine what the children in Palestine are going through, or think about sitting at home with your family while constantly facing aerial, land, and sea bombardments with all sorts of chemical bombs.The people in Gaza are being denied access to essential resources such as electricity, water, food, medical supplies/equipment, and fuel. What will patients dependent on medical devices, premature babies in incubators, and those who have no access to anything do to survive? This is a blatant act of genocide and a violation of human rights. Regardless of your religion, whether you are Muslim, Christian, Jewish, Buddhist, Atheist, or of any other faith, it doesn't matter. Show your outrage against this massacre because you are a human being.Just think about it.The State of Israel is ruthlessly bombing hospitals, schools, marketplaces, civilian settlements, places of worship (mosques, churches) and places where civilians and children take shelter in Gaza.<br><hr>Note: This e-mail has been sent automatically for informational purposes.Posted by: Erkan Demir 🇹🇷</p>"
    }

    response = requests.post(post_url, data=data, headers=headers)

    if response.status_code == 200:
     if "params" in response.text:
        print(f"Email başarıyla gönderildi: {email}")
     else:
        print(f"Gönderimde bir hata oluştu: {email}")
    else:
     print(f"Hata oluştu: {email}, Durum kodu: {response.status_code}")
     print(response.text)  # Hata ayıklama için yanıt metnini görüntüleyin
