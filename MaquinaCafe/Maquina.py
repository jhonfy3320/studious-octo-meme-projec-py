#!/usr/bin/env python3
# main.py
# Máquina de café con menú interactivo por terminal

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "milk": 0, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}

# Recursos iniciales
resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0.0}


def is_resource_sufficient(order_ingredients):
    """Devuelve (True, "") si hay suficientes recursos, si no (False, mensaje)."""
    for item, amount_required in order_ingredients.items():
        if resources.get(item, 0) < amount_required:
            return False, f"Insuficiente {item}. Disponible: {resources.get(item,0)} ml/g"
    return True, ""


def process_payment(cost):
    """
    Pide al usuario el pago (importe en euros). Devuelve (True, change) si pago >= cost,
    si no devuelve (False, cantidad_insertada) para indicar que faltó dinero.
    """
    print(f"El precio es €{cost:.2f}. Inserte monedas o billetes. Puede escribir 0 para cancelar.")
    total = 0.0
    try:
        # modo simple: pedir un único importe float
        entry = input("Ingrese importe total en euros (ej. 2.50): ").strip()
        if not entry:
            print("Pago cancelado.")
            return False, 0.0
        total = float(entry.replace(",", "."))
    except ValueError:
        print("Cantidad inválida. Pago cancelado.")
        return False, 0.0

    if total < cost:
        return False, total
    change = round(total - cost, 2)
    return True, change


def make_coffee(drink_name, order_ingredients):
    """Resta los recursos y actualiza el dinero."""
    for item, amount in order_ingredients.items():
        resources[item] -= amount
    resources["money"] += MENU[drink_name]["cost"]


def print_report():
    print("Reporte de recursos:")
    print(f"  Agua: {resources['water']} ml")
    print(f"  Leche: {resources['milk']} ml")
    print(f"  Café: {resources['coffee']} g")
    print(f"  Dinero: €{resources['money']:.2f}")


def refill_resources():
    """Permite rellenar recursos interactivos (valores enteros)."""
    try:
        add_water = int(input("Agregar agua (ml): ") or 0)
        add_milk = int(input("Agregar leche (ml): ") or 0)
        add_coffee = int(input("Agregar café (g): ") or 0)
    except ValueError:
        print("Entrada inválida. No se realizaron cambios.")
        return
    resources["water"] += max(0, add_water)
    resources["milk"] += max(0, add_milk)
    resources["coffee"] += max(0, add_coffee)
    print("Recursos actualizados.")


def show_menu():
    print("\n=== Máquina de Café ===")
    print("Opciones:")
    for name, data in MENU.items():
        print(f"  - {name} : €{data['cost']:.2f}")
    print("  - report   --> Mostrar recursos")
    print("  - refill   --> Rellenar recursos")
    print("  - off      --> Apagar máquina")
    print()


def main():
    while True:
        show_menu()
        choice = input("¿Qué deseas? (espresso/latte/cappuccino/report/refill/off): ").strip().lower()
        if choice == "off":
            print("Apagando máquina. ¡Hasta luego!")
            break
        elif choice == "report":
            print_report()
        elif choice == "refill":
            refill_resources()
        elif choice in MENU:
            drink = MENU[choice]
            ok, msg = is_resource_sufficient(drink["ingredients"])
            if not ok:
                print("No se puede preparar:", msg)
                continue

            paid, value = process_payment(drink["cost"])
            if not paid:
                if value == 0:
                    print("Compra cancelada.")
                else:
                    print(f"Dinero insuficiente. Se retornó €{value:.2f}.")
                continue

            change = value
            make_coffee(choice, drink["ingredients"])
            print(f"Aquí tiene su {choice}. ¡Disfrute!")
            if change > 0:
                print(f"Su cambio: €{change:.2f}")
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()