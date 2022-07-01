from main import Departamentos, Empleados, Notas, Likes,Comentarios, create_connection, execute_query, execute_read_query

def menu_Consola():
      while True:
        print("BIENVENIDO A HELLBOT")
        print("Empresa N 1° en la fabricacion y exportacion de medias con cordones")
        print("INGRESE SU IDE ")
        e1=Empleados()
        e1.mostrar()
        if e1.veriEmp==0:
            print("Notas del departamento")
            e1.Notas_VisiblesEmpleado()
            print("1-Comentar")
            print("2-LIKEAR")
            print("3-AGREGAR NOTA")
            print("4-SALIR")
            op=int(input())
            if op==1:
                print("INGRESE NUMERO DE NOTA Y CONTENIDO")
                e1.ComentarNota()
            elif op==2:
                print("INGRESAR NUMERO DE NOTA")
                e1.Likear()
                continue
            elif op==3:
                print("INGRESAR ID DE NOTA")
                e1.EsbribirNota()
                continue
            elif op==4:
                print("MUCHAS GRACIAS!")
                break
        else:
            sal = int(input("Desea registrarse a la empresa? 1-Si, 2-Volver al Menu"))
            if sal == 1 :

                e1.agregar()
                continue
            else:
                continue






#d1=Departamentos()
#d1.mostrar()


#e1.Notas_VisiblesEmpleado()
#e1.ComentarNota()
#n1= Notas()
#n1.mostrar()
#menu_Consola()
#l1=Likes()
#l1.mostrar()
#menu_Consola()
#c1=Comentarios()
#c1.agregar()
#c1.mostrar()


#d1=Departamentos()
#d1.mostrar()

#e1=Empleados()
#e1.mostrar()
#e1.Notas_VisiblesEmpleado()
#e1.ComentarNota()
#n1= Notas()
#n1.mostrar()
#menu_Consola()
#l1=Likes()
#l1.mostrar()
menu_Consola()
#c1=Comentarios()
#c1.agregar()
#c1.mostrar()
