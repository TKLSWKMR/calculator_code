#code for Calculator in python

import tkinter as cal
 

calculation =" "

def add_to_calculation(symbol):

   global calculation

   calculation += str(symbol)

   text_result.delete(1.0,"end")

   text_result.insert(1.0,calculation)

 

def evaluate_calculation():

    global calculation

    try:

        calculation= str(eval(calculation))

        text_result.delete(1.0,"end")

        text_result.insert(1.0,calculation)

    except:

        clear_field()

        text_result.insert(1.0,"error")

 

def clear_field():

    global calculation

    calculation=""

    text_result.delete(1.0,"end")


        

 

root = cal.Tk()

root.title("calculator")

root.geometry("300x275")

text_result=cal.Text(root, height=2,width=18,font=("arial",24))

text_result.grid(columnspan=5)

 

btn_clear=cal.Button(root,text="C",command=clear_field,width=5, font=("arial",14))

btn_clear.grid(row=2,column=1)



btn_div=cal.Button(root,text="/",command=lambda: add_to_calculation("/"),width=5, font=("arial",14))

btn_div.grid(row=2,column=2)

btn_mul=cal.Button(root,text="*",command=lambda: add_to_calculation("*"),width=5, font=("arial",14))

btn_mul.grid(row=2,column=3)

btn_sub=cal.Button(root,text="-",command=lambda: add_to_calculation("-"),width=5, font=("arial",14))

btn_sub.grid(row=2,column=4)

btn_7=cal.Button(root,text="7",command=lambda: add_to_calculation("7"),width=5, font=("arial",14))

btn_7.grid(row=3,column=1)

btn_8=cal.Button(root,text="8",command=lambda: add_to_calculation("8"),width=5, font=("arial",14))

btn_8.grid(row=3,column=2)

btn_9=cal.Button(root,text="9",command=lambda: add_to_calculation("9"),width=5, font=("arial",14))

btn_9.grid(row=3,column=3)

btn_4=cal.Button(root,text="4",command=lambda: add_to_calculation("4"),width=5, font=("arial",14))

btn_4.grid(row=4,column=1)

btn_5=cal.Button(root,text="5",command=lambda: add_to_calculation("5"),width=5, font=("arial",14))

btn_5.grid(row=4,column=2)

btn_6=cal.Button(root,text="6",command=lambda: add_to_calculation("6"),width=5, font=("arial",14))

btn_6.grid(row=4,column=3)

btn_1=cal.Button(root,text="1",command=lambda: add_to_calculation("1"),width=5, font=("arial",14))

btn_1.grid(row=5,column=1)

btn_2=cal.Button(root,text="2",command=lambda: add_to_calculation("2"),width=5, font=("arial",14))

btn_2.grid(row=5,column=2)

btn_3=cal.Button(root,text="3",command=lambda: add_to_calculation("3"),width=5, font=("arial",14))

btn_3.grid(row=5,column=3)

btn_0=cal.Button(root,text="0",command=lambda: add_to_calculation("0"),width=12, font=("arial",14))

btn_0.grid(row=6,column=1,columnspan=2)

btn_point=cal.Button(root,text=".",command=lambda: add_to_calculation("."),width=5, font=("arial",14))

btn_point.grid(row=6,column=3)

btn_mod=cal.Button(root,text="%",command=lambda: add_to_calculation("%"),width=5, font=("arial",14))

btn_mod.grid(row=4,column=4)

btn_plus=cal.Button(root,text="+",command=lambda: add_to_calculation("+"),width=5, font=("arial",14))

btn_plus.grid(row=3,column=4)

btn_equal=cal.Button(root,text="=",command=evaluate_calculation,width=5,height=3,font=("arial",14))

btn_equal.grid(row=5,column=4,rowspan=2)

root.mainloop()
#code written by  Sandhya Rani.C