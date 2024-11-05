import requests, json

class F5LTM():

      def __init__(self, ip, port=22, username=None, password=None, device_type=None):
        """
        Establishes connection to target device.
        
        :param str IP:              IP address of target device.
        :param int port:            port for connection
        :param str username:        username for authentication
        :param str password:        password for authentication
        :param str device_type:     LTM, GTM etc.
        """
        self.ip = ip
        self.port = port
        self.device_type = device_type
        self.username = username
        self.password = password

      def get_token(self):
        """
        Returns an authentication token for API access.
        """
        body = {
            "username": self.username,
            "password": self.password,
            "loginProviderName": "tmos"
        }
        
        token_response = requests.post(
            f'https://{self.ip}/mgmt/shared/authn/login',
            verify=False,
            auth=(self.username, self.password),json=body)\
            .json()
        token = token_response['token']['token']
        return token
        
