# Automatically subnet a block of IPv4 addresses given the following information:
# a) Type of subnetting (FLSM or VLSM)
# b) The block of IPv4 addresses in CIDR notation
# c) The number of subnets

# If user chose VLSM, ask for the number of usable IPv4 address in each subnet

# Output:
# Network address
# Broadcast address
# Subnet mask in CIDR notation

from sys import exit


def main():
    
    #ipAdd = getIpAddress()
    
    options = {'1' : 'FLSM', '2' : 'VLSM', '3' : 'quit'}
    option = ''
    
    while option not in options:
        
        option = input('Which type of subnetting do you want to subnet?\n1) FLSM\n2) VLSM\n3) Quit\n>> ')
        
        if option not in options:
            
            print('Invalid option\n')
            
    #options[option]
    

if __name__ == '__main__':
    main()