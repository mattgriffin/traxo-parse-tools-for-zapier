#print(input_data['raw'])

import json
book=json.loads(input_data['raw'])

for segment in book["data"]["object"]["segments"]:
    #hotel segment extract
    if segment["type"] == 'Hotel':
        #print(book["data"]["object"]["id"])
        email_id = book["data"]["object"]["id"]
        mailbox_id = book["data"]["object"]["mailbox_id"]
        created = book["data"]["object"]["created"]
        parse_status = book["data"]["object"]["status"]
        parse_class =  book["data"]["object"]["class"]
        user_address = book["data"]["object"]["user_address"]
        #print segment["type"]
        segment_type = segment["type"]
        hotel_name = segment["hotel_name"]
        checkin_date = segment["checkin_date"]
        checkout_date = segment["checkout_date"]
        booking_source = segment["source"]
        booking_status = segment["status"]
        
output = [{'email_id': email_id, 'mailbox_id': mailbox_id, 'created': created, 'parse_status': parse_status, 'parse_class': parse_class, 'user_address': user_address, 'segment_type': segment_type, 'hotel_name': hotel_name, 'checkin_date': checkin_date, 'checkout_date': checkout_date, 'booking_source': booking_source, 'booking_status': booking_status}]
#output = [{'id': 123, 'hello': 'world'}]
