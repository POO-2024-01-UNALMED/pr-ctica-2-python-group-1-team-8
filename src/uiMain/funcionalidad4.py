from re import match
totalVentasSemanaActual = 0
totalVentasMesActual = 0
totalVentasYearActual = 0

def inspeccionEmpleado(local, fecha_actual):
    total_ventas_semana_actual = 0
    total_ventas_mes_actual = 0
    total_ventas_year_actual = 0
    empleado = indentificarEmpleado(local)

    if empleado is None:
        return

    gestionarMeta(empleado, fecha_actual)
    print("Presione enter para revisar si hay metas alcanzadas")
    input()

    mostrarMetasAlcanzadas(empleado)

    while not empleado.get_metas_caducadas() == False:
        mostrarMetasCaducadas(empleado)
        decision = siNo("¿Desea ampliar el plazo de alguna de las metas?")
        if decision:
            meta = revisarMetasCaducadas(empleado)
            if meta == None:
                break
            ampliarMeta(empleado, meta, fecha_actual)
        else:
            break

    while True:
        pregunta = siNo("¿Desea ver el rendimiento del empleado?")
        if not pregunta:
            break

        rendimineto = verRendimiento(empleado, fecha_actual)
        compararRendimiento(empleado, fechaActual, rendimiento)



def siNo(pregunta):
    respuesta = input(pregunta + " (S/n)")
    return False if respuesta == 'n' or  'N' else True


#Elegir con que empleado se desea usar la funcionalidad
def indentificarEmpleado(local):
    print("Empleados de la tienda:")

    for e in local.get_empleados():
        print(e)

    while True:

        try :
            cedula = int(input("Ingrese la cedula del empleado con el que desea trabajar: "))

            for e in local.get_empleados():
                if e.get_cedula() == cedula:
                    return e

            cedula = 0

        except ValueError:
            print("Ingrese un numero valido. Presione enter para volver a intentar\n")
            input()
            continue

        if cedula == 0:
            if not siNo("La cedula ingresada no corresponde a ningun empleado. Desea intentarlo de nuevo?"):
                return None

def gestionarMeta(empleado, fecha_actual):
    metasARemover = []

    print(f"Porcentaje de progreso de las metas del empleado: {empleado.get_nombre()}")
    for m in empleado.get_metas():
        porcentajeProgreso = m.get_acumulado() * 100 / m.get_valor_alcanzar()
        print(f"* Codigo: {m.get_codigo()} - Porcentaje de progreso: {porcentajeProgreso}%")

        if porcentajeProgreso >= 100 and fecha_actual.get_totalDias() <= m.get_fecha().get_totalDias(): #Si la meta se ha cumplido
            metasARemover.append(m)
            empleado.ingresar_meta_alcanzada(m)
            m.set_estado("Meta Cumplida")
            empleado.set_acumulado_mensual(empleado.get_acumulado_mensual() + m.get_valor_bonificacion())

        elif fecha_actual.get_totalDias() > m.get_fecha().get_totalDias(): #Si la meta ha caducado
            metasARemover.append(m)
            empleado.ingresar_meta_caducada(m)
            m.set_estado("Meta Caducada")

        for m in metasARemover:
            empleado.get_metas().remove(m)

def mostrarMetasAlcanzadas(empleado):
    if empleado.get_metas_alcanzadas() == []:
        print(f"El empleado {empleado.get_nombre()} no ha cumplido ninguna meta. Animo")
        print("Presione enter para continuar")
        input()

    else:
        print(f"Las metas alcanzadas por el empleado {empleado.get_nombre()} son:")
        for m in empleado.get_metas_alcanzadas():
            print(m)

def mostrarMetasCaducadas(empleado):
    if empleado.get_metas_caducadas() == []:
        print(f"El empleado {empleado.get_nombre()} no tiene metas caducadas")
        print("Presione enter para continuar")
        input()

    else:
        print(f"Las me¿etas caducadas por el empleado {empleado.get_nombre()} son:")
        for m in empleado.get_metas_caducadas():
            print(m)

def revisarMetasCaducadas(empleado):
    while True:
        try:
            codigo = int(input("Ingrese el codigo de la meta que desea modificar: "))

        except ValueError:
            print("Ingrese un numero valido. Presione enter para volver a intentar")
            input()
            continue

        for m in empleado.get_metas_caducadas():
            if m.get_codigo() == codigo:
                return m

        if not siNo("El codigo ingresado no corresponde a ninguna meta. ¿Desea intentarlo de nuevo?"):
            return None

def ampliarMeta(empleado, meta, fecha_actual):
    while True:
        try:
            year_ajuste = int(input("Ingrese el año en que desea ampliar la meta:"))

        except ValueError:
            print("Ingrese un numero valido. Presione enter para volver a intentar")
            input()
            continue

        meta.get_fecha().set_year(year_ajuste)

        try:
            mes_ajuste = int(input("Ingrese el mes en que desea ampliar la meta:"))

        except ValueError:
            print("Ingrese un numero valido. Presione enter para volver a intentar")
            input()
            continue

        meta.get_fecha().set_mes(mes_ajuste)

        try:
            dia_ajuste = int(input("Ingrese el dia en que desea ampliar la meta:"))

        except ValueError:
            print("Ingrese un numero valido. Presione enter para volver a intentar")
            input()
            continue

        meta.get_fecha().set_dia(dia_ajuste)

        meta.get_fecha().set_totalDias(0)
        meta.get_fecha().set_totalDias(meta.get_fecha().fechaToDias(dia_ajuste, mes_ajuste, year_ajuste))

        if meta.get_fecha().get_totalDias() < fecha_actual.get_totalDias():
            print("Fecha no valida. Presione enter para volver a intentar")
            input()

        else:
            print(f"Fecha actualizada. La meta {meta.get_codigo()} quedo para {meta.get_fecha()}")
            print("Presione enter para continuar")
            empleado.get_metas_caducadas().remove(meta)
            empleado.ingresar_meta(meta)
            meta.set_estado("En proceso")
            input()
            break

def verRendimiento(empleado, fecha_actual):
    while True:
        try:
            opcion = int(print(f"Desea ver el rendimiento del empleado {empleado.get_nombre()} \n1. Semanal \n2. Mensual \n3. Anual"))

        except ValueError:
            print("Ingrese un numero valido. Presione enter para volver a intentar")
            input()
            continue

        match opcion:
            case 1:
                global total_ventas_semana_actual
                for t in empleado.get_transacciones():
                    if fecha_actual.get_totalDias - 7 <= t.get_fecha().get_totalDias():
                        total_ventas_semana_actual += 1
                print(f"El total de ventas semanales del empleado {empleado.get_nombre()} son {total_ventas_semana_actual}")
                break
            case 2:
                global total_ventas_mes_actual
                for t in empleado.get_transacciones():
                    if fecha_actual.get_totalDias - 31 <= t.get_fecha().get_totalDias():
                        total_ventas_mes_actual += 1
                print(f"El total de ventas mensuales del empleado {empleado.get_nombre()} son {total_ventas_mes_actual}")
                break
            case 3:
                global total_ventas_year_actual
                for t in empleado.get_transacciones():
                    if fecha_actual.get_totalDias - 365 <= t.get_fecha().get_totalDias():
                        total_ventas_year_actual += 1
                print(f"El total de ventas anuales del empleado {empleado.get_nombre()} son {total_ventas_year_actual}")
                break
            case _:
                print("Ingrese una opcion valida. Presione enter para volver a intentar")
                input()
                break

        while True
            try:
                print("¿Qué desea haer?")