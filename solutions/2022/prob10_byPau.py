state = str(input())
ranks = ['Admiral' , 'Captain' , 'Commander' , 'Lieutenant' , 'Officer']
placeholder = ['From:', 'From rank:', 'To:', 'To rank:', 'Content:', 'Timestamp:']


if state == 'S':
  
  clist = []
  
  for x in range(6):
    c = input().rstrip()
    clist.append(c)
    if c not in ranks and x == 1 and x==3:
        print("Invalid input.")
        exit()
  
  if ranks.index(clist[1]) < ranks.index(clist[3]) and 'URGENT' not in clist:
    print('URGENT,' + ",".join(clist))
  else:
    print(','.join(clist))
    
elif state == 'R':
  
    clist = input().split(',')
    if clist[1] not in ranks or clist[3] not in ranks:
      print("Invalid input.")
      exit()
      
    if ranks.index(clist[1]) < ranks.index(clist[3]) and 'URGENT' not in clist:
      print('<<< URGENT >>>')
    else:
      print(f'<<< {clist} >>>')
      clist.remove(clist[0])

  
    for c in clist:
      print(f'{placeholder[clist.index(c)]} {c}')
else:
  print('Invalid input.')