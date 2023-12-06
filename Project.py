from datetime import datetime, timedelta
#the main menu
def menu():
    print('You may select one of the following:\n1) List available cars\n2) Rent a car\n3) Return a car\n4) Count the money\n0) Exit')
def av_cars():
    #here the file with all vehicles is read and then all components are splitted
    f = open('Vehicles.txt', 'r')
    print('The following cars are available:')
    while True:
        lines = f.readline()
        if len(lines) == 0:
            break
        #all information is splitted,so it can be used comfortably
        split = lines.split(',')
        reg_num = split[0]
        model = split[1]
        price = split[2]
        prop = split[3:]
        if len(lines) != 0:
            print('*Reg. nr:', reg_num, ',Model:', model, ',Price per day:', price, '\nProperties:',','.join(prop),end='')
            #for i in prop:
                #print(i,end=', ')
    print('\n')
    f.close()
def rent_car():
    #in this function where the car is rented
    #it gets the information of the customer if he is not in the system and considers age
    f = open('Vehicles.txt', 'r')
    f1=open('Customers.txt','a+')
    current_time = datetime.now()
    current_time2 = current_time.strftime('%d/%m/%Y')
    current_time3=datetime.strptime(current_time2,'%d/%m/%Y')
    print(current_time2)
    rent_car = input('Which car do you want to rent?\n')
    a=True
    while a:
            lines = f.readline()
            split = lines.split(',')
            reg_num = split[0]
            model = split[1]
            price = split[2]
            prop = split[3:]
            if rent_car in lines:
                #getting the date of birth and counting the age.And solving whether this person is allowed to ride a car or not
                birthday = input('input your birthday DD/MM/YYYY:')
                birthday_time=datetime.strptime(birthday,'%d/%m/%Y')
                age=abs((current_time3-birthday_time).days)
                age_years=age//365
                a = False
                if age_years>100 or age_years<18:
                    print('You are not allowed to rent a car,due to your age.')
                else:
                    #if the age fits in the age restrictions,the system gets all information from the customer as name,email and etc.
                    if birthday_time not in f1:
                        first_name=input('Enter first name:\n')
                        last_name=input('Enter last name:\n')
                        email_address=input('Enter your email address:\n')
                        if ('@' in email_address) and ('.' in email_address):
                            birthday1=datetime.strftime(birthday_time,'%d/%m/%Y')
                            info=birthday1+','+first_name+','+last_name+','+email_address
                            f1.write('\n'+info)
                            print('Hello',first_name)
                            print('You rented the car',rent_car)
    f.close()
    f1.close()
def return_car():
    #in this function when the car is returned,but the deleting from the rented vehicles of the returned car was not done
    file = open('rentedVehicles.txt', 'r')
    file1=open('Vehicles.txt','r')
    all_rented_cars=[]
    all_cars=[]
    car_return = input('Input the register of the returned car:\n')
    current_time = datetime.now()
    for lines in file:
        lines1=lines.split(',')
        reg_num = lines1[0]
        birth = lines1[1]
        pickup_time = lines1[2]
        all=[]
        all.append(reg_num)
        all.append(birth)
        all.append(pickup_time)
        all_rented_cars.append(all)
    for car in all_rented_cars:
        #here the time of using is counted
        if car_return==car[0]:
            using_time=datetime.strptime(car[2].strip(),'%d/%m/%y %H:%M')
            time_using=current_time-using_time
            time_using_days=time_using.days
            break
    for lines in file1:
        #here the price is found
        split = lines.split(',')
        reg_num1 = split[0]
        car = split[1]
        price1 = split[2]
        prop1 = split[3:]
        if reg_num1==split[0]:
            return price1
    else:
        print('This car does not exist or is not rented')
        #if the printed register number of car does not exist
    file.close()
    file1.close()
def count():
    #in this function the total amount of money from the transactions is counted
    file=open('transActions.txt','r')
    transactions=[]
    number=0
    for lines in file:
        lines=lines[0:-2]
        lines1=lines.split(',')
        reg_num=lines1[0]
        birthday=lines[1]
        rent_start=lines1[2]
        rent_over=lines1[3]
        days=lines1[4]
        total_amount=lines1[5]
        number=number+float(total_amount)
        if len(lines)!=0:
                total_amount+=total_amount
                print('The total amount of money is', number, 'euros')
    file.close()
#here the choose is done and then it is goint to the particular function
while True:
    menu()
    try:
        menu1 = int(input('What is your selection?\n'))
        if menu1==1:
            av_cars()
        elif menu1==2:
            rent_car()
        elif menu1==3:
            return_car()
        elif menu1==4:
            count()
        if menu1==0:
            print('The program is closing.Bye!')
            break
    except ValueError:
        #if the user's input is not an integer
        print('Unknown selection.Please,try again')