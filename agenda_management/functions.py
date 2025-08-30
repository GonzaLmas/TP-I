from agenda_management import constants as cons

from datetime import datetime

def show_menu():
    print("\n" + "="*cons.LINE_LENGTH)
    print("    SISTEMA DE AGENDA")
    print("="*cons.LINE_LENGTH)
    print("1. Agregar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Eliminar contacto")
    print("6. Buscar por categoría")
    print("7. Salir")
    print("="*cons.LINE_LENGTH)

def validate_email(email):
    # Valida que el email tenga un formato correcto
    return "@" in email and "." in email.split("@")[-1]

def validate_phone(phone):
    valid_characters = cons.AVAILABLE_PHONE_NUMBERS
    
   # Valida que el teléfono contenga solo números    
    if not all(c in valid_characters for c in phone):
        return False
    
    # Valida que el telefono tenga 10 dígitos
    digit_count = sum(c.isdigit() for c in phone)
    
    return digit_count == cons.PHONE_LENGHT

def validate_date(date_str):
   # Valida que la fecha tenga formato DD/MM/YYYY
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def create_contact():
    print("\n--- AGREGAR NUEVO CONTACTO ---")
    
    while True:
        name = input("Nombre: ").strip()
        if name:
            break
        
        print("El nombre es obligatorio.")
    
    while True:
        phone = input("Teléfono: ").strip()
        if not phone:
            break
        if validate_phone(phone):
            break
        
        print("Formato de teléfono inválido. Ingrese únicamente números, 10 dígitos, sin espacios.")
    
    while True:
        email = input("Email: ").strip().lower()
        if not email:
            break
        if validate_email(email):
            break
        
        print("Formato de email inválido.")
    
    print("\nCategorías disponibles:")
    
    categories = cons.CATEGORIES_NAMES
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat.title()}")
    
    while True:
        try:
            option = input("Seleccione categoría (1-3): ").strip()
            if option.isdigit() and 1 <= int(option) <= cons.AVAILABLE_CATEGORIES:
                category = categories[int(option) - 1]
                break
            else:
                break
        except:
            print("Opción inválida.")
    
    # Crea un diccionario del contacto
    contact = {
        cons.NOMBRE: name,
        cons.TELEFONO: phone,
        cons.EMAIL: email,
        cons.CATEGORIA: category,
    }
    
    return contact

def show_contact(contact):
    print("\n" + "-"*cons.LINE_LENGTH)
    print(f"Nombre: {contact[cons.NOMBRE]}")
    
    if contact[cons.TELEFONO]:
        print(f"Teléfono: {contact[cons.TELEFONO]}")
    
    if contact[cons.EMAIL]:
        print(f"Email: {contact[cons.EMAIL]}")
    
    print(f"Categoría: {contact[cons.CATEGORIA].title()}")
    
    print("-"*cons.LINE_LENGTH)

def show_all_contacts(contacts):
    if not contacts:
        print("\nNo hay contactos registrados.")
        return
    
    print(f"\nTODOS LOS CONTACTOS ({len(contacts)} total)")
    print("="*cons.LINE_LENGTH)
    
    sorted_contacts = sorted(contacts, key=lambda x: x[cons.NOMBRE].lower())
    
    for i, contact in enumerate(sorted_contacts, 1):
        phone = f" - {contact[cons.TELEFONO]}" if contact[cons.TELEFONO] else ""
        category = f" [{contact[cons.CATEGORIA].title()}]"
        
        print(f"{i:2d}. {contact[cons.NOMBRE]}{phone}{category}")

def find_contacts(contacts, field):
    field = field.lower().strip()
    results = []
    
    for contact in contacts:
        if (field == contact[cons.NOMBRE].lower() or 
            field == contact[cons.TELEFONO].lower() or 
            field == contact[cons.EMAIL].lower()):
            results.append(contact)
    
    return results

def find_by_category(contacts, category):
    return [c for c in contacts if c[cons.CATEGORIA].lower() == category.lower()]

def edit_contact(contact):
    print(f"\n--- EDITANDO: {contact[cons.NOMBRE]} ---")
    print("Presione Enter para mantener el valor actual")
    
    # Modifica el nombre
    new_name = input(f"Nombre [{contact[cons.NOMBRE]}]: ").strip()
    if new_name:
        contact[cons.NOMBRE] = new_name
    
    # Modifica el teléfono
    while True:
        new_phone = input(f"Teléfono [{contact[cons.TELEFONO]}]: ").strip()
        if not new_phone:
            break
        if validate_phone(new_phone):
            contact[cons.TELEFONO] = new_phone
            break
        
        print("Formato de teléfono inválido.")
    
    # Modifica el email
    while True:
        new_email = input(f"Email [{contact[cons.EMAIL]}]: ").strip().lower()
        if not new_email:
            break
        if validate_email(new_email):
            contact[cons.EMAIL] = new_email
            break
        
        print("Formato de email inválido.")
    
    # Modifica la categoría
    new_category = input(f"Categoría [{contact[cons.CATEGORIA]}]: ").strip().lower()
    if new_category:
        contact[cons.CATEGORIA] = new_category
    
    print("Contacto editado exitosamente.")
    return True
