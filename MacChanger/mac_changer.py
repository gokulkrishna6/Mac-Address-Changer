import subprocess  
import optparse  

 
def args():
    parser = optparse.OptionParser()  
    parser.add_option("-d", "--device", dest="device", help="Device to change MAC address")
    parser.add_option("-m", "--mac_address", dest="mac_address", help="New MAC address to set")
    (options, args) = parser.parse_args()  
    if not options.device:   
        parser.error("[+] Please provide the device name (use -d option).")
    elif not options.mac_address:  
        parser.error("[+] Please provide the new MAC address (use -m option).")
    return options 

 
def mac_address_change_fun(device, new_mac):
    print("[+] Changing MAC address for " + device + " to " + new_mac) 
    subprocess.call(["ifconfig", device, "down"])
    subprocess.call(["ifconfig", device, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", device, "up"])

 
options = args()
mac_address_change_fun(options.device, options.mac_address)
