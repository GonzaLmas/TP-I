from agenda_management import functions as f
from agenda_management import constants as cons

def main():
    # Lista para almacenar todos los contactos 
    contacts = []
    
    # Bandera de control para el bucle principal
    flag = True
    
    print("Bienvenido al Sistema de Agenda!")
    
    # Bucle principal del programa
    while flag:
        try:
            f.show_menu()
            option = input("\nSeleccione una opción (1-7): ").strip()

            match option:
                case "1":
                    print("\nAGREGAR CONTACTO")
                    
                    new_contact = f.create_contact()
                    contacts.append(new_contact)
                    
                    print(f"Contacto '{new_contact[cons.NOMBRE]}' agregado exitosamente.")

                    while True:
                        another_contact = input("\n¿Desea agregar otro contacto? (s/n): ").lower().strip()
                        if another_contact == 's':
                            new_contact = f.create_contact()
                            contacts.append(new_contact)
                            
                            print(f"Contacto '{new_contact[cons.NOMBRE]}' agregado exitosamente.")
                        elif another_contact == 'n':
                            break
                        else:
                            print("Responda 's' para sí o 'n' para no.")

                case "2":
                    print("\nMOSTRAR TODOS LOS CONTACTOS")
                    f.show_all_contacts(contacts)

                case "3":
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

                case "4":
                    print("\nEDITAR CONTACTO")
                    
                    if not contacts:
                        print("No hay contactos para editar.")
                        continue

                    f.show_all_contacts(contacts)
                    
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
                            print(f"{i}. {contact[cons.NOMBRE]}")
                            
                        try:
                            contact_index = int(input("Seleccione el número del contacto a editar: ")) - 1
                            if 0 <= contact_index < len(results):
                                f.edit_contact(results[contact_index])
                            else:
                                print("Selección inválida.")
                                
                        except ValueError:
                            print("Debe ingresar un número válido.")

                case "5":
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
                            print(f"{i}. {contact[cons.NOMBRE]}")
                            
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
                    
                    if confirmation == 's':
                        contacts.remove(contact_to_remove)
                        print(f"Contacto '{contact_to_remove[cons.NOMBRE]}' eliminado exitosamente.")
                    else:
                        print("Eliminación cancelada.")

                case "6":
                    print("\nBUSCAR POR CATEGORÍA")
                    
                    if not contacts:
                        print("No hay contactos para buscar.")
                        continue

                    categories = set(c[cons.CATEGORIA] for c in contacts)
                    
                    print("Categorías disponibles:")
                    
                    for i, cat in enumerate(sorted(categories), 1):
                        quantity = len([c for c in contacts if c[cons.CATEGORIA] == cat])
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

                case "7":
                    print("\nGracias por usar el Sistema de Agenda.")
                    print("Hasta luego!")
                    
                    flag = False

                case _:
                    print("Opción inválida. Seleccione un número del 1 al 7.")

        except KeyboardInterrupt:
            print("\n\nInterrupción detectada.")
            exit = input("¿Desea salir del programa? (s/n): ").lower().strip()
            
            if exit == 's':
                print("Hasta luego!")
                flag = False

        except Exception as e:
            print(f"\nError inesperado: {e}")
            print("El programa continuará funcionando...")

        if flag:
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()