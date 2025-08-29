import agenda_management.functions as f

def main():
    # Lista para almacenar todos los contactos 
    contacts = []
    
    # Bandera de control para el bucle principal
    flag = True
    
    print("¡Bienvenido al Sistema de Agenda!")
    
    # Bucle principal del programa
    while flag:
        try:
            f.show_menu()
            option = input("\nSeleccione una opción (1-7): ").strip()
            
            if option == "1":
                print("\nAGREGAR CONTACTO")
                new_contact = f.create_contact()
                contacts.append(new_contact)
                print(f"Contacto '{new_contact['nombre']}' agregado exitosamente.")
                
                # Preguntar si quiere agregar otro
                while True:
                    another_contact = input("\n¿Desea agregar otro contacto? (s/n): ").lower().strip()
                    if another_contact in ['s', 'si', 'sí']:
                        new_contact = f.create_contact()
                        contacts.append(new_contact)
                        print(f"Contacto '{new_contact['nombre']}' agregado exitosamente.")
                    elif another_contact in ['n', 'no']:
                        break
                    else:
                        print("Responda 's' para sí o 'n' para no.")
            
            elif option == "2":
                print("\nMOSTRAR TODOS LOS CONTACTOS")
                f.show_all_contacts(contacts)
                
                if contacts:
                    # Opción para ver detalle de un contacto
                    while True:
                        view_detail = input("\n¿Desea ver el detalle de algún contacto? (número/n): ").strip()
                        if view_detail.lower() in ['n', 'no']:
                            break
                        try:
                            index = int(view_detail) - 1
                            sorted_contacts = sorted(contacts, key=lambda x: x['nombre'].lower())
                            if 0 <= index < len(sorted_contacts):
                                f.show_contact(sorted_contacts[index], True)
                            else:
                                print("Número de contacto inválido.")
                        except ValueError:
                            print("Ingrese un número válido o 'n' para salir.")
            
            elif option == "3":
                print("\n🔍 BUSCAR CONTACTO")
                if not contacts:
                    print("No hay contactos para buscar.")
                    continue
                
                field = input("Ingrese nombre, teléfono o email a buscar: ").strip()
                if not field:
                    print("Debe ingresar un término de búsqueda.")
                    continue
                
                results = f.find_contacts(contacts, field)
                
                if results:
                    print(f"\nSe encontraron {len(results)} resultado(s):")
                    for i, contact in enumerate(results, 1):
                        print(f"\n--- Resultado {i} ---")
                        f.show_contact(contact)
                else:
                    print(f"No se encontraron contactos con '{field}'.")
            
            elif option == "4":
                print("\nEDITAR CONTACTO")
                if not contacts:
                    print("No hay contactos para editar.")
                    continue
                
                # Mostrar lista de contactos
                f.show_all_contacts(contacts)
                
                # Buscar contacto a editar
                field = input("\nIngrese nombre del contacto a editar: ").strip()
                if not field:
                    print("Debe ingresar un nombre.")
                    continue
                
                results = f.find_contacts(contacts, field)
                
                if not results:
                    print(f"No se encontró el contacto '{field}'.")
                    continue
                
                if len(results) == 1:
                    f.edit_contact(results[0])
                else:
                    print(f"\nSe encontraron {len(results)} contactos:")
                    for i, contact in enumerate(results, 1):
                        print(f"{i}. {contact['nombre']}")
                    
                    try:
                        contact_index = int(input("Seleccione el número del contacto a editar: ")) - 1
                        if 0 <= contact_index < len(results):
                            f.edit_contact(results[contact_index])
                        else:
                            print("Selección inválida.")
                    except ValueError:
                        print("Debe ingresar un número válido.")
            
            elif option == "5":
                print("\nELIMINAR CONTACTO")
                if not contacts:
                    print("No hay contactos para eliminar.")
                    continue
                
                f.show_all_contacts(contacts)
                
                field = input("\nIngrese nombre del contacto a eliminar: ").strip()
                if not field:
                    print("Debe ingresar un nombre.")
                    continue
                
                results = f.find_contacts(contacts, field)
                
                if not results:
                    print(f"No se encontró el contacto '{field}'.")
                    continue
                
                contact_to_remove = None
                
                if len(results) == 1:
                    contact_to_remove = results[0]
                else:
                    print(f"\nSe encontraron {len(results)} contactos:")
                    for i, contact in enumerate(results, 1):
                        print(f"{i}. {contact['nombre']}")
                    
                    try:
                        contact_index = int(input("Seleccione el número del contacto a eliminar: ")) - 1
                        if 0 <= contact_index < len(results):
                            contact_to_remove = results[contact_index]
                        else:
                            print("Selección inválida.")
                            continue
                    except ValueError:
                        print("Debe ingresar un número válido.")
                        continue
                
                print(f"\nEstá a punto de eliminar:")
                f.show_contact(contact_to_remove)
                
                confirmation = input("¿Está seguro? (s/n): ").lower().strip()
                if confirmation in ['s', 'si', 'sí']:
                    contacts.remove(contact_to_remove)
                    print(f"Contacto '{contact_to_remove['nombre']}' eliminado exitosamente.")
                else:
                    print("Eliminación cancelada.")
            
            elif option == "6":
                print("\nBUSCAR POR CATEGORÍA")
                if not contacts:
                    print("No hay contactos para buscar.")
                    continue
                
                categories = set(c['categoria'] for c in contacts)
                print("Categorías disponibles:")
                
                for i, cat in enumerate(sorted(categories), 1):
                    quantity = len([c for c in contacts if c['categoria'] == cat])
                    print(f"{i}. {cat.title()} ({quantity} contactos)")
                
                category = input("\nIngrese la categoría a buscar: ").strip()
                if not category:
                    print("Debe ingresar una categoría.")
                    continue
                
                results = f.find_by_category(contacts, category)
                
                if results:
                    print(f"\nContactos en categoría '{category.title()}' ({len(results)}):")
                    for contact in results:
                        f.show_contact(contact)
                else:
                    print(f"No hay contactos en la categoría '{category}'.")
            
            elif option == "7":
                print("\nGracias por usar el Sistema de Agenda.")
                print("¡Hasta luego!")
                
                flag = False
            
            else:
                print("Opción inválida. Seleccione un número del 1 al 7.")
        
        except KeyboardInterrupt:
            # Manejo de Ctrl+C
            print("\n\nInterrupción detectada.")
            
            exit = input("¿Desea salir del programa? (s/n): ").lower().strip()
            
            if exit in ['s', 'si', 'sí']:
                print("¡Hasta luego!")
                
                flag = False
        
        except Exception as e:
            # Manejo de errores inesperados
            print(f"\nError inesperado: {e}")
            print("El programa continuará funcionando...")
        
        # Pausa para leer los mensajes (excepto en salida)
        if flag:
            input("\nPresione Enter para continuar...")

# Verificar si este archivo se está ejecutando directamente
if __name__ == "__main__":
    main()