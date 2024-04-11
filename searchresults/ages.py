def ageconverter(ages):
  if ages:
    new=str.split(ages,',')
    for i in range(len(new)):
      new[i]=int(new[i])
    return new
  else:
    return []