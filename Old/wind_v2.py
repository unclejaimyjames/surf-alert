
import urllib2
import json
import datetime

urlwnd = \
    'http://magicseaweed.com/api/149ef032c0d1dd2d26397212fa0658ad/forecast/?spot_id=145&fields=localTimestamp,wind.*'

data = json.load(urllib2.urlopen(urlwnd))

green = 1

# IMPORT WIND DATA
if green == 1:
    # 06:00 next day
    dat06 = data[10:11]
    for item in dat06:
        wind06 = item.get("wind")
        lt06 = item.get("localTimestamp")
        direction06 = wind06.get('direction')
        compass06 = wind06.get('compassDirection')
        gusts06 = wind06.get('gusts')
        speed06 = wind06.get('speed')
        chill06 = wind06.get('chill')

    # 09:00 next day
    dat09 = data[11:12]
    for item in dat09:
        wind09 = item.get("wind")
        lt09 = item.get("localTimestamp")
        direction09 = wind09.get('direction')
        compass09 = wind09.get('compassDirection')
        gusts09 = wind09.get('gusts')
        speed09 = wind09.get('speed')
        chill09 = wind09.get('chill')

    # 12:00 next day
    dat12 = data[12:13]
    for item in dat12:
        wind12 = item.get("wind")
        lt12 = item.get("localTimestamp")
        direction12 = wind12.get('direction')
        compass12 = wind12.get('compassDirection')
        gusts12 = wind12.get('gusts')
        speed12 = wind12.get('speed')
        chill12 = wind12.get('chill')

    # 15:00 next day
    dat15 = data[13:14]
    for item in dat15:
        wind15 = item.get("wind")
        lt15 = item.get("localTimestamp")
        direction15 = wind15.get('direction')
        compass15 = wind15.get('compassDirection')
        gusts15 = wind15.get('gusts')
        speed15 = wind15.get('speed')
        chill15 = wind15.get('chill')

    # 18:00 next day
    dat18 = data[14:15]
    for item in dat18:
        wind18 = item.get("wind")
        lt18 = item.get("localTimestamp")
        direction18 = wind18.get('direction')
        compass18 = wind18.get('compassDirection')
        gusts18 = wind18.get('gusts')
        speed18 = wind18.get('speed')
        chill18 = wind18.get('chill')

    # 21:00 next day
    dat21 = data[15:16]
    for item in dat21:
        wind21 = item.get("wind")
        lt21 = item.get("localTimestamp")
        direction21 = wind21.get('direction')
        compass21 = wind21.get('compassDirection')
        gusts21 = wind21.get('gusts')
        speed21 = wind21.get('speed')
        chill21 = wind21.get('chill')
else:
    print "error"

print "\n"
print(datetime.datetime.fromtimestamp(int(lt06)).strftime('%d-%m-%Y %H:%M:%S'))
print "Direction :\t\t\t %s" %  direction06
print "Compass direction :\t %s" %  compass06
print "Gusts (kph) :\t\t %s" %  gusts06
print "Wind speed (kph) :\t %s" %  speed06
print "Chill :\t\t\t\t %s" %  chill06

print "\n"
print(datetime.datetime.fromtimestamp(int(lt09)).strftime('%d-%m-%Y %H:%M:%S'))
print "Direction :\t\t\t %s" %  direction09
print "Compass direction :\t %s" %  compass09
print "Gusts (kph) :\t\t %s" %  gusts09
print "Wind speed (kph) :\t %s" %  speed09
print "Chill :\t\t\t\t %s" %  chill09

print "\n"
print(datetime.datetime.fromtimestamp(int(lt12)).strftime('%d-%m-%Y %H:%M:%S'))
print "Direction :\t\t\t %s" %  direction12
print "Compass direction :\t %s" %  compass12
print "Gusts (kph) :\t\t %s" %  gusts12
print "Wind speed (kph) :\t %s" %  speed12
print "Chill :\t\t\t\t %s" %  chill12

print "\n"
print(datetime.datetime.fromtimestamp(int(lt15)).strftime('%d-%m-%Y %H:%M:%S'))
print "Direction :\t\t\t %s" %  direction15
print "Compass direction :\t %s" %  compass15
print "Gusts (kph) :\t\t %s" %  gusts15
print "Wind speed (kph) :\t %s" %  speed15
print "Chill :\t\t\t\t %s" %  chill15

print "\n"
print(datetime.datetime.fromtimestamp(int(lt18)).strftime('%d-%m-%Y %H:%M:%S'))
print "Direction :\t\t\t %s" %  direction18
print "Compass direction :\t %s" %  compass18
print "Gusts (kph) :\t\t %s" %  gusts18
print "Wind speed (kph) :\t %s" %  speed18
print "Chill :\t\t\t\t %s" %  chill18

print "\n"
print(datetime.datetime.fromtimestamp(int(lt21)).strftime('%d-%m-%Y %H:%M:%S'))
print "Direction :\t\t\t %s" %  direction21
print "Compass direction :\t %s" %  compass21
print "Gusts (kph) :\t\t %s" %  gusts21
print "Wind speed (kph) :\t %s" %  speed21
print "Chill :\t\t\t\t %s" %  chill21

