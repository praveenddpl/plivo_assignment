import requests
import json


class Msg():
	auth_id='MAODUZYTQ0Y2FMYJBLOW'
	auth_token='Mzk0MzU1Mzc3MTc1MTEyMGU2M2RlYTIwN2UyMzk1'
	sub_auth_id='SAYZA2MTZJZDLJNWUXZJ'
	sub_auth_token='NTk5NGIzYzVkZDhiNTI2NDExNGY0YzkwYWEzNTll'
	base_url='https://api.plivo.com/v1/Account/'

	
	"""To retrieve account details""" 

	def account(self):
		response=requests.get(self.base_url+self.auth_id, auth=(self.auth_id,self.auth_token))
		return response.json()


	"""For sending message from src to dst"""

	def send_message(self,src,dst,text):
		response=requests.post(self.base_url+self.auth_id+'/Message/', 
			                   auth=(self.auth_id,self.auth_token),
			                   json={'src':src,'dst':dst,'text':text})
		print response.status_code
		if response.status_code==202:
			return response.json()


	"""To get the message details"""

	def msg_details(self,uuid):
		response=requests.get(self.base_url+self.auth_id+'/Message/'+uuid,
		                      auth=(self.auth_id,self.auth_token))
		print response.status_code
		return response.json()


	"""To know the rate for specific country"""
	
	def msg_price(self, country):
		response = requests.get(self.base_url+self.auth_id+'/Pricing/', auth=(self.auth_id, self.auth_token), params = {'country_iso' : country} )
		return response.json()




