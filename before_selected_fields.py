import requests, csv

headers = {'Authorization': 'Bearer 12345678-abcd-1234-abcd-1234567890ab'}
url = 'https://api.carrierx.com/core/v2/calls/call_drs'

date = '2020-03-15'
i = 1
params = {
'limit': '1',
'order': 'date_stop asc',
'filter': f'date_stop ge {date}'
}
r = requests.get(url, headers=headers, params=params)
dr_items = r.json()['items']
if len(dr_items):
    with open('calls.csv', 'w', encoding='UTF8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_header = ['dr_sid','date_start','number_src','number_dst','direction','duration','price']
        csv_writer.writerow(csv_header)
        dr_sid = dr_items[0]['dr_sid']
        csv_row = [dr_items[0]['dr_sid'],dr_items[0]['date_start'],dr_items[0]['number_src'],dr_items[0]['number_dst'],dr_items[0]['direction'],dr_items[0]['duration'],dr_items[0]['price']]
        csv_writer.writerow(csv_row)
        print(f"{i}. {dr_items[0]['dr_sid']}")
        while True:
            params = {
            'limit': '100',
            'order': 'date_stop asc',
            'after': dr_sid
            }
            r = requests.get(url, headers=headers, params=params)
            if len(r.json()['items']):
                dr_items = r.json()['items']
                for item in dr_items:
                    i += 1
                    dr_sid = dr_items[len(r.json()['items']) - 1]['dr_sid']
                    csv_row = [item['dr_sid'],item['date_start'],item['number_src'],item['number_dst'],item['direction'],item['duration'],item['price']]
                    csv_writer.writerow(csv_row)
                    print(f"{i}. {item['dr_sid']}")
            else:
                print('No more new calls')
                break
else:
    print(f'No calls since {date}')