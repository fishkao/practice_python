# contab -e 
# */5 * * * * sh  /home/fishzhao/monitor.sh

ip=220.181.30.53
count=100
 
/usr/local/sbin/mtr -c $count -r $ip | awk ' 
BEGIN {print "monitor '$ip'" }
{if( NR>2 && ($3 > "10.0%" || $6 > 50.0)) print $0 }
END {print "end of monitor"} '  >> /tmp/mlog
