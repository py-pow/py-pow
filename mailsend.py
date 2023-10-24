import requests

# E-posta listesini içeren dosyanın adı
file_name = "extracted_emails.txt"

# POST isteği yapılacak URL
post_url = "https://mail.com.tr/message/send/format/html"  # İlgili URL'yi güncelleyin

# Diğer verileri ve başlıkları (headers) burada belirtin
headers = {
    'Cookie': 't=f_l.tr; ms=757218ab4ee020075fde16208ccbe358; _ga_9K9MFVHHN9=GS1.1.1698146268.2.1.1698146316.0.0.0; _ga=GA1.1.1416591069.1698140118; vid=1634121417-0-6154711257691689631; __gads=ID=9fc22252a9060ee9-229e023503e300f3:T=1698140116:RT=1698146310:S=ALNI_MbMJIjVBByqDJDTM1SIofoIDutOpg; __gpi=UID=00000ca199049a78:T=1698140116:RT=1698146310:S=ALNI_MZUjbNXqwatDIaNar_XoExDMH5tPw; __utma=33577149.1416591069.1698140118.1698146271.1698146315.3; __utmc=33577149; __utmz=33577149.1698140123.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); cto_bundle=h-oNEV9uUU9xWGFkVXB0NFNEMlNLN0kyS1hlVUlsVjNPbEU2V1hXaFo1aWpWY2FHc1V1b0duZDl1d0VRdFVnQUxROEo1YzdtaW41cDNnMms2Q2FwSnJ6eWtQRlJyS3lrNzgzNmxvcWlYc2xvWk4lMkJyWUttQ1NKSnVha1VFc1ElMkJPU3NNVzV5elhWOTI5dFJLZFVSMmkyU2J5JTJCdmclM0QlM0Q; current_page=mailbox/sent; __utmb=33577149.1.10.1698146271; __utmt=1; __utmd=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
    'Accept': 'application/json, text/javascript, */*',
    'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'XMLHttpRequest'
}

# E-posta listesini dosyadan okuyun ve her e-postayı gönderin
with open(file_name, "r") as file:
    email_list = [line.strip() for line in file]

for email in email_list:
    data = {
        "token": "6537904aa0ef6_451df879d38f290abe8572c713e817476537904aa0f35",
        "readresponse": 0,
        "saveattachments": 1,
        "saveinsent": 1,
        "linkattachments": 0,
        "to": email,  # Her e-postayı sırayla gönderin
        "subject": "#FREEPALESTINE 🇵🇸🇹🇷",
        "message": "<img src='https://img.tv100.com/rcman/Cw850h478q95gc/storage/files/images/2023/10/22/kapak-fn56_cover.jpg' width='275' height='250'><img src='https://www.gercektaraf.com/images/haberler/2023/10/israil-gazze-de-1030-cocugu-oldurdu-9707.jpg' width='275' height='250'><img src='https://trthaberstatic.cdn.wp.trt.com.tr/resimler/2128000/saldiri-gazze-aa-2128967_2.jpg' width='275' height='250'><img src='https://trthaberstatic.cdn.wp.trt.com.tr/resimler/2120000/rimal-a-2121838.jpg' width='275' height='250'><style>img {float:left;}</style><br><p>Palestine is under the occupation of the Israeli state. Innocent civilians, including children and babies, are being ruthlessly killed in Palestine. What crimes have these children, babies, and civilians committed to justify such merciless killings by the Israeli government? How can babies and children be considered terrorists and be brutally killed? Stand against the ruthless attacks in Palestine, for it is only babies, children, and civilians who are losing their lives. 'If you can feel pain, you are alive. If you can feel the pain of others, you are human. - Lev Tolstoy.' No case in which innocent babies, children, and civilians are being killed can be considered a just one. Oppose this ruthless genocide, so that the innocent, babies, and children do not perish. Imagine what the children in Palestine are going through, or think about sitting at home with your family while constantly facing aerial, land, and sea bombardments with all sorts of chemical bombs.The people in Gaza are being denied access to essential resources such as electricity, water, food, medical supplies/equipment, and fuel. What will patients dependent on medical devices, premature babies in incubators, and those who have no access to anything do to survive? This is a blatant act of genocide and a violation of human rights. Regardless of your religion, whether you are Muslim, Christian, Jewish, Buddhist, Atheist, or of any other faith, it doesn't matter. Show your outrage against this massacre because you are a human being.Just think about it.The State of Israel is ruthlessly bombing hospitals, schools, marketplaces, civilian settlements, places of worship (mosques, churches) and places where civilians and children take shelter in Gaza. <br> <hr>Note: This e-mail has been sent automatically for informational purposes. Posted by: Erkan Demir 🇹🇷</p>"
    }

    response = requests.post(post_url, data=data, headers=headers)

if response.status_code == 200:
    if "<params>%7B%22prevuid%22%3A-1%2C%22nextuid%22%3A-1%2C%22nextunseen%22%3A-1%2C%22flagname%22%3A%22%22%7D</params>" in response.text:
        print(f"Email başarıyla gönderildi: {email}")
    else:
        print(f"Gönderimde bir hata oluştu: {email}")
else:
    print(f"Hata oluştu: {email}, Durum kodu: {response.status_code}")
    print(response.text)  # Hata ayıklama için yanıt metnini görüntüleyin
