
def employee_data(name, **details):
    print('Name:',name)
    for k,v in details.items():
        print(f"{k}: {v}")


employee_data('Ali',address='121/232,hazrat',phone=3929292)
employee_data('Alan',phone=29392992,country='Srilanka',job='accounts')
employee_data('Rakesh')
employee_data('Sara',a='23',b=2,c=23,d=21,e=232)