def isLeapyear(year):
  if(year %4==0 and year%100!=0)or year %400==0:
      return True
  else:
      return false

year=int(input("Enter a year :"))

if isLeapyear(year):
 print('{}isLeap year .'.format(year))
else:
 print('{}is not a Leap year.'.format(year))