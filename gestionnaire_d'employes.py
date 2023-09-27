
from tkinter import*
import sqlite3


window= Tk()
window.title("GESTIONNAiRE D'EMPLOYES")


frame_add_employes = Frame(window)
frame_add_employes.pack()


label_first_employe=Label(frame_add_employes,text="PRENOM :")
label_first_employe.grid(row=0,column=0)

entry_first_name=Entry(frame_add_employes)
entry_first_name.grid(row=0,column=1)

label_second_name=Label(frame_add_employes,text="NOM:")
label_second_name.grid(row=1,column=0)

entry_second_name=Entry(frame_add_employes)
entry_second_name.grid(row=1,column=1)

phone_number=Label(frame_add_employes,text="NUMERO TELEPHONE:")
phone_number.grid(row=2,column=0)

entry_phone_number=Entry(frame_add_employes)
entry_phone_number.grid(row=2,column=1)

address_personne=Label(frame_add_employes,text="ADDRESSE :")
address_personne.grid(row=3,column=0)

address_personne_entry=Entry(frame_add_employes)
address_personne_entry.grid(row=3,column=1)


def add_employee():

    first_name=entry_first_name.get()
    second_name=entry_second_name.get()
    phone= entry_phone_number.get()
    adress=address_personne_entry.get()
    conn=sqlite3.connect('EMPLOYES.db')
    c=conn.cursor()
    c.execute("INSERT INTO EMPLOYES(first_name,second_name,adress,phone) VALUES (?,?,?,?)",(first_name,second_name,adress,phone))
    conn.commit()
    conn.close()


    entry_first_name.delete(0,Tk.END) 
    entry_second_name.delete(0,Tk.END) 
    address_personne_entry.delete(0,Tk.END)
    entry_phone_number.delete(0,Tk.END)


button_add_employes=Button(frame_add_employes,text="AJOUTER",command=add_employee)
button_add_employes.grid(row=4,column=1)

window.mainloop()