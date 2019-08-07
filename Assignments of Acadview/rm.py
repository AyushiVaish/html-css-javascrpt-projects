from Tkinter import*
import time
import random

root=Tk()
root.geometry("1600x8000")
root.title("Resturant Management System")


#_________________________________________________________________FRAME______________________________________________________________________#

f1=Frame(root,width=1600,relief=SUNKEN)
f1.pack(side=TOP)

f2=Frame(root,height=7000,width=1600,relief=SUNKEN)
f2.pack(side=LEFT)

#______________________________________________________________TITLE_____________________________________________________________________#




localtime=time.asctime(time.localtime(time.time()))

lblInfo=Label(f1,font=("ALGERIAN",50,"bold"),fg="black",bd=16,text="RESTURANT MANAGEMENT SYSTEM",anchor="w")
lblInfo.grid(row=0,column=0)

lblInfo=Label(f1,font=("arial,20"),fg="blue",bd=10,text=localtime,anchor="w")
lblInfo.grid(row=1,column=0)


#_______________________________________________________________________________________________________________________________________________#

def Ref():
    x=random.randint(1,500)
    randomRef=str(x)
    rand.set(randomRef)

    if(Fries.get()==""):
        CoFries=0
    else:
         CoFries=float(Fries.get())
    


    if(Noodles.get()==""):
        CoNoodles=0
    else:
        CoNoodles=float(Noodles.get())

    if(Soup.get()==""):
        CoSoup=0
    else:
        CoSoup=float(Soup.get())


    if(Burger.get()==""):
        CoBurger=0
    else:
        CoBurger=float(Burger.get())

    if(Sandwich.get()==""):
        CoSandwich=0
    else:
        CoSandwich=float(Sandwich.get())

    if(Drinks.get()==""):
        CoDrinks=0
    else:
        CoDrinks=float(Drinks.get())

    CostofFries=CoFries*120
    CostofDrinks=CoDrinks*40
    CostofNoodles=CoNoodles*100
    CostofSoup=CoSoup*70
    CostofBurger=CoBurger*150
    CostofSandwich=CoSandwich*250

    CostofMeal="Rs",str('%.2f'%(CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostofBurger+CostofSandwich))
    PayTax=((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostofBurger+CostofSandwich)*0.05)
    TotalCost=(CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostofBurger+CostofSandwich)     
    Ser_Charge=((CostofFries+CostofDrinks+CostofNoodles+CostofSoup+CostofBurger+CostofSandwich)/99)
    Service="Rs",str('%.2f' % Ser_Charge)
    OverAllCost="Rs",str('%.2f' %(PayTax+TotalCost+Ser_Charge))

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PayTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)

#________________________________________________________________________________________________________________________________________________#
def qExit():
    root.destroy()

#_________________________________________________________________________________________________________________________________________________#

lb1Info1=Label(f2,font=("helvetica",20,"bold"),text="Cost of Fries=120",fg="Black",bd=10,anchor="w")
lb2Info2=Label(f2,font=("helvetica",20,"bold"),text="Cost of Drinks=40",fg="Black",bd=10,anchor="w")
lb3Info3=Label(f2,font=("helvetica",20,"bold"),text="Cost of Noodles=100",fg="Black",bd=10,anchor="w")
lb4Info4=Label(f2,font=("helvetica",20,"bold"),text="Cost of Soup=70",fg="Black",bd=10,anchor="w")
lb5Info5=Label(f2,font=("helvetica",20,"bold"),text="Cost of burger=150",fg="Black",bd=10,anchor="w")
lb6Info6=Label(f2,font=("helvetica",20,"bold"),text="Cost of Sandwich=250",fg="Black",bd=10,anchor="w")

def List():

    lb1Info1.grid(row=0,column=4)
    lb2Info2.grid(row=1,column=4)
    lb3Info3.grid(row=2,column=4)
    lb4Info4.grid(row=3,column=4)
    lb5Info5.grid(row=4,column=4)
    lb6Info6.grid(row=5,column=4)
#______________________________________________________________________________________________________________________________________________________________________________#

def Dlt():
    #print("hide called")
    lb1Info1.grid_forget()
    lb2Info2.grid_forget()
    lb3Info3.grid_forget()
    lb4Info4.grid_forget()
    lb5Info5.grid_forget()
    lb6Info6.grid_forget()

    #print("Hide Completed...")

