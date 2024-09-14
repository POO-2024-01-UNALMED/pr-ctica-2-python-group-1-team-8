from re import match
totalVentasSemanaActual = 0
totalVentasMesActual = 0
totalVentasYearActual = 0

def inspeccionEmpleado(local, fecha_actual):
    total_ventas_semana_actual = 0
    total_ventas_mes_actual = 0
    total_ventas_year_actual = 0
    #/ *~~~ Identificacion del empleado ~~~ * /

    empleado = indentificarEmpleado(local)

    if empleado is None:
        return

    #/ *~~~ Gestionar metas ~~~ * /

    gestionarMeta(empleado, fecha_actual)
    print("Presione enter para revisar si hay metas alcanzadas")
    input()

    #/*~~~ Mostrar metas alcanzadas ~~~ * /

    mostrarMetasAlcanzadas(empleado)

    #/ *~~~ Revisar metas caducadas ~~~ * /

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

    #/* ~~~ Ver rendimiento ~~~ */
    while True:
        pregunta = siNo("¿Desea ver el rendimiento del empleado?")
        if not pregunta:
            break

        rendimiento = verRendimiento(empleado, fecha_actual)
        compararRendimiento(empleado, fecha_actual, rendimiento)
        try:
            decision = int(input("¿Qué desea hacer? \n1. Ver el rendimiento en otro periodo \n2. Continuar"))

        except ValueError:
            print("Ingrese un numero valido. Presione enter para volver a intentar")
            input()
            continue

        if decision == 2:
            break

    #/* ~~~ Modificar Salarios o dias laborales ~~~ */
    while True:




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
        print(f"Las metas caducadas por el empleado {empleado.get_nombre()} son:")
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
            option = int(input(f"Desea ver el rendimiento del empleado {empleado.get_nombre()} \n1. Semanal \n2. Mensual \n3. Anual"))

        except ValueError:
            print("Ingrese un numero valido. Presione enter para volver a intentar")
            input()
            continue

        match option:
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

        while True:
            try:
                decision = int(input("¿Qué desea hacer? \n1. Ver el rendimiento en otro periodo de tiempo. \n2. Comparar el rendimiento con período anterior"))

            except ValueError:
                print("Ingrese un numero valido. Presione enter para volver a intentar")
                input()
                continue

            match decision:
                case 1:
                    break
                case 2:
                    return option
                case _:
                    print("Ingrese una opcion valida. Presione enter para volver a intentar")
                    input()
                    break

def compararRendimiento(empleado, fecha_actual, decision):
    match decision:
        case 1:
            total_semana = 0
            for t in empleado.get_transacciones():
                if fecha_actual.get_totalDias - 14 <= t.get_fecha().get_totalDias() and fecha_actual.get_totalDias - 7 >= t.get_fecha().get_totalDias():
                    total_semana += 1

            print(f"El total de ventas en la semana anterior del empleado {empleado.get_nombre()} fueron: {total_semana}")
            print("Presione enter para continuar.\n")
            input()

            if total_semana < total_ventas_semana_actual:
                calculo = ((total_ventas_semana_actual - total_semana) * 100) / total_semana
                print(f"El total de ventas en esta semana incremento en un {calculo}%")
                if calculo > 30:
                    print("El empleado tuvo un incremento en ventas mayor al 30%. El empleado debería tener una bonificacion remunerada")
                    print("Presione enter para continuar")
                    input()

            elif total_semana == total_ventas_semana_actual:
                print(f"El total de ventas fue igual al de la semana pasada {total_semana} ventas")
                print("Presione enter para continuar")
                input()

            else:
                calculo = ((total_semana - total_ventas_semana_actual) * 100) / total_semana
                print(f"El total de ventas en esta semana disminuyo en un {calculo}%")
                print("Presione enter para continuar")
                input()

        case 2:
            total_mes = 0
            for t in empleado.get_transacciones():
                if fecha_actual.get_totalDias - 62 <= t.get_fecha().get_totalDias() and fecha_actual.get_totalDias - 31 >= t.get_fecha().get_totalDias():
                    total_mes += 1

            if total_mes < total_ventas_mes_actual:
                calculo = ((total_ventas_mes_actual - total_mes) * 100) / total_mes
                print(f"El total de ventas en este mes incremento en un {calculo}%")
                if calculo > 30:
                    print("El empleado tuvo un incremento en ventas mayor al 30%. El empleado debería tener una bonificacion remunerada")
                    print("Presione enter para continuar")
                    input()

            elif total_mes == total_ventas_mes_actual:
                print(f"El total de ventas fue igual al del mes pasado {total_mes} ventas")
                print("Presione enter para continuar")
                input()

            else:
                calculo = ((total_mes - total_ventas_mes_actual) * 100) / total_mes
                print(f"El total de ventas en este mes disminuyo en un {calculo}%")
                print("Presione enter para continuar")
                input()

        case 3:
            total_year = 0
            for t in empleado.get_transacciones():
                if fecha_actual.get_totalDias - 730 <= t.get_fecha().get_totalDias() and fecha_actual.get_totalDias - 365 >= t.get_fecha().get_totalDias():
                    total_year += 1

            if total_year < total_ventas_year_actual:
                calculo = ((total_ventas_year_actual - total_year) * 100) / total_year
                print(f"El total de ventas en este año incremento en un {calculo}%")
                if calculo > 30:
                    print("El empleado tuvo un incremento en ventas mayor al 30%. El empleado debería tener una bonificacion remunerada")
                    print("Presione enter para continuar")
                    input()

            elif total_year == total_ventas_year_actual:
                print(f"El total de ventas fue igual al del año pasado {total_year} ventas")
                print("Presione enter para continuar")
                input()

            else:
                calculo = ((total_year - total_ventas_year_actual) * 100) / total_year
                print(f"El total de ventas en este año disminuyo en un {calculo}%")
                print("Presione enter para continuar")
                input()

        case _:
            print("Ingrese una opcion valida. Presione enter para volver a intentar")
            input()

