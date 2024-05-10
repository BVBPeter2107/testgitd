
from fritzconnection import FritzConnection

ip = input('IP Addresse der Fritzbox:')
user = input('Username:')
pw = input('Passwort:')
global fc

fc = FritzConnection(address=ip, user=user, password=pw)

print(fc)

def get_link_speed():
    status = fc.call_action('WANCommonInterfaceConfig', 'GetCommonLinkProperties')
    downstream = status['NewLayer1DownstreamMaxBitRate'] / 8.
    upstream = status['NewLayer1UpstreamMaxBitRate'] / 8.
    return (upstream, downstream)


ul, dl = get_link_speed()

print("Uplink:" + str(ul))
print("Downlink:" + str(dl))
