def promedio (a:float,b:float,c:float,d:float,e:float)->float:
    return (a+b+c+d+e)/5
def mediana (a:float,b:float,c:float,d:float,e:float)->float:
  if a<=b and a<=c and a<=d and a<=e :
    n1=a
    if b<=c and b<=d and b<=e :
        n2=b
        if c<=d and c<=e :
            n3=c
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=c and d<=e :
            n3=d
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif e<=c and e<=d :
            n3=e
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
    elif c<=b and c<=d and c<=e :
        n2=c
        if b<=d and b<=e :
            n3=b
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=b and d<=e :
            n3=d
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=d :
            n3=e
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
    elif d<=b and d<=c and d<=e :
        n2=d
        if b<=c and b<=e :
            n3=b
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=b and c<=e :
            n3=c
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=c :
            n3=e
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif e<=b and e<=c and e<=d :
        n2=e
        if b<=c and b<=d :
            n3=b
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=b and c<=d :
            n3=c
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif d<=b and d<=c :
            n3=d
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
  elif b<=a and b<=c and b<=d and b<=e :
    n1=b
    if a<=c and a<=d and a<=e :
        n2=a
        if c<=d and c<=e :
            n3=c
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=c and d<=e :
            n3=d
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif e<=c and e<=d :
            n3=e
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
    elif c<=a and c<=d and c<=e :
        n2=c
        if a<=d and a<=e :
            n3=a
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=a and d<=e :
            n3=d
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=d :
            n3=e
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
    elif d<=a and d<=c and d<=e :
        n2=d
        if a<=c and a<=e :
            n3=a
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=a and c<=e :
            n3=c
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=c :
            n3=e
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif e<=a and e<=c and e<=d :
        n2=e
        if a<=c and a<=d :
            n3=a
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=a and c<=d :
            n3=c
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=c :
            n3=d
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
  elif c<=a and c<=b and c<=d and c<=e :
    n1=c
    if a<=b and a<=d and a<=e :
        n2=a
        if b<=d and b<=e :
            n3=b
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=b and d<=e :
            n3=d
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=d :
            n3=e
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
    elif b<=a and b<=d and b<=e :
        n2=b
        if a<=d and a<=e :
            n3=a
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=a and d<=e :
            n3=d
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=d :
            n3=e
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
    elif d<=a and d<=b and d<=e :
        n2=d
        if a<=b and a<=e :
            n3=a
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif b<=a and b<=e :
            n3=b
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=b :
            n3=e
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif e<=a and e<=b and e<=d :
        n2=e
        if a<=b and a<=d :
            n3=a
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif b<=a and b<=d :
            n3=b
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=b :
            n3=d
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  elif d<=a and d<=b and d<=c and d<=e :
    n1=d
    if a<=b and a<=c and a<=e :
        n2=a
        if b<=c and b<=e :
            n3=b
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=b and c<=e :
            n3=c
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=c :
            n3=e
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif b<=a and b<=c and b<=e :
        n2=b
        if a<=c and a<=e :
            n3=a
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=a and c<=e :
            n3=c
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=c :
            n3=e
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif c<=a and c<=b and c<=e :
        n2=c
        if a<=b and a<=e :
            n3=a
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif b<=a and b<=e :
            n3=b
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=b :
            n3=e
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif e<=a and e<=b and e<=c :
        n2=e
        if a<=b and a<=c :
            n3=a
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
        elif b<=a and b<=c :
            n3=b
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
        elif c<=a and c<=b :
            n3=c
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  elif e<=a and e<=b and e<=c and e<=d :
    n1=e
    if a<=b and a<=c and a<=d :
        n2=a
        if b<=c and b<=d :
            n3=b
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=b and c<=d :
            n3=c
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif d<=b and d<=c :
            n3=d
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif b<=a and b<=c and b<=d :
        n2=b
        if a<=c and a<=d :
            n3=a
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=a and c<=d :
            n3=c
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=c :
            n3=d
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif c<=a and c<=b and c<=d :
        n2=c
        if a<=b and a<=d :
            n3=a
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif b<=a and b<=d :
            n3=b
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=b :
            n3=d
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif d<=a and d<=b and d<=c :
        n2=d
        if a<=b and a<=c :
            n3=a
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
        elif b<=a and b<=c :
            n3=b
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
        elif c<=a and c<=b :
            n3=c
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  return n3
def promedio_multiplicativo (a:float,b:float,c:float,d:float,e:float)->float:
    return(a*b*c*d*e)**0.5
