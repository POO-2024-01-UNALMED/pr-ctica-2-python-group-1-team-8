class Fecha:
    def __init__(self, dia, mes, year):
        self.dia = dia
        self.mes = mes
        self.year = year

        self.total_dias = Fecha.fecha_a_dias(dia, mes, year)

    # TODO Crear constructor con totalDias

    # Metodo que retorna la cantidad de dias en una fecha dada
    @staticmethod
    def fecha_a_dias(dia, mes, year):
        total_dias = 0

        # sumar un dia por cada año bisiesto
        total_dias += ((year * 365) +
                       (year / 4) - (year / 100) + (year / 400))

        # añadir un dia mas por el año 0 (que es bisiesto)
        if year > 0: total_dias += 1

        # Si el año actual es bisiesto, se resta un dia
        if Fecha.es_bisiesto(year) and year != 0: total_dias -= 1

        # Meses
        # Sumar la cantidad de dias que corresponde por cada mes
        for (mesTemp) in range(2, mes + 1):
            match mesTemp:
                case 1, 3, 5, 7, 8, 10, 12:
                    total_dias += 31
                case 4, 6, 9, 11:
                    total_dias += 30
                case 2:
                    if Fecha.es_bisiesto(year):
                        total_dias += 29
                    else:
                        total_dias += 28

        # Dias
        total_dias += dia

        return total_dias

    # Metodo que asigna a un objeto Fecha una fecha a partir de un total de dias
    def dias_a_fecha(self, total_dias):
        year = 0
        mes = 1
        dia = 0

        # Sumar años restando 365 o 366 días hasta que el total de días sea menor a 365
        while True:
            if Fecha.es_bisiesto(year):
                if total_dias - 366 <= 0: break
                total_dias -= 366

            else:
                if total_dias - 365 <= 0: break
                total_dias -= 365

            year += 1

        # Restar la cantidad de dias que corresponde a cada mes hasta que
        # el total de días sea menor a la cantidad de dias que tiene un mes
        while total_dias > 0:
            match mes:
                case 1, 3, 5, 7, 8, 10, 12:
                    if total_dias - 31 > 0:
                        total_dias -= 31
                        mes += 1
                    else:
                        dia = total_dias
                        total_dias = 0

                case 4, 6, 9, 11:
                    if total_dias - 30 > 0:
                        total_dias -= 30
                        mes += 1
                    else:
                        dia = total_dias
                        total_dias = 0

                case 2:
                    if Fecha.es_bisiesto(year):
                        if total_dias - 29 > 0:
                            total_dias -= 29
                            mes += 1
                        else:
                            dia = total_dias
                            total_dias = 0
                    else:
                        if total_dias - 28 > 0:
                            total_dias -= 28
                            mes += 1
                        else:
                            dia = total_dias
                            total_dias = 0

        self.dia = dia
        self.mes = mes
        self.year = year

    # Metodo que verifica si un año dado es bisiesto
    @staticmethod
    def es_bisiesto(year):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    # Metodo toString
    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.year}"

    # Getters y setters
    def get_total_dias(self):
        return self.total_dias
    def get_dia(self):
        return self.dia
    def get_mes(self):
        return self.mes
    def get_year(self):
        return self.year

    def set_total_dias(self, total_dias):
        self.total_dias = total_dias
    def set_dia(self, dia):
        self.dia = dia
    def set_mes(self, mes):
        self.mes = mes
    def set_year(self, year):
        self.year = year