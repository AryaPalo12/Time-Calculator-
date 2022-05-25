def add_time(ix, ip = None, day_n = None):
  if ip == None :
    new_time = f"{ix}"
  day=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  new_time = ""
  day_count = 0
  day_now = 0
  sm = ix.rsplit(":")
  sm1 = sm[1].rsplit(" ")
  hour = int(sm[0])
  minute = int(sm1[0])
  ampm = str(sm1[1])
  sp = ip.rsplit(":")
  hour_p = int(sp[0])
  minute_p = int(sp[1])
  hour_tot = hour + hour_p
  minute_tot = minute + minute_p
  if minute_tot >= 60 :
    minute_tot = minute_tot%60
    hour_tot +=1
    minute_tot = f"{minute_tot:02d}"
  elif minute_tot < 60 :
    minute_tot = f"{minute_tot:02d}"
  while hour_tot >=12 :
    if hour_tot > 12 :
      hour_tot = hour_tot - 12
    else :
      hour_tot = 12
    if ampm =='AM':
      ampm = 'PM'
    elif ampm =='PM' :
      ampm ='AM'
      day_count+=1
  if day_n != None :
    day_now = day.index(day_n.title())
    day_now = day_now + day_count
    while day_now > 6 :
      day_now -= 7
  day_shown = day[day_now]
  if day_n == None :
    if day_count < 1 :
      new_time += f"{hour_tot}:{minute_tot} {ampm}"
    elif day_count == 1 :
        new_time += f"{hour_tot}:{minute_tot} {ampm} (next day)"
    elif day_count > 1 :
      new_time += f"{hour_tot}:{minute_tot} {ampm} ({day_count} days later)"
  else :
    if day_count < 1 :
      new_time += f"{hour_tot}:{minute_tot} {ampm}, {day_shown}"
    elif day_count == 1:
      new_time += f"{hour_tot}:{minute_tot} {ampm}, {day_shown} (next day)"
    elif day_count > 1:
      new_time += f"{hour_tot}:{minute_tot} {ampm}, {day_shown} ({day_count} days later)"
        
  return new_time