def orden_ascendente (a:float,b:float,c:float,d:float,e:float)->float:
  if a<=b and a<=c and a<=d and a<=e :
    n1=a
    if b<=c and b<=d and b<=e :
        n2=b
        if c<=d and c<=e :
            n3=c
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=c and d<=e :
            n3=d
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif e<=c and e<=d :
            n3=e
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
    elif c<=b and c<=d and c<=e :
        n2=c
        if b<=d and b<=e :
            n3=b
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=b and d<=e :
            n3=d
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=d :
            n3=e
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
    elif d<=b and d<=c and d<=e :
        n2=d
        if b<=c and b<=e :
            n3=b
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=b and c<=e :
            n3=c
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=c :
            n3=e
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif e<=b and e<=c and e<=d :
        n2=e
        if b<=c and b<=d :
            n3=b
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=b and c<=d :
            n3=c
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif d<=b and d<=c :
            n3=d
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
  elif b<=a and b<=c and b<=d and b<=e :
    n1=b
    if a<=c and a<=d and a<=e :
        n2=a
        if c<=d and c<=e :
            n3=c
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=c and d<=e :
            n3=d
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif e<=c and e<=d :
            n3=e
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
    elif c<=a and c<=d and c<=e :
        n2=c
        if a<=d and a<=e :
            n3=a
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=a and d<=e :
            n3=d
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=d :
            n3=e
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
    elif d<=a and d<=c and d<=e :
        n2=d
        if a<=c and a<=e :
            n3=a
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=a and c<=e :
            n3=c
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=c :
            n3=e
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif e<=a and e<=c and e<=d :
        n2=e
        if a<=c and a<=d :
            n3=a
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=a and c<=d :
            n3=c
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=c :
            n3=d
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
  elif c<=a and c<=b and c<=d and c<=e :
    n1=c
    if a<=b and a<=d and a<=e :
        n2=a
        if b<=d and b<=e :
            n3=b
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=b and d<=e :
            n3=d
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=d :
            n3=e
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
    elif b<=a and b<=d and b<=e :
        n2=b
        if a<=d and a<=e :
            n3=a
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=a and d<=e :
            n3=d
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=d :
            n3=e
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
    elif d<=a and d<=b and d<=e :
        n2=d
        if a<=b and a<=e :
            n3=a
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif b<=a and b<=e :
            n3=b
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=b :
            n3=e
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif e<=a and e<=b and e<=d :
        n2=e
        if a<=b and a<=d :
            n3=a
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif b<=a and b<=d :
            n3=b
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=b :
            n3=d
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  elif d<=a and d<=b and d<=c and d<=e :
    n1=d
    if a<=b and a<=c and a<=e :
        n2=a
        if b<=c and b<=e :
            n3=b
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=b and c<=e :
            n3=c
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=c :
            n3=e
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif b<=a and b<=c and b<=e :
        n2=b
        if a<=c and a<=e :
            n3=a
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=a and c<=e :
            n3=c
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=c :
            n3=e
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif c<=a and c<=b and c<=e :
        n2=c
        if a<=b and a<=e :
            n3=a
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif b<=a and b<=e :
            n3=b
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=b :
            n3=e
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif e<=a and e<=b and e<=c :
        n2=e
        if a<=b and a<=c :
            n3=a
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
        elif b<=a and b<=c :
            n3=b
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
        elif c<=a and c<=b :
            n3=c
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  elif e<=a and e<=b and e<=c and e<=d :
    n1=e
    if a<=b and a<=c and a<=d :
        n2=a
        if b<=c and b<=d :
            n3=b
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=b and c<=d :
            n3=c
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif d<=b and d<=c :
            n3=d
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif b<=a and b<=c and b<=d :
        n2=b
        if a<=c and a<=d :
            n3=a
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=a and c<=d :
            n3=c
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=c :
            n3=d
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif c<=a and c<=b and c<=d :
        n2=c
        if a<=b and a<=d :
            n3=a
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif b<=a and b<=d :
            n3=b
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=b :
            n3=d
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif d<=a and d<=b and d<=c :
        n2=d
        if a<=b and a<=c :
            n3=a
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
        elif b<=a and b<=c :
            n3=b
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
        elif c<=a and c<=b :
            n3=c
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  return n1, n2, n3, n4, n5
def orden_descendente (a:float,b:float,c:float,d:float,e:float)->float:
  if a<=b and a<=c and a<=d and a<=e :
    n1=a
    if b<=c and b<=d and b<=e :
        n2=b
        if c<=d and c<=e :
            n3=c
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=c and d<=e :
            n3=d
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif e<=c and e<=d :
            n3=e
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
    elif c<=b and c<=d and c<=e :
        n2=c
        if b<=d and b<=e :
            n3=b
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=b and d<=e :
            n3=d
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=d :
            n3=e
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
    elif d<=b and d<=c and d<=e :
        n2=d
        if b<=c and b<=e :
            n3=b
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=b and c<=e :
            n3=c
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=c :
            n3=e
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif e<=b and e<=c and e<=d :
        n2=e
        if b<=c and b<=d :
            n3=b
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=b and c<=d :
            n3=c
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif d<=b and d<=c :
            n3=d
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
  elif b<=a and b<=c and b<=d and b<=e :
    n1=b
    if a<=c and a<=d and a<=e :
        n2=a
        if c<=d and c<=e :
            n3=c
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=c and d<=e :
            n3=d
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif e<=c and e<=d :
            n3=e
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
    elif c<=a and c<=d and c<=e :
        n2=c
        if a<=d and a<=e :
            n3=a
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=a and d<=e :
            n3=d
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=d :
            n3=e
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
    elif d<=a and d<=c and d<=e :
        n2=d
        if a<=c and a<=e :
            n3=a
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=a and c<=e :
            n3=c
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=c :
            n3=e
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif e<=a and e<=c and e<=d :
        n2=e
        if a<=c and a<=d :
            n3=a
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=a and c<=d :
            n3=c
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=c :
            n3=d
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
  elif c<=a and c<=b and c<=d and c<=e :
    n1=c
    if a<=b and a<=d and a<=e :
        n2=a
        if b<=d and b<=e :
            n3=b
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=b and d<=e :
            n3=d
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=d :
            n3=e
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
    elif b<=a and b<=d and b<=e :
        n2=b
        if a<=d and a<=e :
            n3=a
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=a and d<=e :
            n3=d
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=d :
            n3=e
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
    elif d<=a and d<=b and d<=e :
        n2=d
        if a<=b and a<=e :
            n3=a
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif b<=a and b<=e :
            n3=b
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=b :
            n3=e
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif e<=a and e<=b and e<=d :
        n2=e
        if a<=b and a<=d :
            n3=a
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif b<=a and b<=d :
            n3=b
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=b :
            n3=d
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  elif d<=a and d<=b and d<=c and d<=e :
    n1=d
    if a<=b and a<=c and a<=e :
        n2=a
        if b<=c and b<=e :
            n3=b
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=b and c<=e :
            n3=c
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=c :
            n3=e
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif b<=a and b<=c and b<=e :
        n2=b
        if a<=c and a<=e :
            n3=a
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=a and c<=e :
            n3=c
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=c :
            n3=e
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif c<=a and c<=b and c<=e :
        n2=c
        if a<=b and a<=e :
            n3=a
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif b<=a and b<=e :
            n3=b
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=b :
            n3=e
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif e<=a and e<=b and e<=c :
        n2=e
        if a<=b and a<=c :
            n3=a
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
        elif b<=a and b<=c :
            n3=b
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
        elif c<=a and c<=b :
            n3=c
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  elif e<=a and e<=b and e<=c and e<=d :
    n1=e
    if a<=b and a<=c and a<=d :
        n2=a
        if b<=c and b<=d :
            n3=b
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=b and c<=d :
            n3=c
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif d<=b and d<=c :
            n3=d
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif b<=a and b<=c and b<=d :
        n2=b
        if a<=c and a<=d :
            n3=a
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=a and c<=d :
            n3=c
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=c :
            n3=d
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif c<=a and c<=b and c<=d :
        n2=c
        if a<=b and a<=d :
            n3=a
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif b<=a and b<=d :
            n3=b
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=b :
            n3=d
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif d<=a and d<=b and d<=c :
        n2=d
        if a<=b and a<=c :
            n3=a
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
        elif b<=a and b<=c :
            n3=b
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
        elif c<=a and c<=b :
            n3=c
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  return n5, n4, n3, n2, n1
def mayor_elevado_menor (a:float,b:float,c:float,d:float,e:float)->float:
  if a<=b and a<=c and a<=d and a<=e :
    n1=a
    if b<=c and b<=d and b<=e :
        n2=b
        if c<=d and c<=e :
            n3=c
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=c and d<=e :
            n3=d
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif e<=c and e<=d :
            n3=e
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
    elif c<=b and c<=d and c<=e :
        n2=c
        if b<=d and b<=e :
            n3=b
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=b and d<=e :
            n3=d
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=d :
            n3=e
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
    elif d<=b and d<=c and d<=e :
        n2=d
        if b<=c and b<=e :
            n3=b
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=b and c<=e :
            n3=c
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=c :
            n3=e
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif e<=b and e<=c and e<=d :
        n2=e
        if b<=c and b<=d :
            n3=b
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=b and c<=d :
            n3=c
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif d<=b and d<=c :
            n3=d
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
  elif b<=a and b<=c and b<=d and b<=e :
    n1=b
    if a<=c and a<=d and a<=e :
        n2=a
        if c<=d and c<=e :
            n3=c
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=c and d<=e :
            n3=d
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif e<=c and e<=d :
            n3=e
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
    elif c<=a and c<=d and c<=e :
        n2=c
        if a<=d and a<=e :
            n3=a
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=a and d<=e :
            n3=d
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=d :
            n3=e
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
    elif d<=a and d<=c and d<=e :
        n2=d
        if a<=c and a<=e :
            n3=a
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=a and c<=e :
            n3=c
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=c :
            n3=e
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif e<=a and e<=c and e<=d :
        n2=e
        if a<=c and a<=d :
            n3=a
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=a and c<=d :
            n3=c
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=c :
            n3=d
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
  elif c<=a and c<=b and c<=d and c<=e :
    n1=c
    if a<=b and a<=d and a<=e :
        n2=a
        if b<=d and b<=e :
            n3=b
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=b and d<=e :
            n3=d
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=d :
            n3=e
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
    elif b<=a and b<=d and b<=e :
        n2=b
        if a<=d and a<=e :
            n3=a
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=a and d<=e :
            n3=d
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=d :
            n3=e
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
    elif d<=a and d<=b and d<=e :
        n2=d
        if a<=b and a<=e :
            n3=a
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif b<=a and b<=e :
            n3=b
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=b :
            n3=e
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif e<=a and e<=b and e<=d :
        n2=e
        if a<=b and a<=d :
            n3=a
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif b<=a and b<=d :
            n3=b
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=b :
            n3=d
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  elif d<=a and d<=b and d<=c and d<=e :
    n1=d
    if a<=b and a<=c and a<=e :
        n2=a
        if b<=c and b<=e :
            n3=b
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=b and c<=e :
            n3=c
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=c :
            n3=e
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif b<=a and b<=c and b<=e :
        n2=b
        if a<=c and a<=e :
            n3=a
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=a and c<=e :
            n3=c
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=c :
            n3=e
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif c<=a and c<=b and c<=e :
        n2=c
        if a<=b and a<=e :
            n3=a
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif b<=a and b<=e :
            n3=b
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=b :
            n3=e
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif e<=a and e<=b and e<=c :
        n2=e
        if a<=b and a<=c :
            n3=a
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
        elif b<=a and b<=c :
            n3=b
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
        elif c<=a and c<=b :
            n3=c
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  elif e<=a and e<=b and e<=c and e<=d :
    n1=e
    if a<=b and a<=c and a<=d :
        n2=a
        if b<=c and b<=d :
            n3=b
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=b and c<=d :
            n3=c
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif d<=b and d<=c :
            n3=d
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif b<=a and b<=c and b<=d :
        n2=b
        if a<=c and a<=d :
            n3=a
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=a and c<=d :
            n3=c
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=c :
            n3=d
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif c<=a and c<=b and c<=d :
        n2=c
        if a<=b and a<=d :
            n3=a
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif b<=a and b<=d :
            n3=b
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=b :
            n3=d
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif d<=a and d<=b and d<=c :
        n2=d
        if a<=b and a<=c :
            n3=a
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
        elif b<=a and b<=c :
            n3=b
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
        elif c<=a and c<=b :
            n3=c
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  return n5**n1
def raiz_menor (a:float,b:float,c:float,d:float,e:float)->float:
  if a<=b and a<=c and a<=d and a<=e :
    n1=a
    if b<=c and b<=d and b<=e :
        n2=b
        if c<=d and c<=e :
            n3=c
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=c and d<=e :
            n3=d
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif e<=c and e<=d :
            n3=e
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
    elif c<=b and c<=d and c<=e :
        n2=c
        if b<=d and b<=e :
            n3=b
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=b and d<=e :
            n3=d
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=d :
            n3=e
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
    elif d<=b and d<=c and d<=e :
        n2=d
        if b<=c and b<=e :
            n3=b
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=b and c<=e :
            n3=c
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=c :
            n3=e
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif e<=b and e<=c and e<=d :
        n2=e
        if b<=c and b<=d :
            n3=b
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=b and c<=d :
            n3=c
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif d<=b and d<=c :
            n3=d
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
  elif b<=a and b<=c and b<=d and b<=e :
    n1=b
    if a<=c and a<=d and a<=e :
        n2=a
        if c<=d and c<=e :
            n3=c
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=c and d<=e :
            n3=d
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif e<=c and e<=d :
            n3=e
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
    elif c<=a and c<=d and c<=e :
        n2=c
        if a<=d and a<=e :
            n3=a
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=a and d<=e :
            n3=d
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=d :
            n3=e
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
    elif d<=a and d<=c and d<=e :
        n2=d
        if a<=c and a<=e :
            n3=a
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=a and c<=e :
            n3=c
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=c :
            n3=e
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif e<=a and e<=c and e<=d :
        n2=e
        if a<=c and a<=d :
            n3=a
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=a and c<=d :
            n3=c
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=c :
            n3=d
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
  elif c<=a and c<=b and c<=d and c<=e :
    n1=c
    if a<=b and a<=d and a<=e :
        n2=a
        if b<=d and b<=e :
            n3=b
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=b and d<=e :
            n3=d
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=d :
            n3=e
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
    elif b<=a and b<=d and b<=e :
        n2=b
        if a<=d and a<=e :
            n3=a
            if d<=e :
                n4=d
                n5=e
            else:
                n4=e
                n5=d
        elif d<=a and d<=e :
            n3=d
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=d :
            n3=e
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
    elif d<=a and d<=b and d<=e :
        n2=d
        if a<=b and a<=e :
            n3=a
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif b<=a and b<=e :
            n3=b
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=b :
            n3=e
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif e<=a and e<=b and e<=d :
        n2=e
        if a<=b and a<=d :
            n3=a
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif b<=a and b<=d :
            n3=b
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=b :
            n3=d
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  elif d<=a and d<=b and d<=c and d<=e :
    n1=d
    if a<=b and a<=c and a<=e :
        n2=a
        if b<=c and b<=e :
            n3=b
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=b and c<=e :
            n3=c
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif e<=b and e<=c :
            n3=e
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif b<=a and b<=c and b<=e :
        n2=b
        if a<=c and a<=e :
            n3=a
            if c<=e :
                n4=c
                n5=e
            else:
                n4=e
                n5=c
        elif c<=a and c<=e :
            n3=c
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=c :
            n3=e
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif c<=a and c<=b and c<=e :
        n2=c
        if a<=b and a<=e :
            n3=a
            if b<=e :
                n4=b
                n5=e
            else:
                n4=e
                n5=b
        elif b<=a and b<=e :
            n3=b
            if a<=e :
                n4=a
                n5=e
            else:
                n4=e
                n5=a
        elif e<=a and e<=b :
            n3=e
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif e<=a and e<=b and e<=c :
        n2=e
        if a<=b and a<=c :
            n3=a
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
        elif b<=a and b<=c :
            n3=b
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
        elif c<=a and c<=b :
            n3=c
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  elif e<=a and e<=b and e<=c and e<=d :
    n1=e
    if a<=b and a<=c and a<=d :
        n2=a
        if b<=c and b<=d :
            n3=b
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=b and c<=d :
            n3=c
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif d<=b and d<=c :
            n3=d
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
    elif b<=a and b<=c and b<=d :
        n2=b
        if a<=c and a<=d :
            n3=a
            if c<=d :
                n4=c
                n5=d
            else:
                n4=d
                n5=c
        elif c<=a and c<=d :
            n3=c
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=c :
            n3=d
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
    elif c<=a and c<=b and c<=d :
        n2=c
        if a<=b and a<=d :
            n3=a
            if b<=d :
                n4=b
                n5=d
            else:
                n4=d
                n5=b
        elif b<=a and b<=d :
            n3=b
            if a<=d :
                n4=a
                n5=d
            else:
                n4=d
                n5=a
        elif d<=a and d<=b :
            n3=d
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
    elif d<=a and d<=b and d<=c :
        n2=d
        if a<=b and a<=c :
            n3=a
            if b<=c :
                n4=b
                n5=c
            else:
                n4=c
                n5=b
        elif b<=a and b<=c :
            n3=b
            if a<=c :
                n4=a
                n5=c
            else:
                n4=c
                n5=a
        elif c<=a and c<=b :
            n3=c
            if a<=b :
                n4=a
                n5=b
            else:
                n4=b
                n5=a
  return n1**(1/3)
