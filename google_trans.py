from tkinter import *
from tkinter import ttk
# from googletrans.client import Translator
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    try:

        trans = Translator()
        trans1 = trans.translate(text,src=src,dest=dest)
        return trans1.text
    except Exception as e:
        print(e)

def data():
    s = combo_source.get()
    d = combo_destn.get()
    msg = s_txt.get(1.0,END).strip()
    translated_txt = change(text=msg, src = s,dest = d)
    d_txt.delete(1.0, END)
    d_txt.insert(END,translated_txt)


root = Tk()
root.title("Translator")
root.geometry("600x600")
root.config(bg='RoyalBlue')

txt_label = Label(root,text='Translator',font=("Time New Roman",25,"bold","underline"),bg='RoyalBlue')
txt_label.place(x=150,y=40, height = 50, width= 300)

s_frame = Frame(root).pack(side=BOTTOM)

txt_label = Label(root,text='Source Text:',font=("Time New Roman",15,"bold"),fg='Black',bg='RoyalBlue')
txt_label.place(x=10,y=100, height = 20, width= 160)

s_txt = Text(s_frame,font=("Time New Roman",13),wrap=WORD)
s_txt.place(x=10,y=130,height=150,width=580)

list_text = list(LANGUAGES.values())

combo_source = ttk.Combobox(s_frame,value=list_text)
combo_source.place(x=10,y=290,height=40,width=170)
combo_source.set('English')

chng_button = Button(s_frame,text='Translate',relief=RAISED,command=data)
chng_button.place(x=200,y=290,height=40,width=170)

combo_destn = ttk.Combobox(s_frame,value=list_text)
combo_destn.place(x=390,y=290,height=40,width=170)
combo_destn.set('Hindi')



txt_labl = Label(root,text='Destination Text:',font=("Time New Roman",15,"bold"),fg='Black',bg='RoyalBlue')
txt_labl.place(x=12,y=350, height = 20, width= 180)

d_txt = Text(root,font=("Time New Roman",13),wrap=WORD)
d_txt.place(x=10,y=380,height=150,width=580)






root.mainloop()