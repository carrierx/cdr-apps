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
        csv_head = []
        for key in dr_items[0]:
            csv_head.append(key)
        csv_writer.writerow(csv_head)
        dr_sid = dr_items[0]['dr_sid']
        csv_row_full = []
        for key in dr_items[0]:
            csv_row_full.append(dr_items[0][key])
        csv_writer.writerow(csv_row_full)
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
                    csv_row_full = []
                    dr_sid = dr_items[len(r.json()['items']) - 1]['dr_sid']
                    for key in item:
                        csv_row_full.append(item[key])
                    csv_writer.writerow(csv_row_full)
                    print(f"{i}. {item['dr_sid']}")
            else:
                print('No more new calls')
                break
else:
    print(f'No calls since {date}')