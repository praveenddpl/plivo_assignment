from message import Msg

ms=Msg()

"""To know available credit in Account""" 
cash_credit=ms.account()
print 'cash credit in account before sending msg',cash_credit['cash_credits']


"""To send text message from any src number to any dst number"""
src=xxxxxxxxxxxx 
dst=xxxxxxxxxxxx 
text= 'xxxxxxxxxx'
sendmsg=ms.send_message(src,dst,text)

uuid=sendmsg['message_uuid'][0]


"""To get message details """
msgdetails=ms.msg_details(uuid)
print 'price deducted for the sending message',msgdetails['total_rate']


"""To know the rate of the message for specific country"""
country='US'
price=ms.msg_price(country)
msg_cost=price['message']['outbound']['rate']
print msg_cost


"""To verify the rate and the price deducted for the sending message"""
if msg_cost == msgdetails['total_rate']:
    print "price deducted for sending msg"
else:
    print "price not deducted"


"""cash credit available after sending message"""
cash_credit=ms.account()
print 'cash credit in account after sending msg',cash_credit['cash_credits']

