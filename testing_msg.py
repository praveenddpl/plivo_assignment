from message import Msg

ms=Msg()
cash_credit=ms.account()
print 'cash credit in account before sending msg',cash_credit['cash_credits']
src=13252080160 
dst=13238318440 
text= 'hi hello'
sendmsg=ms.send_message(src,dst,text)

uuid=sendmsg['message_uuid'][0]
msgdetails=ms.msg_details(uuid)


country='US'
price=ms.msg_price(country)
msg_cost=price['message']['outbound']['rate']
print msg_cost

if msg_cost == msgdetails['total_rate']:
    print "price deducted for sending msg"
else:
    print "price not deducted"

cash_credit=ms.account()
print 'cash credit in account after sending msg',cash_credit['cash_credits']

