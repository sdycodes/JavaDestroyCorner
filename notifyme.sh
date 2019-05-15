# author: Shi Dingyuan s.dy@foxmail.com
# requirements:
# 	1 sudo apt install msmtp
#	2 sudo apt install mutt
#	3 touch .msmtprc (better under user root path)
#	4 add below contents to .msmtprc:
#		account default
#		host smtp.aliyun.com
#		from <your email address to send email aliyun is recommended>
#		auth plain
#		user <your email address again>
#		password <your password of email>
#		logfile /var/log/msmtp.log
#	5 touch .muttrc (better under user root path)
#	6 add below contents to .muttrc:
#		set sendmail="/usr/bin/msmtp"  (can get by whereis msmtp)
#		set use_from=yes
# 		set realname="RaspberryPi"
#		set editor="vim"
# 		set crypt_use_gpgme = no
# can also use ./notify.sh --setup
if [ $? != 0 ] ; then echo "Terminating..." >&2 ; exit 1 ; fi
while [ $# -gt 0 ];do
    case "$1" in
        -s|--setup)
            sudo apt install msmtp
            sudo apt install mutt
            echo "account default" >> .msmtprc 
            echo "host smtp.aliyun.com" >> .msmtprc
            echo "from <your email address>" >> .msmtprc
            echo "auth plain" >> .msmtprc
            echo "user <your email address again>" >> .msmtprc
            echo "password <your password of email>" >> .msmtprc
            echo "logfile /var/log/msmtp.log" >> .msmtprc
            echo "set sendmail=\"/usr/bin/msmtp\"" >> .muttrc
            echo "set use_from=yes" >> .muttrc
            echo "set realname=\"RaspberryPi\"" >> .muttrc
            echo "set editor=\"vim\"" >> .muttrc
            echo "set crypt_use_gpgme = no" >> .muttrc
	    exit 0
	    ;;
        -t|--title)
            title=$2
            shift 2
            ;;
        -c|--content)
            contents=$2
            shift 2
            ;;
	    -r|--receiver)
            receiver=$2
            shift 2
            ;;
	    -d|--delete)
            isremove="a"
	        shift
	        ;;
        -v|--version)
	        echo "notify version 1.0 by sdy"
	        exit 0
	        ;;
        -h |--help)
	        echo "-v|--version get the version of notify"
            echo "-t|-title input title of email"
            echo "-c|-contents input the contents of email"
	        echo "-r|--reciever input the reiever of email"
            echo "-d|--delete remove mutt and send file"
    	    exit 0
            ;;
        --)
            shift
            break
            ;;
        *)
            echo "unknown para {$1}, try -h or --help"
            exit 1
            ;;
    esac
done
if [[ -n "$title" || -n "$contents" || -n "$reciever" ]];then 
	echo "sending..."
	echo "title: $title"
	echo "receiver: $receiver"
	echo "contents: $contents"
	echo "$contents" | mutt -s "$title" "$receiver" 
else
	echo "failed:not enough info to send an email"
fi
if [[ -n "$isremove" ]];then
	rm ./mutt
	rm ./sent
fi

