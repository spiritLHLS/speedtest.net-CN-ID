import csv
import json
import urllib.request

# IP地址归属地查询API的URL
url_template = 'http://ip-api.com/json/{ip}?fields=status,message,isp'

# 三个运营商的关键词
unicom_keywords = ['China Unicom']
mobile_keywords = ['China Mobile']
telecom_keywords = ['China Telecom', 'China Tietong']

# 打开CSV文件
with open('CN.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    # 跳过第一行，因为是标题
    next(reader)
    # 创建三个CSV文件，用于存储三个运营商的行
    unicom_file = open('CN_Unicom.csv', 'w', encoding='utf-8', newline='')
    mobile_file = open('CN_Mobile.csv', 'w', encoding='utf-8', newline='')
    telecom_file = open('CN_Telecom.csv', 'w', encoding='utf-8', newline='')
    unicom_writer = csv.writer(unicom_file)
    mobile_writer = csv.writer(mobile_file)
    telecom_writer = csv.writer(telecom_file)
    # 依次读取每一行，并查询所属运营商
    for row in reader:
        ip = row[4] # IP地址所在的列为第5列，下标为4
        url = url_template.format(ip=ip)
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            data = json.loads(data)
            if data['status'] == 'success':
                isp = data['isp']
                # 判断所属运营商
                if any(keyword in isp for keyword in unicom_keywords):
                    unicom_writer.writerow(row)
                elif any(keyword in isp for keyword in mobile_keywords):
                    mobile_writer.writerow(row)
                elif any(keyword in isp for keyword in telecom_keywords):
                    telecom_writer.writerow(row)
                else:
                    print(isp)
    # 关闭文件
    unicom_file.close()
    mobile_file.close()
    telecom_file.close()
