import tkinter as tk

pencere = tk.Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("300x400")

giris_alani = tk.Entry(pencere, width=20, font=('Arial', 24), bd=5, justify='right')
giris_alani.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
giris_alani.insert(0, "0")

for i in range(4):
    pencere.grid_columnconfigure(i, weight=1)


#Düğmeler

dugme_duzeni = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in dugme_duzeni:
    dugme = tk.Button(pencere, text=text, font=('Arial', 18), padx=20, pady=20)
    dugme.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

#Clear Tuşu
temizle_dugmesi = tk.Button(pencere, text='C', font=('Arial', 18), padx=20, pady=20, bg='red', fg='white')
temizle_dugmesi.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

for i in range(1, 6):
    pencere.grid_rowconfigure(i, weight=1)


pencere.mainloop()