if __name__ == "__main__":
    a=float(input("Escribe un numero: "))
    b=float(input("Escribe otro numero: "))
    c=float(input("Escribe otro numero: "))
    d=float(input("Escribe otro numero: "))
    e=float(input("Escribe un ultimo numero: "))
promedio_one=promedio(a,b,c,d,e)
mediana_one=mediana(a,b,c,d,e)
promedio_multiplicativo_one=promedio_multiplicativo(a,b,c,d,e)
orden_ascendente_one=orden_ascendente(a,b,c,d,e)
orden_descendente_one=orden_descendente(a,b,c,d,e)
mayor_elevado_menor_one=mayor_elevado_menor(a,b,c,d,e)
raiz_menor_one=raiz_menor(a,b,c,d,e)
print(f"El promedio de {a}, {b},{c}, {d} y {e} es {promedio_one}")
print(f"La mediana de {a}, {b},{c}, {d} y {e} es {mediana_one}")
print(f"El promedio multiplicativo de {a}, {b},{c}, {d} y {e} es {promedio_multiplicativo_one}")
print(f"Ordenados de forma ascendente {a}, {b},{c}, {d} y {e} serian {orden_ascendente_one}")
print(f"Ordenados de forma descendente {a}, {b},{c}, {d} y {e} serian {orden_descendente_one}")
print(f"El resultado de elevar el numero mayor al menor es {mayor_elevado_menor_one}")
print(f"El resultado de sacarle la raiz cubica al numero menor es {raiz_menor_one}")
