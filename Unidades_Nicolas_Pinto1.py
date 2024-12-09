from tkinter import messagebox, Label, Tk, StringVar, CENTER, ttk

def convertir_unidades(valor, unidad):
    resultados = {}

    if unidad == 'm':
        resultados['Centímetros'] = valor * 100
        resultados['Milímetros'] = valor * 1000
        resultados['Metros'] = valor  
    elif unidad == 'cm':
        resultados['Metros'] = valor / 100
        resultados['Milímetros'] = valor * 10
        resultados['Centímetros'] = valor  
    elif unidad == 'mm':
        resultados['Metros'] = valor / 1000
        resultados['Centímetros'] = valor / 10
        resultados['Milímetros'] = valor  
    else:
        raise ValueError("Unidad no válida. Usa 'm', 'cm' o 'mm'.")
    return resultados


root = Tk()
root.title("Conversor de Unidades")

valor_var = StringVar()
unidad_var = StringVar()

def mostrar_resultados():
    valor = valor_var.get()
    unidad = unidad_var.get().lower()

    if not valor or not valor.replace('.', '', 1).isdigit():
        messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido.")
        return

    try:
        valor_float = float(valor)
        resultados = convertir_unidades(valor_float, unidad)
        resultados_str = "\n".join([f"{unidad_convertida}: {resultado:.2f}" for unidad_convertida, resultado in resultados.items()])
        messagebox.showinfo("Resultados", resultados_str)
    except ValueError as e:
        messagebox.showerror("Error", str(e))


Label(root, text="Dame el número que quieres convertir:").grid(row=0, column=0, padx=10, pady=5)
valor_entry = ttk.Entry(root, textvariable=valor_var)
valor_entry.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="¿Qué unidad de medida es (m, cm, mm)?").grid(row=1, column=0, padx=10, pady=5)
unidad_entry = ttk.Combobox(root, textvariable=unidad_var, values=["m", "cm", "mm"])
unidad_entry.grid(row=1, column=1, padx=10, pady=5)

convertir_button = ttk.Button(root, text="Convertir", command=mostrar_resultados)
convertir_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()

