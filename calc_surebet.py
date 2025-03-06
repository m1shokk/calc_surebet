import tkinter as tk
from tkinter import messagebox
from tkinter import font

def calculate_distribution():
    try:
        # Remplacer les virgules par des points pour la conversion
        x1 = float(entry_x1.get().replace(',', '.'))
        x2 = float(entry_x2.get().replace(',', '.'))
        
        # Проверяем, что коэффициенты положительные
        if x1 <= 0 or x2 <= 0:
            messagebox.showerror("Erreur", "Les coefficients doivent être positifs")
            return
            
        # Рассчитываем распределение
        total = 100.0
        bet1 = total / (1 + x1/x2)
        bet2 = total - bet1
        
        # Рассчитываем выигрыш
        win1 = bet1 * x1
        win2 = bet2 * x2
        
        # Показываем результаты в большом окне
        result_text = f"Распределение:\n\nНа {x1:.2f}: {bet1:.2f} €\nНа {x2:.2f}: {bet2:.2f} €\nВыигрыш для обоих: {max(win1, win2):.2f} €"
        # Создаем новое окно для результатов
        result_window = tk.Toplevel()
        result_window.title("Результаты расчета")
        result_window.geometry("500x300")
        result_window.configure(bg='#f0f0f0')
        
        # Добавляем текст с результатами
        result_label = tk.Label(result_window, text=result_text, 
                              font=font.Font(size=16), bg='#f0f0f0', fg='#333333')
        result_label.pack(expand=True, padx=20, pady=20)
        
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides (utilisez le point comme séparateur décimal)")

# Создаем главное окно с увеличенными размерами
root = tk.Tk()
root.title("Распределитель коэффициентов")
root.geometry("600x400")  # Делаем окно еще больше
root.configure(bg='#f0f0f0')  # Добавляем приятный фоновый цвет

# Определяем шрифты после создания root
LARGE_FONT = font.Font(size=16)
TITLE_FONT = font.Font(size=18, weight='bold')

# Создаем фрейм для содержимого с отступами
content_frame = tk.Frame(root, bg='#f0f0f0', padx=20, pady=20)
content_frame.pack(expand=True)

# Заголовок
title_label = tk.Label(content_frame, text="Калькулятор коэффициентов", 
                      font=TITLE_FONT, bg='#f0f0f0', fg='#333333')
title_label.grid(row=0, column=0, columnspan=2, pady=20)

label_x1 = tk.Label(content_frame, text="Коэффициент 1:", 
                    font=LARGE_FONT, bg='#f0f0f0', fg='#333333')
label_x1.grid(row=1, column=0, padx=15, pady=15, sticky='e')

entry_x1 = tk.Entry(content_frame, font=LARGE_FONT, width=15)
entry_x1.grid(row=1, column=1, padx=15, pady=15)

label_x2 = tk.Label(content_frame, text="Коэффициент 2:", 
                    font=LARGE_FONT, bg='#f0f0f0', fg='#333333')
label_x2.grid(row=2, column=0, padx=15, pady=15, sticky='e')

entry_x2 = tk.Entry(content_frame, font=LARGE_FONT, width=15)
entry_x2.grid(row=2, column=1, padx=15, pady=15)

calculate_button = tk.Button(content_frame, text="Рассчитать", 
                           command=calculate_distribution, 
                           font=LARGE_FONT,
                           bg='#4CAF50', fg='white',
                           padx=20, pady=10,
                           relief=tk.RAISED)
calculate_button.grid(row=3, column=0, columnspan=2, pady=30)

# Запускаем главный цикл
root.mainloop()