#______________________________________________________________________________________________________________________________________________________________________#
def Reset():
    rand.set("")
    Fries.set("")
    Noodles.set("")
    Soup.set("")
    SubTotal("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Sandwich.set("")

rand=StringVar()
Fries=StringVar()
Noodles=StringVar()
Soup=StringVar()
SubTotal=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Burger=StringVar()
Sandwich=StringVar()
                    



#__________________________________________________________________MENU_________________________________________________________________________#




l_reference=Label(f2, font=("arial,15,bold"),text="Reference",bd=16,anchor="w").grid(row=0,column=0)
e_reference=Entry(f2,font=("arial,15,bold"),bd=10,insertwidth=4,bg="powder blue",textvariable=rand,justify="right").grid(row=0,column=1)
l_drink=Label(f2, font=("arial,15,bold"),text="Drinks",bd=16,anchor="w").grid(row=0,column=2)
e_drink=Entry(f2,font=("arial,15"),bd=10,insertwidth=4,textvariable=Drinks,bg="powder blue",justify="right").grid(row=0,column=3)

l_fries=Label(f2, font=("arial,15,bold"),text="Fries",bd=16,anchor="w").grid(row=1,column=0)
e_fries=Entry(f2,font=("arial,15,bold"),bd=10,insertwidth=4,bg="powder blue",textvariable=Fries,justify="right").grid(row=1,column=1)
l_cost=Label(f2,font=("arial,15,bold"),text="Cost",bd=16,anchor="w").grid(row=1,column=2)
e_cost=Entry(f2,font=("arial,15"),bd=10,insertwidth=4,textvariable=Cost,bg="powder blue",justify="right").grid(row=1,column=3)

l_noodles=Label(f2, font=("arial,15,bold"),text="Noodles",bd=16,anchor="w").grid(row=2,column=0)
e_noodles=Entry(f2,font=("arial,15,bold"),bd=10,insertwidth=4,bg="powder blue",textvariable=Noodles,justify="right").grid(row=2,column=1)
l_service_charge=Label(f2,font=("arial,15,bold"),text="Service_Charge",bd=16,anchor="w").grid(row=2,column=2)
e_service_charge=Entry(f2,font=("arial,15"),bd=10,insertwidth=4,textvariable=Service_Charge,bg="powder blue",justify="right").grid(row=2,column=3)

l_soup=Label(f2, font=("arial,15,bold"),text="Soup",bd=16,anchor="w").grid(row=3,column=0)
e_soup=Entry(f2,font=("arial,15,bold"),bd=10,insertwidth=4,bg="powder blue",textvariable=Soup,justify="right").grid(row=3,column=1)
l_tax=Label(f2,font=("arial,15,bold"),text="Tax",bd=16,anchor="w").grid(row=3,column=2)
e_tax=Entry(f2,font=("arial,15"),bd=10,insertwidth=4,textvariable=Tax,bg="powder blue",justify="right").grid(row=3,column=3)

l_burger=Label(f2, font=("arial,15,bold"),text="Burger",bd=16,anchor="w").grid(row=4,column=0)
e_burger=Entry(f2,font=("arial,15,bold"),bd=10,insertwidth=4,bg="powder blue",textvariable=Burger,justify="right").grid(row=4,column=1)
l_subtotal=Label(f2,font=("arial,15,bold"),text="SubTotal",bd=16,anchor="w").grid(row=4,column=2)
e_subtotal=Entry(f2,font=("arial,15"),bd=10,insertwidth=4,textvariable=SubTotal,bg="powder blue",justify="right").grid(row=4,column=3)

l_sandwich=Label(f2, font=("arial,15,bold"),text="Sandwich",bd=16,anchor="w").grid(row=5,column=0)
e_sandwich=Entry(f2,font=("arial,15,bold"),bd=10,insertwidth=4,bg="powder blue",textvariable=Sandwich,justify="right").grid(row=5,column=1)
l_total=Label(f2,font=("arial,15,bold"),text="Total",bd=16,anchor="w").grid(row=5,column=2)
e_total=Entry(f2,font=("arial,15"),bd=10,insertwidth=4,textvariable=Total,bg="powder blue",justify="right").grid(row=5,column=3)

#_____________________________________________________________________BUTTON________________________________________________________________________#

btotal=Button(f2,padx=16,pady=8,bd=16,fg="black",font=("arial",10,"bold"),width=10,text="Total",bg="Blue",command=Ref).grid(row=6,column=0)
bReset=Button(f2,padx=10,pady=8,bd=16,fg="black",font=("arial",10,"bold"),width=10,text="Reset",bg="Red",command=Reset).grid(row=6,column=1)
bExit=Button(f2,padx=10,pady=8,bd=16,fg="black",font=("arial",10,"bold"),width=10,text="Exit",bg="Cyan",command=qExit).grid(row=6,column=2)
bPriceList=Button(f2,padx=10,pady=8,bd=16,fg="black",font=("arial",10,"bold"),width=10,text="Price List",bg="violet",command=List).grid(row=6,column=3)
bDlt=Button(f2,padx=16,pady=8,bd=16,fg="black",font=("arial",10,"bold"),width=10,text="Delete",bg="Orange",command=Dlt).grid(row=6,column=4)

root.mainloop()
