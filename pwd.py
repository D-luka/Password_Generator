import itertools


size = input('[!] Provide a size [ex: "1 to 8" = 1:8] : ')

start = size.split(':')[0]
end = size.split(':')[1]

personal = str(input("\n [*] Do you want to enter personal data? [y/n]" ))

if personal == 'y':
    full_name = str(input("\n [*] Full name [SKIP WITH ENTER]: "))
    birthday = str(input("\n [*] Birthday [SKIP WITH ENTER]: "))
    month = str(input("\n [*] Month [SKIP WITH ENTER]: "))
    year = str(input("\n [*] Year [SKIP WITH ENTER]: "))
    chs = full_name + birthday + month + year

else:
    chs = 'abcdefghijklmnopqrstuvwxyz'

chs_up = chs.upper()
chs_specials = '|!\][/?.,~-~";:><@#$%&`()_+\''
chs_numerics = '1234567890'

file_name = input('\n [!] Insert a name for wordlist file: ')

arq = open(file_name, 'w')

if input('\n [?] Do you want to use uppercase characters? (y/n): ') == 'y':
    chs = ''.join([chs, chs_up])

if input('\n [?] Do you want to use specials characters? (y/n): ') == 'y':
    chs = ''.join([chs, chs_specials])

if input('\n [?] Do you want to use numerics characters? (y/n): ') == 'y':
    chs= ''.join([chs, chs_numerics])

for i in range(int(start), int(end)+1):
    for j in itertools.product(chs, repeat=1):
        temp = ''.join(j)
        print(temp)
        arq.write(temp + '\n')

arq.close