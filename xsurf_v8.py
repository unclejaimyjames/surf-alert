#--------------------- TO DO --------------------
#TODO make time between updates dynamic
#TODO start script on specific time: https://schedule.readthedocs.io/en/stable/
#TODO email upon boot pi ("surf.py succesfully initiated at #time")
#TODO change conditions to absMaxBreakingHeight

#---------------------------- -------------------

import sched
import datetime, time
import urllib2
import datetime
import json
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "surfmelding@gmail.com"
toaddrs  = ['jaimyvanderheijden@gmail.com']
#toaddrs  = ['jaimyvanderheijden@gmail.com', 'guidovanderheijden@gmail.com', 'emma.wagner@nibc.com']

username = "surfmelding@gmail.com"
password = "surfsurfsurf"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = ", ".join(toaddrs)

url1 = 'http://magicseaweed.com/api/149ef032c0d1dd2d26397212fa0658ad/forecast/?spot_id=145&fields=localTimestamp,wind.*'
url = 'http://magicseaweed.com/api/149ef032c0d1dd2d26397212fa0658ad/forecast/?spot_id=145&fields=localTimestamp,swell.*'
green = 1
count = 0

# VARIABELEN: condities 1 (offshore wind)
wind_direction_min       = 50
wind_direction_max       = 240
wind_speed_max           = 40
swell_height_min          = 0.29
swell_period_min          = 3.9
swelldirection_min  = 70
swelldirection_max  = 200

# VARIABELEN: condities 2 (golven) windrichting maakt niet uit
qdirection_min       = 359
qdirection_max       = 1
qspeed_max           = 20
qheight_min          = 0.39
qperiod_min          = 4.9
qswelldirection_min  = 90
qswelldirection_max  = 210


# Scheduler - time defined below
class PeriodicScheduler(object):
    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def setup(self, interval, action, actionargs=()):
        action(*actionargs)
        self.scheduler.enter(interval, 1, self.setup,
                             (interval, action, actionargs))

    def run(self):
        self.scheduler.run()


