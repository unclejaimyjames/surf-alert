
import urllib2
import json
import datetime

url = 'http://magicseaweed.com/api/149ef032c0d1dd2d26397212fa0658ad/forecast/?spot_id=145&fields=localTimestamp,swell.*'
data = json.load(urllib2.urlopen(url))
dat = data[10:11]

#print json.dumps(dat, sort_keys=True, indent=4)

for item in dat:
    swell = item.get("swell")
    lt = item.get("localTimestamp")

absMaxBreakingHeight06 = swell.get('absMaxBreakingHeight')
absMinBreakingHeight06 = swell.get('absMinBreakingHeight')
maxBreakingHeight06 = swell.get('maxBreakingHeight')
minBreakingHeight06 = swell.get('minBreakingHeight')

components06 = swell.get('components')
combined06 = components06.get('combined')
primary06 = components06.get('primary')

combined_direction06 = combined06.get('direction')
combined_compassdirection06 = combined06.get('compassDirection')
combined_period06 = combined06.get('period')
combined_height06 = combined06.get('height')

primary_direction06 = primary06.get('direction')
primary_compassdirection06 = primary06.get('compassDirection')
primary_period06 = primary06.get('period')
primary_height06 = primary06.get('height')

print "\n"
print(datetime.datetime.fromtimestamp(int(lt)).strftime('%d-%m-%Y %H:%M:%S'))
print "\n"
print "combined06 :\t\t\t %s" %  combined06
print "primary06 :\t\t\t %s" %  primary06

print "absMaxBreakingHeight :\t\t\t %s" %  absMaxBreakingHeight06
print "absMinBreakingHeight :\t\t\t %s" %  absMinBreakingHeight06
print "maxBreakingHeight :\t\t\t\t %s" %  maxBreakingHeight06
print "minBreakingHeight :\t\t\t\t %s" %  minBreakingHeight06
print(combined_direction06, combined_compassdirection06, combined_period06, combined_height06)
print(primary_direction06, primary_compassdirection06, primary_period06, primary_height06)
