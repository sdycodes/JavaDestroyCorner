python ../gw.py
res=`grep --max-count=1 "ERROR" ./res.txt`
if [ -n "$res" ];then
	../notifyme.sh -t "ERROR" -c "ERROR found!!" -r s.dy@foxmail.com
else
	../notifyme.sh -t "FINISH" -c "no error found" -r s.dy@foxmail.com
fi

