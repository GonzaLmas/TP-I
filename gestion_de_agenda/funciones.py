from datetime import datetime

def show_menu():
    """
    Muestra el menú principal del sistema
    """
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
    """
    Valida que el email tenga un formato básico correcto
    Args:
        email (str): Email a validar
    Returns:
        bool: True si es válido, False si no
    """
    return "@" in email and "." in email.split("@")[-1]

def validate_phone(phone):
    """
    Valida que el teléfono contenga solo números y espacios/guiones
    Args:
        telefono (str): Teléfono a validar
    Returns:
        bool: True si es válido, False si no
    """
    valid_characters = "0123456789 -+()"
    return all(c in valid_characters for c in phone) and len(phone.strip()) >= 7

def validate_date(date_str):
    """
    Valida que la fecha tenga formato DD/MM/YYYY
    Args:
        fecha_str (str): Fecha en formato string
    Returns:
        bool: True si es válida, False si no
    """
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def create_contact():
    """
    Crea un nuevo contacto solicitando datos al usuario
    Returns:
        dict: Diccionario con los datos del contacto
    """
    print("\n--- AGREGAR NUEVO CONTACTO ---")
    
    # Solicitar nombre (obligatorio)
    while True:
        name = input("Nombre completo: ").strip()
        if name:
            break
        print("❌ El nombre es obligatorio.")
    
    # Solicitar teléfono con validación
    while True:
        phone = input("Teléfono: ").strip()
        if not phone:
            break
        if validate_phone(phone):
            break
        print("❌ Formato de teléfono inválido. Use números, espacios, guiones o paréntesis.")
    
    # Solicitar email con validación
    while True:
        email = input("Email: ").strip().lower()
        if not email:
            break
        if validate_email(email):
            break
        print("❌ Formato de email inválido.")
    
    # Solicitar categoría
    print("\nCategorías disponibles:")
    categories = ["familia", "trabajo", "amigos", "otros"]
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat.title()}")
    
    while True:
        try:
            option = input("Seleccione categoría (1-4) o escriba una nueva: ").strip()
            if option.isdigit() and 1 <= int(option) <= 4:
                category = categories[int(option) - 1]
                break
            elif option:
                category = option.lower()
                break
            else:
                category = "otros"
                break
        except:
            print("❌ Opción inválida.")
    
    # Solicitar fecha de cumpleaños
    while True:
        birthday = input("Fecha de cumpleaños (DD/MM/YYYY) [opcional]: ").strip()
        if not birthday:
            break
        if validate_date(birthday):
            break
        print("❌ Formato de fecha inválido. Use DD/MM/YYYY.")
    
    # Dirección (opcional)
    direccion = input("Dirección [opcional]: ").strip()
    
    # Notas adicionales (opcional)
    notas = input("Notas adicionales [opcional]: ").strip()
    
    # Crear diccionario del contacto
    contact = {
        "nombre": name,
        "telefono": phone,
        "email": email,
        "categoria": category,
    }
    
    return contact

def show_contact(contact):
    """
    Muestra un contacto con formato organizado
    Args:
        contacto (dict): Datos del contacto
        mostrar_fecha_creacion (bool): Si mostrar la fecha de creación
    """
    print("\n" + "-"*40)
    print(f"👤 Nombre: {contact['nombre']}")
    
    if contact['telefono']:
        print(f"📞 Teléfono: {contact['telefono']}")
    
    if contact['email']:
        print(f"📧 Email: {contact['email']}")
    
    print(f"🏷️  Categoría: {contact['categoria'].title()}")
    
    print("-"*40)

def show_all_contacts(contacts):
    """
    Muestra todos los contactos de forma resumida
    Args:
        contactos (list): Lista de contactos
    """
    if not contacts:
        print("\n❌ No hay contactos registrados.")
        return
    
    print(f"\n📖 TODOS LOS CONTACTOS ({len(contacts)} total)")
    print("="*60)
    
    # Ordenar por nombre
    sorted_contacts = sorted(contacts, key=lambda x: x['nombre'].lower())
    
    for i, contact in enumerate(sorted_contacts, 1):
        phone = f" - {contact['telefono']}" if contact['telefono'] else ""
        category = f" [{contact['categoria'].title()}]"
        print(f"{i:2d}. {contact['nombre']}{phone}{category}")

def find_contacts(contacts, field):
    """
    Busca contactos por nombre, teléfono o email
    Args:
        contactos (list): Lista de contactos
        termino_busqueda (str): Término a buscar
    Returns:
        list: Lista de contactos que coinciden
    """
    field = field.lower().strip()
    results = []
    
    for contact in contacts:
        # Buscar en nombre, teléfono y email
        if (field in contact['nombre'].lower() or 
            field in contact['telefono'].lower() or 
            field in contact['email'].lower()):
            results.append(contact)
    
    return results

def find_by_category(contacts, category):
    """
    Busca contactos por categoría
    Args:
        contactos (list): Lista de contactos
        categoria (str): Categoría a buscar
    Returns:
        list: Lista de contactos de esa categoría
    """
    return [c for c in contacts if c['categoria'].lower() == category.lower()]

def edit_contact(contact):
    """
    Permite editar un contacto existente
    Args:
        contacto (dict): Contacto a editar
    Returns:
        bool: True si se editó, False si se canceló
    """
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
        print("❌ Formato de teléfono inválido.")
    
    # Editar email
    while True:
        new_email = input(f"Email [{contact['email']}]: ").strip().lower()
        if not new_email:
            break
        if validate_email(new_email):
            contact['email'] = new_email
            break
        print("❌ Formato de email inválido.")
    
    # Editar categoría
    new_category = input(f"Categoría [{contact['categoria']}]: ").strip().lower()
    if new_category:
        contact['categoria'] = new_category
    
    print("✅ Contacto editado exitosamente.")
    return True
