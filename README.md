Esta é uma ferramenta Pentest que automatiza o processo de criação de cargas úteis. Estão incluídos os seguintes formatos:

Android (apk) Windows (exe) Linux (elf) Mac (macho) Php (php) Python (py) Bash (sh) Perl (pl)

Instalação
Execute o seguinte comando como superusuário: ~ # bash install.sh

Fim
Então, ratloader será capaz de trabalhar, para executá-lo, execute o arquivo 'main.py' ou o comando 'ratloader'

Erros
Se você receber um erro ao tentar criar uma carga útil para o Windows, é por causa de sua versão metasploit ... Para atualizá-lo digite: ~ # apt-get remove metasploit-framework ~ # curl https://raw.githubusercontent.com/ rapid7 / metasploit-omnibus / master / config / templates / metasploit-framework-wrappers / msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall Ou, para qualquer outro erro envolvendo metasploit, talvez seja por causa de seu banco de dados, para corrigi-lo , digite: ~ # msfdb delete && msfdb init