def modificarSalario(empleado):
    while True:
        try:
            salario = int(input("Desea moficiar: \n1. Salario fijo \n2. Salario porcentual"))
        except ValueError:
            print("Ingrese un numero valido. Presione enter para volver a intentar")
            input()
            continue

        match salario:
            case 1:
                try:
                    print(f"El salario fijo del empleado es: {empleado.get_salario()}")
                    nuevo_salario = int(input("Ingrese el nuevo salario fijo: "))
                except ValueError:
                    print("Ingrese un numero valido. Presione enter para volver a intentar")
                    input()
                    continue

                empleado.set_salario(nuevo_salario)
                print(f"El salario fijo del empleado {empleado.get_nombre()} ha sido actualizado a {nuevo_salario}")
                return

            case 2:
                try:
                    print(f"El salario porcentual del empleado es: {empleado.get_salario_porcentual()}")
                    nuevo_salario = int(input("Ingrese el nuevo salario porcentual: "))
                except ValueError:
                    print("Ingrese un numero valido. Presione enter para volver a intentar")
                    input()
                    continue

                empleado.set_salario_porcentual(nuevo_salario)
                print(f"El salario porcentual del empleado {empleado.get_nombre()} ha sido actualizado a {nuevo_salario}")
                return

            case _:
                print("Ingrese una opcion valida. Presione enter para volver a intentar")
                input()
                return
def modifcarDiasLaborales(empleado):
    while True:
        try:
            print(f"Los dias laborales del empleado {empleado.get_nombre()} son: {empleado.get_dias_laborales()} a la semana")
            nuevo_dias = int(input("Ingrese el nuevo numero de dias laborales: "))
        except ValueError:
            print("Ingrese un numero valido. Presione enter para volver a intentar")
            input()
            continue

        if nuevo_dias < 6 and nuevo_dias > 0:
            empleado.set_dias_laborales(nuevo_dias)
            print(f"Los dias laborales del empleado {empleado.get_nombre()} han sido actualizados a {dias_laborales}")
            return

        else:
            print("Cantidad inhumana de dias. Presione enter para volver a intentar")
            input()

def asignarMeta(empleado):
    while True:
        print(f"Las metas del empleado {empleado.get_nombre()} son: ")
        for m in empleado.get_metas():
            print(m)
        print("Presione enter para continuar")
        input()

        try:
            year_limite = int(input("Ingrese el año limite de la meta: "))
        except ValueError:
            print("Ingrese un numero valido. Presione enter para volver a intentar")
            input()
            continue

        try:
            mes_limite = int(input("Ingrese el mes limite de la meta: "))
        except ValueError:
            print("Ingrese un numero valido. Presione enter para volver a intentar")
            input()
            continue

        try:
            dia_limite = int(input("Ingrese el dia limite de la meta: "))
        except ValueError:
            print("Ingrese un numero valido. Presione enter para volver a intentar")
            input()
            continue

        try:
            valor_alcanzar = int(input("Ingrese el valor a alcanzar de la meta: "))
        except ValueError:
            print("Ingrese un numero valido. Presione enter para volver a intentar")
            input()
            continue

        try:
            valor_bonificacion = int(input("Ingrese el valor de la bonificacion de la meta: "))
        except ValueError:
            print("Ingrese un numero valido. Presione enter para volver a intentar")
            input()
            continue

        new Meta(empleado, year_limite, mes_limite, dia_limite, valor_alcanzar, valor_bonificacion)
        return