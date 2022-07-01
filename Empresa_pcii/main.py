from mysql.connector import Error, connect, OperationalError


def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database='Empresa')

        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")

    except OperationalError as e:
        print(f"The error '{e}' occurred")
    cursor.reset()


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
    cursor.reset()


connection = create_connection("localhost", "root", "")


class Departamentos:

    def __init__(self):
        self.id_d = int(input("Id: "))

    def __init__(self,id):
        self.id_d=id



    def Notas_Departamentos(self):
        select_users = "SELECT n.id_n, n.contenido FROM Departamentos d,Notas n Where d.id_d=n.id_d and d.id_d={id_d:n}".format(id_d=self.id_d)
        users = execute_read_query(connection, select_users)
        for user in users:
            print(user)

    def mostrar(self):
        select_users = "SELECT * FROM Departamentos d Where d.id_d={id_d:n}".format(id_d=self.id_d)
        users = execute_read_query(connection, select_users)
        for user in users:
            print(user)

    def agregar(self):
        self.nombre_d= str(input("Nombre: "))
        pregunta = """ select * from Departamentos d where d.id_d = {id_d:n};""".format(id_d=self.id_d)
        if execute_read_query(connection, pregunta) == []:
            execute_query(connection,
                          ("""INSERT INTO Departamentos VALUES ('{}','{}');""".format(self.id_d, self.nombre_d)))

        else:
            print("Departamento ya ingresado")

    def quitar(self):
        pregunta = """ select * from Departamentos d where d.id_d = {id_d:n};""".format(id_d=self.id_d)
        if execute_read_query(connection, pregunta) is not None:
            execute_query(connection,
                          (""" DELETE FROM departamentos  WHERE id_d = {id_d:n};""".format(id_d=self.id_d)))

        else:
            print("Departamento no existente")

class Empleados:

    def __init__(self):
        self.id_e = int(input("Ide: "))
        self.veriEmp=0
        self.nombre_d = "nombre"
        pregunta = """ select e.id_d from Empleados e where e.id_e = {id_e:n};""".format(id_e=self.id_e)
        IDD = execute_read_query(connection,pregunta)
        if IDD == []:
            self.id_d=0
        else:
            ID_DEP = IDD[0]
            self.id_d = ID_DEP[0]

    def Notas_VisiblesEmpleado(self):
        id_D=self.id_d
        d1=Departamentos(id_D)
        d1.Notas_Departamentos()

    def ComentarNota(self):
        cantidad = execute_read_query(connection, "Select count(n.id_n) from Notas n Where n.id_d={id_d:n} ".format(id_d=self.id_d))
        cant = cantidad[0]
        if cant[0]>0 :

          IDE=self.id_e
          C1 = Comentarios(IDE)
          C1.agregar()
        else:
            print("NO EXISTEN NOTAS,SE EL PRIMERO :)")

    def EsbribirNota(self):
        IDE = self.id_e
        IDD = self.id_d
        N1= Notas(IDE,IDD)
        N1.agregar()

    def Likear(self):
        IDE=self.id_e
        L1=Likes(IDE)
        L1.agregar()

    def mostrar(self):
        select_users = "SELECT e.nombre_e,d.nombre_d FROM Empleados e,Departamentos d Where e.id_e={id_e:n} and e.id_d=d.id_d and e.id_d={id_d:n}".format(id_e=self.id_e,id_d=self.id_d)
        users = execute_read_query(connection, select_users)

        if users == []:
            print("EL EMPLEADO NO TRABAJA EN LA EMPRESA")
            self.veriEmp = 1
        else:
             print(users)

    def getVeriEmp(self):
        return self.veriEmp

    def agregar(self):
        self.nombre_d = str(input("Nombre: "))

        for user in execute_read_query(connection,"Select d.id_d,d.nombre_d from Departamentos d"):
             print(user)

        self.id_d=int(input("INGRESAR IDD DONDE TRABAJA : "))
        cantidad = execute_read_query(connection, "Select count(e.id_e) from Empleados e")
        cant=cantidad[0]
        self.id_e = cant[0]+1
        print("SU ID ES : ", self.id_e)
        pregunta = """ select * from Empleados e where e.id_e = {id_e:n};""".format(id_e=self.id_e)
        if execute_read_query(connection, pregunta) == []:
            execute_query(connection,
                          ("""INSERT INTO Empleados VALUES ('{}','{}','{}');""".format(self.id_e, self.nombre_d, self.id_d)))

        else:
            print("Empleado ya ingresado")

    def quitar(self):
        pregunta = """ select * from Empleados e where e.id_e = {id_e:n};""".format(id_e=self.id_e)
        if execute_read_query(connection, pregunta) is not None:
            execute_query(connection,
                          (""" DELETE FROM empleados WHERE id_e = {id_e:n};""".format(id_e=self.id_e)))

        else:
            print("Empleado no existente")

