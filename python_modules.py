"""
View your module’s documentation with the terminal command pydoc3 cisco_routers. You can exit the documentation page by pressing q.
Open the Python interpreter with the terminal command python. In the Python shell, type help('cisco_routers') to view your module’s documentation via the built-in help() function. You can exit this documentation by pressing q as well.
"""
import cisco_routers
csr = cisco_routers.ciscoIOS('10.254.0.1', username='cisco', password='cisco')
print(csr.get_interface_IPs())
print(csr.get_ip_arp(as_dataframe=True))
