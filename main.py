from tkinter import *
from tkinter import filedialog
import json

fileName = "C:"

def doNothing():
    print("Nada")

def openFile():
    f = filedialog.askopenfile(parent=root)
    print(f.name)

menus2 = {"MenuPrincipal":
    [
        {"Fichero":
            [
                "Abrir Fichero",
                {
                    "Submenu":
                        [
                            "SubmenuCommando1",
                            "SubmenuCommando2"
                        ]
                },
                "Cerrar Fichero"
                "Separador"
                "Exit"
            ]
         },
        {"Editar":
             [
                 "Copiar",
                 "Cortar",
                 "Pegar"
             ]
         },
        {
            "Ayuda":
                {
                    "Acerca de"
                }
         },
    ]}

menus = [
            {"Fichero":
                [
                    "Abrir Fichero",
                    {
                        "Submenu":
                            [
                                "SubmenuCommando1",
                                "SubmenuCommando2"
                            ]
                    },
                    "Cerrar Fichero"
                    "Separador"
                    "Exit"
                ]
             },
            {"Editar":
                 [
                     "Copiar",
                     "Cortar",
                     "Pegar"
                 ]
             },
            {
                "Ayuda":
                    {
                        "Acerca de"
                    }
             }
       ]


def estructura_diccionario (menus:dict):
    if menus != {}:
        for opcion in menus.keys():
            lista = menus[opcion]
            for elemento in lista:
                if isinstance(elemento,dict):
                    print(opcion,':')
                    estructura_diccionario(elemento)
                else:
                    print(elemento)


def generar_menus (ventana, menus:dict):
    lista = menus["MenuPrincipal"]
    menuPrincipal = Menu(ventana)
    generar_submenus(menuPrincipal, submenus)
    v.config(menu=menuPrincipal)

def generar_submenus (objetoPadre, menus:dict):
    if menus != {}:
        for opcion in menus.keys():
            lista = menus[opcion]
            for elemento in lista:
                if isinstance(elemento, dict):
                    # print(opcion,':')
                    newMenu = Menu(objetoPadre)
                    objetoPadre.add_cascade(label=opcion, menu=newMenu)
                    generar_submenus(newMenu, elemento)
                else:
                    objetoPadre.add_command(label=elemento)
                    #print(elemento)

v = Tk()
v.title("Generación automática")
menuBar = Menu(v)
v.config(menu=menuBar)
for submenu in menus:
    generar_submenus(menuBar, submenu)
print("OK")

v.mainloop()


# Window creation
ventana = Tk()
ventana.title("Mi Aplicación")      # Título de la Ventana
v.mainloop()


# Creates menu bar & config menu bar in window object
menuBar = Menu(ventana)  # Crea el objeto menú Principal en la ventana
ventana.config(menu=menuBar)    # Enlaza el objeto

# Creates File menu option & adds options for File menu option
fileMenu = Menu(menuBar)       # Crea un menú
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New Project...", command=openFile)

# creates sub menu "SubMenu" for File menu option "Submenu" & creates options for sub menu
subMenu = Menu(master=fileMenu)
fileMenu.add_cascade(label="Submenu", menu=subMenu)
subMenu.add_command(label="Opc Subm")

#Creates File menu additional options
fileMenu.add_command(label="New...", command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=doNothing)

# Creates Edit menu option
editMenu = Menu(menuBar)
menuBar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Copy", command=doNothing)

# Keeps window open
ventana.mainloop()
