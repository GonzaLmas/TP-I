from datetime import datetime

def show_menu():
    print("\n" + "="*50)
    print("    SISTEMA DE AGENDA")
    print("="*50)
    print("1. Agregar contacto")
    print("2. Mostrar todos los contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Eliminar contacto")
    print("6. Buscar por categoría")
    print("7. Salir")
    print("="*50)

def validate_email(email):
    # Valida que el email tenga un formato básico correcto
    return "@" in email and "." in email.split("@")[-1]

def validate_phone(phone):
   # Valida que el teléfono contenga solo números y espacios/guiones
    valid_characters = "0123456789 -+()"
    
    return all(c in valid_characters for c in phone) and len(phone.strip()) >= 7

def validate_date(date_str):
   # Valida que la fecha tenga formato DD/MM/YYYY
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def create_contact():
    # Crea un nuevo contacto solicitando datos al usuario
    print("\n--- AGREGAR NUEVO CONTACTO ---")
    
    while True:
        name = input("Nombre completo: ").strip()
        if name:
            break
        print("El nombre es obligatorio.")
    
    while True:
        phone = input("Teléfono: ").strip()
        if not phone:
            break
        if validate_phone(phone):
            break
        print("Formato de teléfono inválido. Use números, espacios, guiones o paréntesis.")
    
    while True:
        email = input("Email: ").strip().lower()
        if not email:
            break
        if validate_email(email):
            break
        print("Formato de email inválido.")
    
    print("\nCategorías disponibles:")
    
    categories = ["familia", "trabajo", "amigos", "otros"]
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat.title()}")
    
    while True:
        try:
            option = input("Seleccione categoría (1-4): ").strip()
            if option.isdigit() and 1 <= int(option) <= 4:
                category = categories[int(option) - 1]
                break
            else:
                break
        except:
            print("Opción inválida.")
    
    # Crear diccionario del contacto
    contact = {
        "nombre": name,
        "telefono": phone,
        "email": email,
        "categoria": category,
    }
    
    return contact

def show_contact(contact):
    # Muestra un contacto con formato organizado
    print("\n" + "-"*40)
    print(f"Nombre: {contact['nombre']}")
    
    if contact['telefono']:
        print(f"Teléfono: {contact['telefono']}")
    
    if contact['email']:
        print(f"Email: {contact['email']}")
    
    print(f"Categoría: {contact['categoria'].title()}")
    
    print("-"*40)

def show_all_contacts(contacts):
    # Muestra todos los contactos
    if not contacts:
        print("\nNo hay contactos registrados.")
        return
    
    print(f"\nTODOS LOS CONTACTOS ({len(contacts)} total)")
    print("="*60)
    
    # Ordenar por nombre
    sorted_contacts = sorted(contacts, key=lambda x: x['nombre'].lower())
    
    for i, contact in enumerate(sorted_contacts, 1):
        phone = f" - {contact['telefono']}" if contact['telefono'] else ""
        category = f" [{contact['categoria'].title()}]"
        
        print(f"{i:2d}. {contact['nombre']}{phone}{category}")

def find_contacts(contacts, field):
    # Busca contactos por nombre, teléfono o email
    field = field.lower().strip()
    results = []
    
    for contact in contacts:
        if (field in contact['nombre'].lower() or 
            field in contact['telefono'].lower() or 
            field in contact['email'].lower()):
            results.append(contact)
    
    return results

def find_by_category(contacts, category):
    # Busca contactos por categoría
    return [c for c in contacts if c['categoria'].lower() == category.lower()]

def edit_contact(contact):
    # Permite editar un contacto existente
    print(f"\n--- EDITANDO: {contact['nombre']} ---")
    print("Presione Enter para mantener el valor actual")
    
    # Editar nombre
    new_name = input(f"Nombre [{contact['nombre']}]: ").strip()
    if new_name:
        contact['nombre'] = new_name
    
    # Editar teléfono
    while True:
        new_phone = input(f"Teléfono [{contact['telefono']}]: ").strip()
        if not new_phone:
            break
        if validate_phone(new_phone):
            contact['telefono'] = new_phone
            break
        print("Formato de teléfono inválido.")
    
    # Editar email
    while True:
        new_email = input(f"Email [{contact['email']}]: ").strip().lower()
        if not new_email:
            break
        if validate_email(new_email):
            contact['email'] = new_email
            break
        print("Formato de email inválido.")
    
    # Editar categoría
    new_category = input(f"Categoría [{contact['categoria']}]: ").strip().lower()
    if new_category:
        contact['categoria'] = new_category
    
    print("Contacto editado exitosamente.")
    return True
