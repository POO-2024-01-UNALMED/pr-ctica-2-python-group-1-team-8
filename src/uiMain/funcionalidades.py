# from src.gestorAplicacion import *
#
# class fRegistrarCompra:
#     def __init__(self):
#         self.sc_compra = input
#         self.puntos_usados = 0
#
#     def registrar_compra(self, local, fecha):
#         cliente = self.identificar_cliente()
#         if not cliente:
#             return
#
#         if cliente.compras:
#             generos_cant = {}
#             generos = []
#             for transaccion in cliente.compras:
#                 for producto in transaccion.productos:
#                     if isinstance(producto, Juego):
#                         genero = producto.genero
#                         generos_cant[genero] = generos_cant.get(genero, 0) + 1
#             genero_favorito = max(generos_cant, key=generos_cant.get)
#             print(f"Género favorito: {genero_favorito}")
#
#             plataformas = []
#             for transaccion in cliente.compras:
#                 for producto in transaccion.productos:
#                     if isinstance(producto, Juego):
#                         plataforma = producto.plataforma
#                         if plataforma not in plataformas:
#                             plataformas.append(plataforma)
#             print("Plataformas en las que ha comprado:")
#             for plataforma in plataformas:
#                 print("* " + plataforma)
#
#         carrito = []
#         while True:
#             self.imprimir_separador()
#             print("1. Agregar producto")
#             print("2. Eliminar producto")
#             print("3. Ver productos en el carrito")
#             print("4. Confirmar compra")
#             print("0. Cancelar y salir")
#
#             opcion = int(input())
#             if opcion == 1:
#                 producto = self.seleccionar_producto(local.inventario)
#                 esta_en_carrito = self.hallar_en_carrito(producto, carrito)
#                 if esta_en_carrito:
#                     if esta_en_carrito.cantidad >= producto.cantidad:
#                         print("No hay mas unidades disponibles.")
#                     else:
#                         esta_en_carrito.cantidad += 1
#                 else:
#                     producto.cantidad = 1
#                     carrito.append(producto)
#                 print("Producto agregado al carrito.")
#             elif opcion == 2:
#                 producto_en_carrito = self.seleccionar_producto(carrito)
#                 if producto_en_carrito.cantidad > 1:
#                     producto_en_carrito.cantidad -= 1
#                 else:
#                     carrito.remove(producto_en_carrito)
#                 print("Producto eliminado del carrito.")
#             elif opcion == 3:
#                 if carrito:
#                     print("CARRITO:")
#                     for p in carrito:
#                         print("* " + p)
#                 else:
#                     print("El carrito esta vacio.")
#             elif opcion == 4:
#                 if carrito:
#                     valor_final = self.calcular_descuentos(carrito, cliente)
#                     print(f"Valor total de la compra: ${valor_final}")
#
#                     while True:
#                         valor_ingresado = int(input("Ingrese el valor con el que pagara: "))
#                         if valor_ingresado < valor_final:
#                             print("El valor ingresado es menor al total de la compra.")
#                         else:
#                             break
#
#                     cambio = valor_ingresado - valor_final
#                     print(f"Cambio: ${cambio}")
#
#                     empleado = self.identificar_empleado(local)
#                     for meta in empleado.metas:
#                         meta.incrementar_acumulado(valor_final)
#
#                     transaccion = Transaccion(fecha, cliente, empleado, local, carrito, valor_final)
#
#                     print("\nPresione Enter para confirmar la compra.")
#                     input()
#
#                     for producto in carrito:
#                         if isinstance(producto, Consola):
#                             for p2 in local.inventario:
#                                 if isinstance(p2, Consola) and p2.codigo == producto.codigo:
#                                     p2.cantidad -= producto.cantidad
#                         elif isinstance(producto, Juego):
#                             for p2 in local.inventario:
#                                 if isinstance(p2, Juego) and p2.codigo == producto.codigo:
#                                     p2.cantidad -= producto.cantidad
#                         elif isinstance(producto, Accesorio):
#                             for p2 in local.inventario:
#                                 if isinstance(p2, Accesorio) and p2.codigo == producto.codigo:
#                                     p2.cantidad -= producto.cantidad
#
#                     cliente.puntos_fidelidad -= puntos_usados
#                     cliente.agregar_compra(transaccion)
#
#                     print("""
#                                    ...
#
#                                    ᕕ( ᐛ )ᕗ
#                                    ¡Compra realizada con exito!
#                                    """)
#                     return
#                 else:
#                     print("El carrito esta vacio.")
#             else:
#                 print("Opcion fuera del rango.")
#
#     def seleccionar_producto(self, inventario):
#         while True:
#             self.imprimir_separador()
#             print("Ingrese el tipo del producto:")
#             print("1. Consola")
#             print("2. Juego")
#             print("3. Accesorio")
#
#             opcion = int(input())
#
#             if opcion == 1:
#                 print("Consolas disponibles:")
#                 for p in inventario:
#                     if isinstance(p, Consola) and p.cantidad > 0:
#                         print("* " + p)
#                 codigo = int(input("Ingrese el codigo de la consola que desea seleccionar: "))
#                 for p in inventario:
#                     if isinstance(p, Consola) and p.codigo == codigo:
#                         print(f"'{p.nombre}' seleccionado.")
#                         return p
#                 print("Consola no encontrada.")
#             elif opcion == 2:
#                 print("Consolas disponibles:")
#                 for p in inventario:
#                     if isinstance(p, Consola) and p.cantidad > 0:
#                         print("* " + p)
#                 codigo = int(input("Ingrese el codigo de la consola que desea seleccionar: "))
#                 for p in inventario:
#                     if isinstance(p, Consola) and p.codigo == codigo:
#                         print(f"'{p.nombre}' seleccionado.")
#                         return p
#                 print("Consola no encontrada.")
#             elif opcion == 3:
#                 print("Consolas disponibles:")
#                 for p in inventario:
#                     if isinstance(p, Consola) and p.cantidad > 0:
#                         print("* " + p)
#                 codigo = int(input("Ingrese el codigo de la consola que desea seleccionar: "))
#                 for p in inventario:
#                     if isinstance(p, Consola) and p.codigo == codigo:
#                         print(f"'{p.nombre}' seleccionado.")
#                         return p
#                 print("Consola no encontrada.")
#             else:
#                 print("Opcion fuera del rango.")
#
#     def hallar_en_carrito(self, producto, carrito):
#         for p in carrito:
#             if p.nombre == producto.nombre:
#                 return p
#         return None
#
#     def calcular_descuentos(self, carrito, cliente):
#         precio_final = 0
#         puntos_usados = 0
#         for producto in carrito:
#             if producto.descuento > 0:
#                 if producto.puntos_requeridos == 0:
#                     valor_temp = producto.valor * producto.cantidad
#                     precio_final_individual = valor_temp - (valor_temp * producto.descuento / 100)
#                     precio_final += precio_final_individual
#                     print(f"    * Descuento aplicado a '{producto.nombre}': ${valor_temp} ---> ${precio_final_individual}")
#                 elif producto.puntos_requeridos > 0 and (cliente.puntos_fidelidad - puntos_usados) >= producto.puntos_requeridos:
#                     valor_temp = producto.valor * producto.cantidad
#                     precio_final_individual = valor_temp - (valor_temp * producto.descuento / 100)
#                     precio_final += precio_final_individual
#                     puntos_usados += producto.puntos_requeridos
#                     print(f"    * Descuento aplicado a '{producto.nombre}': ${valor_temp} ---> ${precio_final_individual} | Puntos usados: {producto.puntos_requeridos}")
#                 else:
#                     precio_final += producto.valor * producto.cantidad
#             else:
#                 precio_final += producto.valor * producto.cantidad
#         if puntos_usados > 0:
#             print(f"Puntos usados: {puntos_usados}")
#         return precio_final
#
#     def identificar_empleado(self, local):
#         while True:
#             print("Ingrese la cedula del empleado encargado de esta transaccion")
#             cedula_empleado = int(input())
#             for empleado in local.empleados:
#                 if empleado.cedula == cedula_empleado:
#                     return empleado
#             print("Empleado no encontrado.")
#
#
# class fRegistrarPrestamo:
#     def __init__(self):
#         self.sc_prestam = input
#     def registrar_prestamo(self, local, fecha):
#         cliente = self.identificar_cliente()
#         if not cliente:
#             return
#
#         self.comprobar_prestamos(cliente, fecha)
#         if self.tiene_vencidos(cliente):
#             print("El cliente tiene uno o más prestamos vencidos:")
#
#         prestamo_activo = False
#         for prestamo in cliente.prestamos:
#             if prestamo.estado == "Activo" or prestamo.estado == "Vencido":
#                 prestamo_activo = True
#                 break
#
#         if prestamo_activo:
#             if self.si_no("¿Desea devolver productos prestados?"):
#                 for prestamo in cliente.prestamos:
#                     if prestamo.estado == "Vencido":
#                         multa = 0
#                         dias_vencidos = fecha.total_dias - prestamo.fecha_fin.total_dias
#
#                         for producto in prestamo.productos:
#                             multa += int(producto.valor * 0.1 * dias_vencidos)
#
#                         print(prestamo)
#                         print("Este prestamo esta vencido.")
#
#                         if self.si_no("¿Desea devolver los productos de este prestamo?"):
#                             multa += self.comprobar_devolucion(prestamo)
#                             self.cobrar_multa(multa, local)
#                             self.devolver_productos_prestados(prestamo, local)
#                             print("Productos devueltos.")
#                     elif prestamo.estado == "Activo":
#                         multa = 0
#                         print(f"* Prestamo con ID {prestamo.id} generado el {prestamo.fecha_inicio}, con fecha de fin el {prestamo.fecha_fin} y productos: {prestamo.productos}")
#
#                         if self.si_no("¿Desea devolver los productos de este prestamo?"):
#                             multa = self.comprobar_devolucion(prestamo)
#                             self.cobrar_multa(multa, local)
#                             self.devolver_productos_prestados(prestamo, local)
#                             print("Productos devueltos.")
#
#                 self.comprobar_prestamos(cliente, fecha)
#
#                 if self.tiene_vencidos(cliente):
#                     print("El cliente sigue teniendo prestamos vencidos. No se puede realizar un nuevo prestamo.")
#                     return
#
#         if self.si_no("¿Desea realizar un prestamo?"):
#             carrito = []
#             while True:
#                 self.imprimir_separador()
#                 print("1. Agregar producto")
#                 print("2. Eliminar producto")
#                 print("3. Ver productos en el carrito")
#                 print("4. Confirmar Prestamo")
#                 print("0. Cancelar y salir")
#
#                 opcion = int(input())
#                 if opcion == 1:
#                     producto = self.seleccionar_producto(local.inventario_prestamo)
#                     if producto:
#                         if producto not in carrito:
#                             carrito.append(producto)
#                             print("Producto agregado al carrito.")
#                         else:
#                             print("¡Solo esta permitido un ejemplar por prestamo! (ノ ゜Д゜)ノ ︵ ┻━┻")
#                 elif opcion == 2:
#                     producto_en_carrito = self.seleccionar_producto(carrito)
#                     if producto_en_carrito:
#                         carrito.remove(producto_en_carrito)
#                         print("Producto eliminado del carrito.")
#                     else:
#                         print("Producto no encontrado en el carrito.")
#                 elif opcion == 3:
#                     if carrito:
#                         print("CARRITO:")
#                         for p in carrito:
#                             print("* " + p.nombre)
#                     else:
#                         print("El carrito esta vacio.")
#                 elif opcion == 4:
#                     if carrito:
#                         valor = 0
#                         for producto in carrito:
#                             valor += producto.valor * 0.01
#
#                         print("1. 2 semanas (14 dias)")
#                         print("2. 1 mes (30 dias)")
#                         print("3. Mes y medio (45 dias)")
#                         print("4. 2 meses (60 dias)")
#
#                         print("Ingrese el tipo de plazo para el prestamo:")
#
#                         dias = 0
#                         while dias == 0:
#                             opcion_plazo = int(input())
#                             if opcion_plazo == 1:
#                                 dias = 14
#                                 valor = valor * dias
#                             elif opcion_plazo == 2:
#                                 dias = 30
#                                 valor = valor * dias
#                             elif opcion_plazo == 3:
#                                 dias = 45
#                                 valor = int(valor * dias * 0.90)
#                             elif opcion_plazo == 4:
#                                 dias = 60
#                                 valor = int(valor * dias * 0.85)
#                             else:
#                                 print("Opcion fuera del rango.")
#
#                         valor_int = int(valor)
#                         print(f"El precio total del prestamo es de ${valor_int} por {dias} dias.")
#
#                         fecha_fin = self.calcular_fecha_fin(fecha, dias)
#
#                         while True:
#                             valor_ingresado = int(input("Ingrese el valor con el que pagara: "))
#                             if valor_ingresado < valor_int:
#                                 print("El valor ingresado es menor al requerido.")
#                             else:
#                                 break
#
#                         cambio = valor_ingresado - valor_int
#                         print(f"Cambio: ${cambio}")
#
#                         for producto in carrito:
#                             Tienda.retirar_uno_de_inventario(producto, local.inventario_prestamo)
#
#                         prestamo = Prestamo(fecha, fecha_fin, cliente, carrito, valor_int, "Activo")
#                         local.agregar_fondos(valor_int)
#
#                         print("\nPresione Enter para confirmar el prestamo.")
#                         input()
#                     else:
#                         print("El carrito esta vacio.")
#                 else:
#                     print("Opcion fuera del rango.")
#     def seleccionar_producto(self, inventario_prestamo):
#         while True:
#             self.imprimir_separador()
#             print("Ingrese el tipo del producto:")
#             print("1. Consola")
#             print("2. Juego")
#             print("3. Accesorio")
#
#             opcion = int(input())
#
#             if opcion == 1:
#                 hay_consolas = False
#                 for p in inventario_prestamo:
#                     if isinstance(p, Consola) and p.cantidad > 0:
#                         hay_consolas = True
#                         break
#
#                 if not hay_consolas:
#                     print("No hay consolas disponibles para prestamo.")
#                     input()
#                     return None
#
#                 print("Consolas disponibles:")
#                 for p in inventario_prestamo:
#                     if isinstance(p, Consola) and p.cantidad > 0:
#                         print("* " + p.toString_prestable())
#
#                 codigo = int(input("Ingrese el codigo de la consola que desea seleccionar: "))
#                 for p in inventario_prestamo:
#                     if isinstance(p, Consola) and p.codigo == codigo:
#                         print(f"'{p.nombre}' seleccionado.")
#                         return p
#                 print("Consola no encontrada.")
#             elif opcion == 2:
#                 hay_consolas = False
#                 for p in inventario_prestamo:
#                     if isinstance(p, Consola) and p.cantidad > 0:
#                         hay_consolas = True
#                         break
#
#                 if not hay_consolas:
#                     print("No hay consolas disponibles para prestamo.")
#                     input()
#                     return None
#
#                 print("Consolas disponibles:")
#                 for p in inventario_prestamo:
#                     if isinstance(p, Consola) and p.cantidad > 0:
#                         print("* " + p.toString_prestable())
#
#                 codigo = int(input("Ingrese el codigo de la consola que desea seleccionar: "))
#                 for p in inventario_prestamo:
#                     if isinstance(p, Consola) and p.codigo == codigo:
#                         print(f"'{p.nombre}' seleccionado.")
#                         return p
#                 print("Consola no encontrada.")
#                 elif opcion == 3:
#                     hay_consolas = False
#                     for p in inventario_prestamo:
#                         if isinstance(p, Consola) and p.cantidad > 0:
#                             hay_consolas = True
#                             break
#
#                     if not hay_consolas:
#                         print("No hay consolas disponibles para prestamo.")
#                         input()
#                         return None
#
#                     print("Consolas disponibles:")
#                     for p in inventario_prestamo:
#                         if isinstance(p, Consola) and p.cantidad > 0:
#                             print("* " + p.toString_prestable())
#
#                     codigo = int(input("Ingrese el codigo de la consola que desea seleccionar: "))
#                     for p in inventario_prestamo:
#                         if isinstance(p, Consola) and p.codigo == codigo:
#                             print(f"'{p.nombre}' seleccionado.")
#                             return p
#                     print("Consola no encontrada.")
#             else:
#                 print("Opcion fuera del rango.")
#     def comprobar_prestamos(self, cliente, fecha):
#         if cliente.prestamos:
#             for prestamo in cliente.prestamos:
#                 if prestamo.fecha_fin.total_dias < fecha.total_dias:
#                     print(f"El prestamo con ID {prestamo.id} ha vencido.")
#                     prestamo.estado = "Vencido"
#     def tiene_vencidos(self, cliente):
#         for prestamo in cliente.prestamos:
#             if prestamo.estado == "Vencido":
#                 return True
#         return False
#     def devolver_productos_prestados(self, prestamo, local):
#         para_anadir = []
#         for producto in prestamo.productos:
#             for p in local.inventario_prestamo:
#                 if p.nombre == producto.nombre:
#                     p.cantidad += 1
#                 else:
#                     para_anadir.append(producto)
#         for producto in para_anadir:
#             local.inventario_prestamo.append(producto)
#         prestamo.estado = "Devuelto"
#     def comprobar_devolucion(self, prestamo):
#         multa = 0
#         print("Por favor, revise el estado de los productos devueltos.")
#
#         for producto in prestamo.productos:
#             if not self.si_no(f"¿El producto '{producto.nombre}' se encuentra en buen estado?"):
#                 multa += int(producto.valor * 0.25)
#
#         return multa
#
# import random
#
# class fSubastar:
#     def __init__(self):
#         self.sc_sub = input
#
#     def registrar_subasta(self, local, fecha):
#         self.comprobar_subastas(local, fecha)
#
#         while True:
#             self.imprimir_separador()
#             print("1. Crear Subasta")
#             print("2. Registrar Oferta")
#             print("3. Ver subastas activas")
#             print("4. Actualizar subasta descendente")
#             print("0. Salir")
#
#             opcion_menu = self.obtener_opcion_valida("Seleccione una opción: ")
#
#             if opcion_menu == 1:
#                 lista_producto_subasta = []
#
#                 while True:
#                     producto = self.seleccionar_producto(local.get_inventario_usado())
#                     if producto:
#                         lista_producto_subasta.append(producto)
#                         local.retirar_uno_de_inventario(producto, local.get_inventario_usado())
#                         print("Producto agregado a la subasta.")
#                     else:
#                         break
#
#                 self.imprimir_separador()
#                 print("1. Subasta Ascendente")
#                 print("2. Subasta Descendente")
#                 print("3. Subasta Anonima")
#
#                 opcion_sub_menu1 = self.obtener_opcion_valida("Indique el tipo de subasta que desea crear: ")
#
#                 if opcion_sub_menu1 == 1:
#                     self.registrar_subasta_ascendente(local, lista_producto_subasta, fecha)
#                 elif opcion_sub_menu1 == 2:
#                     self.registrar_subasta_descendente(local, lista_producto_subasta, fecha)
#                 elif opcion_sub_menu1 == 3:
#                     self.registrar_subasta_anonima(local, lista_producto_subasta, fecha)
#                 else:
#                     print("Opción fuera del rango.")
#
#             elif opcion_menu == 2:
#                 subasta_selec = self.seleccionar_subasta(local)
#
#                 if subasta_selec:
#                     cliente = self.identificar_cliente()
#
#                     if cliente.get_puntos_fidelidad() == 0:
#                         print("El cliente no tiene puntos de fidelidad para ofertar.")
#                     else:
#                         if subasta_selec.tipo == "Ascendente":
#                             while True:
#                                 try:
#                                     print(f"Ingrese el valor de su oferta: (ultima oferta: {subasta_selec.get_oferta_mayor()})")
#                                     oferta = int(input())
#
#                                     if oferta > cliente.get_puntos_fidelidad():
#                                         print("El cliente no tiene suficientes puntos de fidelidad para ofertar.")
#                                         print(f"Puntos de {cliente.nombre}: {cliente.get_puntos_fidelidad()}")
#                                     else:
#                                         subasta_selec.agregar_oferta(oferta, cliente)
#                                         print("Oferta registrada con exito.")
#                                         break
#                                 except ValueError:
#                                     print("Ingrese un valor válido.")
#                         elif subasta_selec.tipo == "Descendente":
#                             print(f"El valor actualmente asignado a esta subasta es: {subasta_selec.get_oferta_mayor()}")
#                             if cliente.get_puntos_fidelidad() >= subasta_selec.get_oferta_mayor():
#                                 if self.si_no(f"¿Desea ofertar con este valor a nombre de {cliente.nombre}?"):
#                                     subasta_selec.ofertar_y_finalizar_descendente(cliente)
#                                     print("Oferta ganadora registrada con exito.")
#                                     print("Productos subastados:")
#                                     for producto in subasta_selec.get_productos():
#                                         print(f"    * {producto.nombre}")
#                                 else:
#                                     print("El cliente no tiene suficientes puntos de fidelidad para tomar esta subasta.")
#                                     print(f"Puntos de {cliente.nombre}: {cliente.get_puntos_fidelidad()}")
#                         elif subasta_selec.tipo == "Anonima":
#                             while True:
#                                 try:
#                                     print("Ingrese el valor de su oferta: ")
#                                     oferta = int(input())
#
#                                     if oferta > cliente.get_puntos_fidelidad():
#                                         print("El cliente no tiene suficientes puntos de fidelidad para ofertar.")
#                                         print(f"Puntos de {cliente.nombre}: {cliente.get_puntos_fidelidad()}")
#                                     else:
#                                         subasta_selec.agregar_oferta_anonima(oferta, cliente)
#                                         print("Oferta registrada con exito.")
#                                         break
#                                 except ValueError:
#                                     print("Ingrese un valor válido.")
#                 else:
#                     print("No hay subastas activas.")
#
#             elif opcion_menu == 3:
#                 self.mostrar_subastas(local)
#
#             elif opcion_menu == 4:
#                 subasta = self.seleccionar_subasta_descendente(local)
#
#                 if subasta:
#                     print(f"La subasta actualmente tiene un valor de: {subasta.get_oferta_mayor()}")
#                     disminucion = self.obtener_entero("En cuanto desea disminuir el valor?")
#
#                     subasta.set_oferta_mayor(subasta.get_oferta_mayor() - disminucion)
#                 else:
#                     print("No hay subastas descendentes activas.")
#
#             elif opcion_menu == 0:
#                 break
#
#             else:
#                 print("Opción fuera del rango.")
#
#     def seleccionar_producto(self, inventario_usado):
#         while True:
#             self.imprimir_separador()
#             print("Ingrese el tipo del producto:")
#             print("1. Consola")
#             print("2. Juego")
#             print("3. Accesorio")
#
#             opcion = self.obtener_opcion_valida("Ingrese una opción válida: ")
#
#             if opcion == 1:
#                 hay_consolas = False
#                 for p in inventario_usado:
#                     if isinstance(p, Consola) and p.cantidad > 0:
#                         hay_consolas = True
#                         break
#
#                 if not hay_consolas:
#                     print("No hay consolas disponibles para subasta.")
#                     input()
#                     return None
#
#                 print("Consolas disponibles:")
#                 for p in inventario_usado:
#                     if isinstance(p, Consola) and p.cantidad > 0:
#                         print("* " + p.toString_prestable())
#
#                 codigo = self.obtener_entero("Ingrese el codigo de la consola que desea seleccionar: ")
#                 for p in inventario_usado:
#                     if isinstance(p, Consola) and p.codigo == codigo:
#                         print(f"'{p.nombre}' seleccionado.")
#                         return p
#                 print("Consola no encontrada.")
#             elif opcion == 2:
#                 hay_consolas = False
#                 for p in inventario_usado:
#                     if isinstance(p, Consola) and p.cantidad > 0:
#                         hay_consolas = True
#                         break
#
#                 if not hay_consolas:
#                     print("No hay consolas disponibles para subasta.")
#                     input()
#                     return None
#
#                 print("Consolas disponibles:")
#                 for p in inventario_usado:
#                     if isinstance(p, Consola) and p.cantidad > 0:
#                         print("* " + p.toString_prestable())
#
#                 codigo = self.obtener_entero("Ingrese el codigo de la consola que desea seleccionar: ")
#                 for p in inventario_usado:
#                     if isinstance(p, Consola) and p.codigo == codigo:
#                         print(f"'{p.nombre}' seleccionado.")
#                         return p
#                 print("Consola no encontrada.")
#             elif opcion == 3:
#                 hay_consolas = False
#                 for p in inventario_usado:
#                     if isinstance(p, Consola) and p.cantidad > 0:
#                         hay_consolas = True
#                         break
#
#                 if not hay_consolas:
#                     print("No hay consolas disponibles para subasta.")
#                     input()
#                     return None
#
#                 print("Consolas disponibles:")
#                 for p in inventario_usado:
#                     if isinstance(p, Consola) and p.cantidad > 0:
#                         print("* " + p.toString_prestable())
#
#                 codigo = self.obtener_entero("Ingrese el codigo de la consola que desea seleccionar: ")
#                 for p in inventario_usado:
#                     if isinstance(p, Consola) and p.codigo == codigo:
#                         print(f"'{p.nombre}' seleccionado.")
#                         return p
#                 print("Consola no encontrada.")
#             else:
#                 print("Opcion fuera del rango.")
#
#     def comprobar_subastas(self, local, fecha):
#         for subasta in local.getSubastas():
#             if subasta.get_fecha_fin().total_dias < fecha.total_dias and subasta.get_estado() == "Activa":
#                 if subasta.get_ofertas().isEmpty():
#                     print(f"La subasta N° {subasta.getId()} ha finalizado sin ofertas. Se extenderá 7 días más.")
#                     subasta.extender_subasta(fecha)
#                 else:
#                     ganador = subasta.finalizar_subasta()
#                     print(f"La subasta con ID {subasta.getId()} ha finalizado.")
#                     for producto in subasta.get_productos():
#                         print(f"    * {producto.nombre}")
#                     print(f"El ganador es: {ganador.nombre}")
#                     input()
#
#     def mostrar_subastas(self, local):
#         if local.getSubastas().isEmpty():
#             print("No hay subastas activas.")
#         else:
#             print("Subastas activas:")
#             for subasta in local.getSubastas():
#                 if subasta.get_estado() == "Activa":
#                     print(subasta)
#
#     def seleccionar_subasta_descendente(local):
#         subasta_selec = None
#         sc_selec_subasta = input
#
#         lista_subastas = []
#
#         while subasta_selec is None:
#             for subasta in local.getSubastas():
#                 if subasta.getEstado().lower() == "activa" and subasta.getTipo().lower() == "descendente":
#                     print(f"*  Subasta ID: {subasta.getId()} | Fecha de fin: {subasta.getFechaFin()}")
#                     lista_subastas.append(subasta)
#
#             if not lista_subastas:
#                 print("No hay subastas descendentes activas.")
#                 return None
#
#             try:
#                 id_subasta = int(input("Ingrese el ID de la subasta a la que desea ofertar: "))
#             except ValueError:
#                 print("Ingrese un valor válido para el ID de la subasta.")
#                 continue
#
#             for subasta in local.getSubastas():
#                 if subasta.getId() == id_subasta:
#                     subasta_selec = subasta
#                     break
#
#             if subasta_selec is None:
#                 print("No se encontró ninguna subasta con ese ID.")
#
#         return subasta_selec