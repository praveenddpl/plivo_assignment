import requests
import json


class Msg():
	auth_id='******************'
	auth_token='*******************'
	sub_auth_id='******************'
	sub_auth_token='****************'
	base_url='https://api.plivo.com/v1/Account/'
		
	def account(self):
		response=requests.get(self.base_url+self.auth_id, auth=(self.auth_id,self.auth_token))
		return response.json()

	def send_message(self,src,dst,text):
		response=requests.post(self.base_url+self.auth_id+'/Message/', 
			                   auth=(self.auth_id,self.auth_token),
			                   json={'src':src,'dst':dst,'text':text})
		print response.status_code
		if response.status_code==202:
			return response.json()
	def msg_details(self,uuid):
		response=requests.get(self.base_url+self.auth_id+'/Message/'+uuid,
		                      auth=(self.auth_id,self.auth_token))
		print response.status_code
		return response.json()

	def msg_price(self, country):
		response = requests.get(self.base_url+self.auth_id+'/Pricing/', auth=(self.auth_id, self.auth_token), params = {'country_iso' : country} )
		return response.json()




