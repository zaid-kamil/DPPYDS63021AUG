def si(principal, rate=7.75, time=1):
    return (principal * rate * time) / 100


o = si(12000,3.5,3)
o = si(50000)
o = si(50000, 10.0)
o = si(50000, 5.0, 5)
o = si(50000, rate = 10.0)
o = si(50000, rate = 5.0, time = 3)
o = si(principal = 50000, rate = 5.0, time = 3)
o = si(principal = 50000, time = 2)


