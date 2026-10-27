from pyscript import document,display

Nonmetals = {
    "O" : ("Oxygen", 8, 15.999), #tuple so string & the numbers can be together (?)
    "C" : ("Carbon", 6, 12.011),
    "N" : ("Nitrogen", 7, 14.007),
    "F" : ("Fluorine", 9, 18.9984),
    "H" : ("Hydrogen", 1, 1.008),
    "Cl" : ("Chlorine", 17, 35.45),
    "Rn" : ("Radon", 86, 222),
    "He" : ("Helium", 2, 4.0026),
    "Ar" : ("Argon", 18, 39.95),
    "Kr" : ("Krypton", 36, 83.798),
    "Xe" : ("Xenon", 54, 131.29),
    "Ne" : ("Neon", 10, 20.180),
    "Br" : ("Bromine", 35, 79.904),
    "P" : ("Phosphorus", 15, 30.974),
    "S" : ("Sulfur", 16, 32.06),
    "Se" : ("Selenium", 34, 78.971),
    "I" : ("Iodine", 53, 126.90),
}


# display(dict(Nonmetals), target="output1")
# check = display(dict(Nonmetals.get(Nonmetals)))
# display(Nonmetals.get("Nonmetals"))
def check(event):
    element_symbol = document.getElementById("Element").value.strip()
    result = Nonmetals.get(element_symbol, ("Element not found", "-", "-"))
    name, atomic_num, atomic_mass = result
    output_text = f"Element: {name} | Atomic Number: {atomic_num} | Mass: {atomic_mass}"
    document.getElementById("output1").innerText = output_text