class Notas:

    def __init__(self,IDE,IDD):
        self.tipo_n = int(input("Tipo: "))
        self.id_e = IDE
        self.id_d = IDD
        self.fecha = str(input("Fecha: "))
        self.contenido = str(input("Contenido: "))
        #cantidad = "Select count(n.id_n) from Notas n"
        cantidad=execute_read_query(connection,"Select count(n.id_n) from Notas n")
        cant = cantidad[0]
       # for cant in execute_read_query(connection, cantidad):
        #    i = i + 1

        self.id_n = cant[0] + 1

    def mostrar(self):
        select_users = "SELECT n.contenido,n.id_n FROM Departamentos d,Notas n Where d.id_d=n.id_d and n.id_d={id_d:n}".format(id_d=self.id_d)
        users = execute_read_query(connection, select_users)
        for user in users:
            print(user)

    def agregar(self):
        pregunta = """ select * from Notas n where n.id_n = {id_n:n};""".format(id_n=self.id_n)
        if execute_read_query(connection, pregunta) == []:
            execute_query(connection,
                          ("""INSERT INTO Notas VALUES ('{}','{}','{}','{}','{}','{}');""".format(self.id_n, self.tipo_n, self.id_e, self.id_d, self.fecha, self.contenido)))

        else:
            print("Nota ya ingresada")

    def quitar(self):
        pregunta = """ select * from Notas n where n.id_n = {id_n:n};""".format(id_n=self.id_n)
        if execute_read_query(connection, pregunta) is not None:
            execute_query(connection,
                          (""" DELETE FROM Notas WHERE id_n = {id_n:n};""".format(id_n=self.id_n)))

        else:
            print("Nota no existente")

class Comentarios:

    def __init__(self,IDE):

        self.id_n = int(input("Idn: "))
        self.id_e = IDE
        self.contenido = str(input("Contenido: "))

    def mostrar(self):
        select_users = "SELECT n.contenido,c.contenido,e.nombre_e FROM Notas n, Empleados e,Comentarios c Where n.id_n=c.id_n and e.id_e=c.id_e and c.id_e={id_e:n} and c.id_n= {id_n:n}".format(id_n=self.id_n,id_e=self.id_e)
        users = execute_read_query(connection, select_users)
        for user in users:
            print(user)

    def agregar(self):
        try:
            execute_query(connection,("""INSERT INTO Comentarios VALUES ('{}','{}','{}');""".format(self.id_n, self.id_e, self.contenido)))
        except Error as e:
            print(e)

    def quitar(self):
        pregunta = """ select * from Comentarios c where c.id_e = {id_e:n};""".format(id_e=self.id_e)
        if execute_read_query(connection, pregunta) is not None:
            execute_query(connection,
                          (""" DELETE FROM Comentarios WHERE id_e = {id_e:n} and id_n = {id_n:n};""".format(id_e=self.id_e,id_n=self.id_n)))

        else:
            print("Nota no existente")

class Likes:

    def __init__(self,IDE):
        self.id_e = IDE
        self.id_n = int(input("Idn: "))
        cantidad=execute_read_query(connection,"Select count(l.id_l) from Likes l")
        cant=cantidad[0]
        #for cant in execute_read_query(connection,cantidad):
        #   i=i+1

        self.id_l = cant[0]+1



    def mostrar(self):
        select_users = "SELECT n.contenido,e.id_e,e.nombre_e FROM Notas n,Empleados e,Likes l Where l.id_l={id_l:n}".format(id_l=self.id_l)
        users = execute_read_query(connection, select_users)
        for user in users:
            print(user)

    def agregar(self):
        pregunta = """ select * from Likes l where l.id_e = {id_e:n} and l.id_n = {id_n:n};""".format(id_e=self.id_e, id_n=self.id_n)
        if execute_read_query(connection, pregunta) ==[]:
            execute_query(connection,
                          ("""INSERT INTO Likes VALUES ('{}','{}','{}');""".format(self.id_e, self.id_n, self.id_l)))

        else:
            print("Ya ha sido likeado por ese empleado")

    def quitar(self):
        pregunta = """ select * from Likes l where l.id_l = {id_l:n};""".format(id_l=self.id_l)
        if execute_read_query(connection, pregunta) is not None:
            execute_query(connection,
                          (""" DELETE FROM Likes WHERE id_l = {id_l:n};""".format(id_l=self.id_l)))

        else:
            print("Like no existente")


#d1 = Departamentos()
#d1.agregar()
#d1.quitar()

#e1 = Empleados()
#e1.agregar()
#e1.quitar()

#n1 = Notas()
#n1.agregar()
#input("pausa")
#n1.quitar()

#c1 = Comentarios()
#c1.agregar()
#input("pausa")
#c1.quitar()

#l1 = Likes()
#l1.agregar()
#input("pausa")
#l1.quitar()


