import requests

class MobileError(Exception):
      pass


class MobileQIWI:
      def __init__(self, phone=None, pin=None, refresh_token=None):
            self.phone = phone
            self.pin = pin
            self.refresh_token = refresh_token
            self.conf_id = None
            self.code = None

      def sendCode(self):
            if self.phone == None:
                  raise MobileError("For this func you should use 'phone'")
            data = requests.post('https://mobile-api.qiwi.com/oauth/authorize',
                                    data={'response_type':'urn:qiwi:oauth:response-type:confirmation-id',
                                          'username':self.phone.replace('+', ''),
                                          'client_id':'android-qw',
                                          'client_secret':'zAm4FKq9UnSe7id'}).json()
            if 'confirmation_id' not in data.keys():
                  raise MobileError("too many attempts. Try later")
            else:
                  self.conf_id = data['confirmation_id']

      def login(self, vcode):
            if self.phone == None:
                  raise MobileError("For this func you should use 'phone'")
            data = requests.post('https://mobile-api.qiwi.com/oauth/authorize',
                                          data={'response_type':'code',
                                                'username':self.phone,
                                                'client_id':'android-qw',
                                                'client_secret':'zAm4FKq9UnSe7id',
                                                'vcode':vcode,
                                                'confirmation_id':self.conf_id}).json()
            if 'code' not in data.keys():
                  raise MobileError("'code' not a valid")
            else:
                  self.code = data['code']

      def inputPin(self, pin=None):
            if pin != None:
                  self.pin = pin
            data = requests.post('https://mobile-api.qiwi.com/oauth/token',
                                          data={'grant_type':'urn:qiwi:oauth:grant-type:mobile-pin',
                                                'code':self.code,
                                                'client_id':'android-qw',
                                                'client_secret':'zAm4FKq9UnSe7id',
                                                'mobile_pin':self.pin}).json()
            if 'access_token' not in data.keys():
                  raise MobileError("'pin' not a valid")
            else:
                  return {'refresh_token':data['app_token'], 'token':data['access_token'], 'expires_in':data['expires_in']}

      def refreshToken(self, refresh_token=None, pin=None):
            if refresh_token != None:
                  self.refresh_token = refresh_token
            if pin != None:
                  self.pin = pin
            data = requests.post('https://mobile-api.qiwi.com/oauth/token',
                                          data={'grant_type':'urn:qiwi:oauth:grant-type:app-token',
                                                'app_token':self.refresh_token,
                                                'client_id':'android-qw',
                                                'client_secret':'zAm4FKq9UnSe7id',
                                                'mobile_pin':self.pin}).json()
            if 'access_token' not in data.keys():
                  raise MobileError("'refresh_token' or 'pin' not a valid")
            else:
                  return {'token':data['access_token'], 'expires_in':data['expires_in']}