# This is the event to execute every time
def periodic_event():
    # get current time
    now = datetime.datetime.now()
    timenow = now.strftime("%Y-%m-%d %H:%M")
    print "Script initiated:\t %s" % timenow

    data = json.load(urllib2.urlopen(url1))
    dataswell = json.load(urllib2.urlopen(url))

    #   --------    WIND DATA   --------
    if green == 1:

        # 06:00 next day
        dat06 = data[10:11]
        for item in dat06:
            wind06 = item.get("wind")
            lt06 = item.get("localTimestamp")
            wind_direction06 = wind06.get('direction')
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
        print "WIND DATA NOT REDEFINED"

    #   --------    SWELL DATA   --------
    if green == 1:

        # 06:00 next day
        dats06 = dataswell[10:11]
        for item in dats06:
            swell06 = item.get("swell")
            components06 = swell06.get('components')
            combined06 = components06.get('combined')
            primary06 = components06.get('primary')
            absMaxBreakingHeight06 = swell06.get('absMaxBreakingHeight')
            absMinBreakingHeight06 = swell06.get('absMinBreakingHeight')
            maxBreakingHeight06 = swell06.get('maxBreakingHeight')
            minBreakingHeight06 = swell06.get('minBreakingHeight')
            combined_direction06 = combined06.get('direction')
            combined_compassdirection06 = combined06.get('compassDirection')
            combined_period06 = combined06.get('period')
            combined_height06 = combined06.get('height')
            primary_direction06 = primary06.get('direction')
            primary_compassdirection06 = primary06.get('compassDirection')
            primary_period06 = primary06.get('period')
            swell_primary_height06 = primary06.get('height')

        # 09:00 next day
        dats09 = dataswell[11:12]
        for item in dats09:
            swell09 = item.get("swell")
            components09 = swell09.get('components')
            combined09 = components09.get('combined')
            primary09 = components09.get('primary')
            absMaxBreakingHeight09 = swell09.get('absMaxBreakingHeight')
            absMinBreakingHeight09 = swell09.get('absMinBreakingHeight')
            maxBreakingHeight09 = swell09.get('maxBreakingHeight')
            minBreakingHeight09 = swell09.get('minBreakingHeight')
            combined_direction09 = combined09.get('direction')
            combined_compassdirection09 = combined09.get('compassDirection')
            combined_period09 = combined09.get('period')
            combined_height09 = combined09.get('height')
            primary_direction09 = primary09.get('direction')
            primary_compassdirection09 = primary09.get('compassDirection')
            primary_period09 = primary09.get('period')
            primary_height09 = primary09.get('height')

        # 12:00 next day
        dats12 = dataswell[12:13]
        for item in dats12:
            swell12 = item.get("swell")
            components12 = swell12.get('components')
            combined12 = components12.get('combined')
            primary12 = components12.get('primary')
            absMaxBreakingHeight12 = swell12.get('absMaxBreakingHeight')
            absMinBreakingHeight12 = swell12.get('absMinBreakingHeight')
            maxBreakingHeight12 = swell12.get('maxBreakingHeight')
            minBreakingHeight12 = swell12.get('minBreakingHeight')
            combined_direction12 = combined12.get('direction')
            combined_compassdirection12 = combined12.get('compassDirection')
            combined_period12 = combined12.get('period')
            combined_height12 = combined12.get('height')
            primary_direction12 = primary12.get('direction')
            primary_compassdirection12 = primary12.get('compassDirection')
            primary_period12 = primary12.get('period')
            primary_height12 = primary12.get('height')

        # 15:00 next day
        dats15 = dataswell[13:14]
        for item in dats15:
            swell15 = item.get("swell")
            components15 = swell15.get('components')
            combined15 = components15.get('combined')
            primary15 = components15.get('primary')
            absMaxBreakingHeight15 = swell15.get('absMaxBreakingHeight')
            absMinBreakingHeight15 = swell15.get('absMinBreakingHeight')
            maxBreakingHeight15 = swell15.get('maxBreakingHeight')
            minBreakingHeight15 = swell15.get('minBreakingHeight')
            combined_direction15 = combined15.get('direction')
            combined_compassdirection15 = combined15.get('compassDirection')
            combined_period15 = combined15.get('period')
            combined_height15 = combined15.get('height')
            primary_direction15 = primary15.get('direction')
            primary_compassdirection15 = primary15.get('compassDirection')
            primary_period15 = primary15.get('period')
            primary_height15 = primary15.get('height')

        # 18:00 next day
        dats18 = dataswell[14:15]
        for item in dats18:
            swell18 = item.get("swell")
            components18 = swell18.get('components')
            combined18 = components18.get('combined')
            primary18 = components18.get('primary')
            absMaxBreakingHeight18 = swell18.get('absMaxBreakingHeight')
            absMinBreakingHeight18 = swell18.get('absMinBreakingHeight')
            maxBreakingHeight18 = swell18.get('maxBreakingHeight')
            minBreakingHeight18 = swell18.get('minBreakingHeight')
            combined_direction18 = combined18.get('direction')
            combined_compassdirection18 = combined18.get('compassDirection')
            combined_period18 = combined18.get('period')
            combined_height18 = combined18.get('height')
            primary_direction18 = primary18.get('direction')
            primary_compassdirection18 = primary18.get('compassDirection')
            primary_period18 = primary18.get('period')
            primary_height18 = primary18.get('height')

        # 21:00 next day
        dats21 = dataswell[15:16]
        for item in dats21:
            swell21 = item.get("swell")
            components21 = swell21.get('components')
            combined21 = components21.get('combined')
            primary21 = components21.get('primary')
            absMaxBreakingHeight21 = swell21.get('absMaxBreakingHeight')
            absMinBreakingHeight21 = swell21.get('absMinBreakingHeight')
            maxBreakingHeight21 = swell21.get('maxBreakingHeight')
            minBreakingHeight21 = swell21.get('minBreakingHeight')
            combined_direction21 = combined21.get('direction')
            combined_compassdirection21 = combined21.get('compassDirection')
            combined_period21 = combined21.get('period')
            combined_height21 = combined21.get('height')
            primary_direction21 = primary21.get('direction')
            primary_compassdirection21 = primary21.get('compassDirection')
            primary_period21 = primary21.get('period')
            primary_height21 = primary21.get('height')
    else:
        print "SWELL DATA NOT REDEFINED"

    #   ---------   BODY OF MESSAGE   ---------
    #TODO Hier moet de HTML body van bericht komen

    #   ---------   IF STATEMENTS   ---------
    if  wind_direction06 < wind_direction_min \
        and speed06 < wind_speed_max\
        and swell_primary_height06 > swell_height_min\
        and primary_period06 > swell_period_min\
        and swelldirection_min < primary_direction06 < swelldirection_max \
        or wind_direction06 > wind_direction_max \
        and speed06 < wind_speed_max \
        and swell_primary_height06 > swell_height_min \
        and primary_period06 > swell_period_min \
        and swelldirection_min < primary_direction06 < swelldirection_max:

        msg['Subject'] = "Offshore wind, morgen van af 06:00!"
        spec = "Kijk even of er golfhoogte is. De wind staat iig goed!\n\n" \
               "Golf hoogte: %d\n" \
               "Periode: %d\n" \
               "Wind richting: %s\n" \
               "Wind snelheid: %d\n" \
               "\nCheck MSW voor de forecast: https://magicseaweed.com/Scheveningen-Nord-Surf-Report/145/" \
               "\n\n- powered by Jaimy's surf alarm -" \
               % (swell_primary_height06, primary_period06, compass06, speed06)

        msg.attach(MIMEText(spec, 'plain'))
        text = msg.as_string()
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, text)
            server.quit()
            print "email sent"
        except:
            print "email error"
    elif direction09 < wind_direction_min \
        and speed09 < wind_speed_max\
        and primary_height09 > swell_height_min\
        and primary_period09 > swell_period_min\
        and swelldirection_min < primary_direction09 < swelldirection_max \
        or direction09 > wind_direction_max \
        and speed09 < wind_speed_max \
        and primary_height09 > swell_height_min \
        and primary_period09 > swell_period_min \
        and swelldirection_min < primary_direction09 < swelldirection_max:

        msg['Subject'] = "Offshore wind, morgen rond 09:00!"
        spec = "He zou zo maar kunnen dat er nog wat te surfen valt... De wind staat iig goed!\n\n" \
               "Golf hoogte: %d\n" \
               "Periode: %d\n" \
               "Wind richting: %s\n" \
               "Wind snelheid: %d\n" \
               "\nCheck MSW voor de forecast: https://magicseaweed.com/Scheveningen-Nord-Surf-Report/145/" \
               "\n\n- powered by Jaimy's surf alarm -" \
               % (primary_height09, primary_period09, compass09, speed09)

        msg.attach(MIMEText(spec, 'plain'))
        text = msg.as_string()
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, text)
            server.quit()
            print "email sent"
        except:
            print "email error"
    elif direction12 < wind_direction_min \
        and speed12 < wind_speed_max\
        and primary_height12 > swell_height_min\
        and primary_period12 > swell_period_min\
        and swelldirection_min < primary_direction12 < swelldirection_max \
        or direction12 > wind_direction_max \
        and speed12 < wind_speed_max \
        and primary_height12 > swell_height_min \
        and primary_period12 > swell_period_min \
        and swelldirection_min < primary_direction12 < swelldirection_max:

        msg['Subject'] = "Offshore wind, morgen rond 12:00!"
        spec = "Wellicht het thuis werken waard...? \n\n" \
               "Golf hoogte: %d\n" \
               "Periode: %d\n" \
               "Wind richting: %s\n" \
               "Wind snelheid: %d\n" \
               "\nCheck MSW voor de forecast: https://magicseaweed.com/Scheveningen-Nord-Surf-Report/145/" \
               "\n\n- powered by Jaimy's surf alarm -" \
               % (primary_height12, primary_period12, compass12, speed12)

        msg.attach(MIMEText(spec, 'plain'))
        text = msg.as_string()
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, text)
            server.quit()
            print "email sent"
        except:
            print "email error"
    elif direction15 < wind_direction_min \
        and speed15 < wind_speed_max\
        and primary_height15 > swell_height_min\
        and primary_period15 > swell_period_min\
        and swelldirection_min < primary_direction15 < swelldirection_max \
        or direction15 > wind_direction_max \
        and speed15 < wind_speed_max \
        and primary_height15 > swell_height_min \
        and primary_period15 > swell_period_min \
        and swelldirection_min < primary_direction15 < swelldirection_max:

        msg['Subject'] = "Offshore wind, morgen om 15:00!"
        spec = "Heb je morgen tijd voor een middag pauze? De wind staat iig goed!\n\n" \
               "Golf hoogte: %d\n" \
               "Periode: %d\n" \
               "Wind richting: %s\n" \
               "Wind snelheid: %d\n" \
               "\nCheck MSW voor de forecast: https://magicseaweed.com/Scheveningen-Nord-Surf-Report/145/" \
               "\n\n- powered by Jaimy's surf alarm -" \
               % (primary_height15, primary_period15, compass15, speed15)

        msg.attach(MIMEText(spec, 'plain'))
        text = msg.as_string()
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, text)
            server.quit()
            print "email sent"
        except:
            print "email error"
    elif direction18 < wind_direction_min \
        and speed18 < wind_speed_max\
        and primary_height18 > swell_height_min\
        and primary_period18 > swell_period_min\
        and swelldirection_min < primary_direction18 < swelldirection_max \
        or direction18 > wind_direction_max \
        and speed18 < wind_speed_max \
        and primary_height18 > swell_height_min \
        and primary_period18 > swell_period_min \
        and swelldirection_min < primary_direction18 < swelldirection_max:

        msg['Subject'] = "Offshore wind, morgen van rond 18:00!"
        spec = "Vroeg weg van je werk want er zouden zo maar mooie golven mee kunnen komen!\n\n" \
               "Golf hoogte: %d\n" \
               "Periode: %d\n" \
               "Wind richting: %s\n" \
               "Wind snelheid: %d\n" \
               "\nCheck MSW voor de forecast: https://magicseaweed.com/Scheveningen-Nord-Surf-Report/145/" \
               "\n\n- powered by Jaimy's surf alarm -" \
               % (primary_height18, primary_period18, compass18, speed18)

        msg.attach(MIMEText(spec, 'plain'))
        text = msg.as_string()
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, text)
            server.quit()
            print "email sent"
        except:
            print "email error"
    elif direction21 < wind_direction_min \
        and speed21 < wind_speed_max\
        and primary_height21 > swell_height_min\
        and primary_period21 > swell_period_min\
        and swelldirection_min < primary_direction21 < swelldirection_max \
        or direction21 > wind_direction_max \
        and speed21 < wind_speed_max \
        and primary_height21 > swell_height_min \
        and primary_period21 > swell_period_min \
        and swelldirection_min < primary_direction21 < swelldirection_max:

        msg['Subject'] = "Offshore wind, morgen rond 21:00!"
        spec = "Check het even met je surfmaatjes want de wind zou zo maar cadeautjes kunnen brengen!\n\n" \
               "Golf hoogte: %d\n" \
               "Periode: %d\n" \
               "Wind richting: %s\n" \
               "Wind snelheid: %d\n" \
               "\nCheck MSW voor de forecast: https://magicseaweed.com/Scheveningen-Nord-Surf-Report/145/" \
               "\n\n- powered by Jaimy's surf alarm -" \
               % (primary_height21, primary_period21, compass21, speed21)

        msg.attach(MIMEText(spec, 'plain'))
        text = msg.as_string()
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, text)
            server.quit()
            print "email sent"
        except:
            print "email error"
    else:

        # -----   CONDITIE 2   -----

        if  wind_direction06 < qdirection_min \
            and speed06 < qspeed_max \
            and swell_primary_height06 > qheight_min \
            and primary_period06 > qperiod_min \
            and qswelldirection_min < primary_direction06 < qswelldirection_max\
            or  wind_direction06 < qdirection_max \
            and speed06 < qspeed_max \
            and swell_primary_height06 > qheight_min \
            and primary_period06 > qperiod_min \
            and qswelldirection_min < primary_direction06 < qswelldirection_max:

            msg['Subject'] = "Kans of surf, morgen om 06:00!"
            spec =  "Zet de wekker en bel je surf buddy!\n\n" \
                    "Golf hoogte: %d\n" \
                    "Periode: %d\n" \
                    "Wind richting: %s\n" \
                    "Wind snelheid: %d\n" \
                    "\nCheck MSW voor de forecast: https://magicseaweed.com/Scheveningen-Nord-Surf-Report/145/" \
                    "\n\n(Vogeltjes die vroeg zingen zijn voor de poes)" \
                    % (swell_primary_height06, primary_period06, compass06, speed06)

            msg.attach(MIMEText(spec, 'plain'))
            text = msg.as_string()
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(username, password)
                server.sendmail(fromaddr, toaddrs, text)
                server.quit()
                print "email sent"
            except:
                print "email error"
        elif direction09 < qdirection_min \
            and speed09 < qspeed_max \
            and primary_height09 > qheight_min \
            and primary_period09 > qperiod_min \
            and qswelldirection_min < primary_direction09 < qswelldirection_max\
            or  direction09 < qdirection_max \
            and speed09 < qspeed_max \
            and primary_height09 > qheight_min \
            and primary_period09 > qperiod_min \
            and qswelldirection_min < primary_direction09 < qswelldirection_max:

            msg['Subject'] = "Chille surf, morgen om 09:00!"
            spec = "Verschuif die eerste meeting naar de middag. Surf in aantocht!\n\n" \
                   "Golf hoogte: %d\n" \
                   "Periode: %d\n" \
                   "Wind richting: %s\n" \
                   "Wind snelheid: %d\n" \
                   "\nCheck MSW voor de forecast: https://magicseaweed.com/Scheveningen-Nord-Surf-Report/145/" \
                   "\n\n- Powered by Jaimy's surf alarm -" \
                   % (primary_height09, primary_period09, compass09, speed09)

            msg.attach(MIMEText(spec, 'plain'))
            text = msg.as_string()
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(username, password)
                server.sendmail(fromaddr, toaddrs, text)
                server.quit()
                print "email sent"
            except:
                print "email error"
        elif direction12 < qdirection_min \
            and speed12 < qspeed_max \
            and primary_height12 > qheight_min \
            and primary_period12 > qperiod_min \
            and qswelldirection_min < primary_direction12 < qswelldirection_max\
            or  direction12 < qdirection_max \
            and speed12 < qspeed_max \
            and primary_height12 > qheight_min \
            and primary_period12 > qperiod_min \
            and qswelldirection_min < primary_direction12 < qswelldirection_max:

            msg['Subject'] = "Chille surf, morgen om 12:00!"
            spec = "Dit wordt een dagje thuis werken... Yeay!\n\n" \
                   "Golf hoogte: %d\n" \
                   "Periode: %d\n" \
                   "Wind richting: %s\n" \
                   "Wind snelheid: %d\n" \
                   "\nCheck MSW voor de forecast: https://magicseaweed.com/Scheveningen-Nord-Surf-Report/145/" \
                   "\n\n- powered by Jaimy's surf alarm -" \
                   % (primary_height12, primary_period12, compass12, speed12)

            msg.attach(MIMEText(spec, 'plain'))
            text = msg.as_string()
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(username, password)
                server.sendmail(fromaddr, toaddrs, text)
                server.quit()
                print "email sent"
            except:
                print "email error"
        elif direction15 < qdirection_min \
            and speed15 < qspeed_max \
            and primary_height15 > qheight_min \
            and primary_period15 > qperiod_min \
            and qswelldirection_min < primary_direction15 < qswelldirection_max\
            or  direction15 < qdirection_max \
            and speed15 < qspeed_max \
            and primary_height15 > qheight_min \
            and primary_period15 > qperiod_min \
            and qswelldirection_min < primary_direction15 < qswelldirection_max:

            msg['Subject'] = "Chille surf, morgen om 15:00!"
            spec = "Gefeliciteerd, je hebt voldoende karma punten verzameld om te kunnen surfen!\n\n" \
                   "Golf hoogte: %d\n" \
                   "Periode: %d\n" \
                   "Wind richting: %s\n" \
                   "Wind snelheid: %d\n" \
                   "\nCheck MSW voor de forecast: https://magicseaweed.com/Scheveningen-Nord-Surf-Report/145/" \
                   "\n\n- powered by Jaimy's surf alarm -" \
                   % (primary_height15, primary_period15, compass15, speed15)

            msg.attach(MIMEText(spec, 'plain'))
            text = msg.as_string()
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(username, password)
                server.sendmail(fromaddr, toaddrs, text)
                server.quit()
                print "email sent"
            except:
                print "email error"
        elif direction18 < qdirection_min \
            and speed18 < qspeed_max \
            and primary_height18 > qheight_min \
            and primary_period18 > qperiod_min \
            and qswelldirection_min < primary_direction18 < qswelldirection_max\
            or  direction18 < qdirection_max \
            and speed18 < qspeed_max \
            and primary_height18 > qheight_min \
            and primary_period18 > qperiod_min \
            and qswelldirection_min < primary_direction18 < qswelldirection_max:

            msg['Subject'] = "Chille surf, morgen om 18:00!"
            spec = "Diner+surf, surf & snack... Maakt me niet uit hoe je het fixt, als je die golven maar pakt!\n\n" \
                   "Golf hoogte: %d\n" \
                   "Periode: %d\n" \
                   "Wind richting: %s\n" \
                   "Wind snelheid: %d\n" \
                   "\nCheck MSW voor de forecast: https://magicseaweed.com/Scheveningen-Nord-Surf-Report/145/" \
                   "\n\n- powered by Jaimy's surf alarm -" \
                   % (primary_height18, primary_period18, compass18, speed18)

            msg.attach(MIMEText(spec, 'plain'))
            text = msg.as_string()
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(username, password)
                server.sendmail(fromaddr, toaddrs, text)
                server.quit()
                print "email sent"
            except:
                print "email error"
        elif direction21 < qdirection_min \
            and speed21 < qspeed_max \
            and primary_height21 > qheight_min \
            and primary_period21 > qperiod_min \
            and qswelldirection_min < primary_direction21 < qswelldirection_max\
            or  direction21 < qdirection_max \
            and speed21 < qspeed_max \
            and primary_height21 > qheight_min \
            and primary_period21 > qperiod_min \
            and qswelldirection_min < primary_direction21 < qswelldirection_max:

            msg['Subject'] = "Chille surf, morgen om 21:00!"
            spec = "Niets beter dan de dag afsluiten met een goede sessie toch? Ja, toch?!\n\n" \
                   "Golf hoogte: %d\n" \
                   "Periode: %d\n" \
                   "Wind richting: %s\n" \
                   "Wind snelheid: %d\n" \
                   "\nCheck MSW voor de forecast: https://magicseaweed.com/Scheveningen-Nord-Surf-Report/145/" \
                   "\n\n- powered by Jaimy's surf alarm -" \
                   % (primary_height21, primary_period21, compass21, speed21)

            msg.attach(MIMEText(spec, 'plain'))
            text = msg.as_string()
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(username, password)
                server.sendmail(fromaddr, toaddrs, text)
                server.quit()
                print "email sent"
            except:
                print "email error"
        else:
            time06 = (datetime.datetime.fromtimestamp(int(lt06)).strftime('%H:%M'))
            print "No conditions met:\t %s" %  timenow


day = 60*60*24
INTERVAL = day  # interval period
periodic_scheduler = PeriodicScheduler()
periodic_scheduler.setup(INTERVAL, periodic_event)  # executes the event just once
periodic_scheduler.run()  # it starts the scheduler




#   --------    Definitions   --------
# swell.absMaxBreakingHeight    -   Upper end of the likely range for breaking wave size on this beach. Absolute Value. Use this for smooth graphing
# swell.maxBreakingHeight       -   Upper end of the likely range for breaking wave size on this beach. Intelligently rounded. Use this for text display


