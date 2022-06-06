import colorama, string, os, time, random, subprocess, requests
from  colorama import Fore, Back, Style


def logo_():

    print(Fore.LIGHTBLACK_EX + '''
                                 ██▒   █▓ ██▓  ██████  █    ██  ▄▄▄       ██▓    
                                ▓██░   █▒▓██▒▒██    ▒  ██  ▓██▒▒████▄    ▓██▒    
                                 ▓██  █▒░▒██▒░ ▓██▄   ▓██  ▒██░▒██  ▀█▄  ▒██░    
                                  ▒██ █░░░██░  ▒   ██▒▓▓█  ░██░░██▄▄▄▄██ ▒██░    
                                   ▒▀█░  ░██░▒██████▒▒▒▒█████▓  ▓█   ▓██▒░██████▒
                                   ░ ▐░  ░▓  ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒  ▒▒   ▓▒█░░ ▒░▓  ░
                                   ░ ░░   ▒ ░░ ░▒  ░ ░░░▒░ ░ ░   ▒   ▒▒ ░░ ░ ▒  ░
                                     ░░   ▒ ░░  ░  ░   ░░░ ░ ░   ░   ▒     ░ ░   
                                      ░   ░        ░     ░           ░  ░    ░  ░
                                     ░        

                                            https://discord.gg/ZqURQFra7B
    ''')

os.system('cls')

print(Fore.BLACK + '')

os.system('cls')

time.sleep(1.8)

hardwareid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

site = requests.get("https://pastebin.com/raw/AjFt30Ai")

try:

    if hardwareid in site.text:

        pass

    else:

        logo_()

        print(Fore.LIGHTBLACK_EX + '                                              Your are not whitelistet!')

        print(f'                                    Your Hwid is {hardwareid}')

        input()

        exit(0)

except:

    print('failed to connect to database')

    time.sleep(10)

os.system('cls')

logo_()

print('')

User = input(Fore.LIGHTBLACK_EX + '                                               Enter your username: ')



if User == 'yce':

    Pass = input(Fore.LIGHTBLACK_EX + '                                               Enter your password: ')


    if Pass == 'yce':

        time.sleep(2.8)

        os.system('cls')

        logo_()

        print('')

        print(Fore.WHITE + '                                              Connecting to Blockchain...')

        time.sleep(10)

        os.system('cls')

        logo_()

        walletCheck = input(Fore.LIGHTBLACK_EX + '                                                       Wallet : ')

        walletCheck = requests.get("https://www.blockchain.com/eth/address/" + walletCheck)


        if walletCheck.status_code == 200:

            time.sleep(.8)

            os.system('cls')

            logo_()

            print(Fore.GREEN + '                                                     Wallet found !')

            time.sleep(2.3)

            os.system('cls')

            logo_()

            yn = input(Fore.LIGHTBLACK_EX + '                                                     Start y/n: ')


            if yn == 'y':

                time.sleep(3.8)

                os.system('cls')

                tries = 0

                while(True):

                    if(tries > random.randint(10000, 100000)):

                        print(Fore.CYAN + '   [' + Fore.WHITE + '-' + Fore.CYAN + '] ' + Fore.GREEN +  '0x' + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(40)) + Fore.CYAN + ' ' + '-> ' +  str(round(random.uniform(0,2), 4)), "ETH")

                        time.sleep(1)

                        print(Fore.GREEN +"   Sending ETH to your Wallet")

                        time.sleep(10)

                        tries = 0

                        print(Fore.GREEN + "   Done!")

                        time.sleep(1)

                    else:

                        print(Fore.CYAN + '   [' + Fore.WHITE + '-' + Fore.CYAN + '] ' + Fore.WHITE + '0x' + ''.join(random.choice(string.ascii_letters + string.digits) for i in range(40)) + Fore.CYAN + ' -> 0.0000 ETH')

                        tries += 1
                
                
            else:

                os.system('cls')

                logo_()

                print(Fore.LIGHTBLACK_EX + '                                                  have a nice day <3') 

                time.sleep(5)

                exit(0)    

        else:

            os.system('cls')

            logo_()

            print(Fore.RED + '                                                  Wallet not found !') 

            time.sleep(5)

            exit(0)     

    else:
        
        os.system('cls')

        logo_()

        print(Fore.RED + '                                                  wrong password !') 

        time.sleep(5)

        exit(0)

else:

    os.system('cls')

    logo_()

    print(Fore.RED + '                                                  wrong username !') 

    time.sleep(5)

    exit(0)

