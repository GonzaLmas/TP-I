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
    at_exists = "@" in email
    dot_after_at_exists = "." in email.split("@")[-1]
    is_valid = at_exists and dot_after_at_exists
    
    return is_valid

def validate_phone(phone):
    valid_characters = cons.AVAILABLE_PHONE_NUMBERS
    
    # Valida que el teléfono contenga solo números
    only_valid_chars = all(c in valid_characters for c in phone)
    if not only_valid_chars:
        return False
    
    # Valida que el teléfono tenga 10 dígitos
    digit_count = sum(c.isdigit() for c in phone)
    has_correct_length = digit_count == cons.PHONE_LENGHT
    
    return has_correct_length

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
    
    # Ordena de forma ascendente los contactos por su nombre
    sorted_contacts = sorted(contacts, key=lambda x: x[cons.NOMBRE].lower())
    
    for i, contact_name in enumerate(sorted_contacts, 1):
        contact_phone = f" - {contact_name[cons.TELEFONO]}" if contact_name[cons.TELEFONO] else ""
        contact_email = f" - {contact_name[cons.EMAIL]}" if contact_name[cons.EMAIL] else ""
        contact_category = f" [{contact_name[cons.CATEGORIA].title()}]"
        
        print(f"{i:2d}. {contact_name[cons.NOMBRE]}{contact_phone}{contact_email}{contact_category}")

def find_contacts(contacts, field):
    # Parsea el param recibido a minúscula y con strip() sanitiza el input del usuario
    field = field.lower().strip()
    results = []
    
    # Busca coincidencias en los tres campos
    for contact in contacts:
        if (field == contact[cons.NOMBRE].lower() or 
            field == contact[cons.TELEFONO].lower() or 
            field == contact[cons.EMAIL].lower()):
            results.append(contact)
    
    return results

def find_by_category(contacts, category):
    # Parsea el param recibido a minúscula para sanitizar posibles errores
    category_lower = category.lower()
    filtered_contacts = []

    for contact in contacts:
        # Parsea el param recibido a minúscula para sanitizar posibles errores
        contact_category = contact[cons.CATEGORIA].lower()
        
        # Evalúa la categoría del contacto con la categoría recibida por parámetro
        if contact_category == category_lower:
            filtered_contacts.append(contact)
    
    return filtered_contacts

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
