import tkinter as tk

pencere = tk.Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("320x450") 

giris_alani = tk.Entry(pencere, width=20, font=('Arial', 24), bd=5, justify='right')
giris_alani.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
giris_alani.insert(0, "0")

for i in range(4):
    pencere.grid_columnconfigure(i, weight=1)

current_expression = "" 
first_number = None     
operator = None         
is_new_number = True    

#İşlemler

def clear_all():
    """Tüm ekranı ve hafızayı temizler."""
    global current_expression, first_number, operator, is_new_number
    current_expression = ""
    first_number = None
    operator = None
    is_new_number = True
    giris_alani.delete(0, tk.END) 
    giris_alani.insert(0, "0")    

def button_click(char):
    """Sayı ve nokta düğmelerine basıldığında çalışır."""
    global current_expression, is_new_number
    
    if is_new_number: 
        giris_alani.delete(0, tk.END)
        is_new_number = False
        
    if giris_alani.get() == "0" and char != ".":
        giris_alani.delete(0, tk.END)

    if char == '.' and '.' in giris_alani.get():
        return 

    giris_alani.insert(tk.END, char) 
    current_expression = giris_alani.get() 
def set_operator(op):
    """Operatör düğmelerine (+,-,*,/) basıldığında çalışır."""
    global first_number, operator, is_new_number, current_expression
    if current_expression:
        first_number = float(current_expression) 
        operator = op 
        is_new_number = True 

def calculate():
    """Eşittir (=) düğmesine basıldığında çalışır."""
    global first_number, operator, is_new_number, current_expression
    if first_number is None or operator is None or not current_expression:
        return 

    second_number = float(current_expression)
    result = 0

    if operator == '+':
        result = first_number + second_number
    elif operator == '-':
        result = first_number - second_number
    elif operator == '*':
        result = first_number * second_number
    elif operator == '/':
        if second_number == 0: 
            giris_alani.delete(0, tk.END)
            giris_alani.insert(0, "Hata")
            first_number = None 
            operator = None
            is_new_number = True
            return
        result = first_number / second_number
    
    giris_alani.delete(0, tk.END) 
    if result == int(result):
        giris_alani.insert(0, str(int(result)))
    else:
        giris_alani.insert(0, str(result))
    
    first_number = result 
    operator = None       
    is_new_number = True  


# Düğmeler
dugme_duzeni = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in dugme_duzeni:
    dugme = tk.Button(pencere, text=text, font=('Arial', 18), padx=20, pady=20)
    
    if text.isdigit() or text == '.': 
        dugme.config(command=lambda char=text: button_click(char))
    elif text in ['+', '-', '*', '/']: 
        dugme.config(command=lambda op=text: set_operator(op))
    elif text == '=': 
        dugme.config(command=calculate)

    dugme.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

temizle_dugmesi = tk.Button(pencere, text='C', font=('Arial', 18), padx=20, pady=20, bg='red', fg='white', command=clear_all)
temizle_dugmesi.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

for i in range(1, 6):
    pencere.grid_rowconfigure(i, weight=1)
pencere.mainloop()