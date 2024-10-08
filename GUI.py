import tkinter as tk
from tkinter import messagebox
import math

# Hàm giải phương trình bậc hai
def giai_pt_bac_hai():
    try:
        # Lấy giá trị từ các ô nhập
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Kiểm tra nếu a = 0 thì không phải phương trình bậc hai
        if a == 0:
            messagebox.showerror("Lỗi", "Hệ số a phải khác 0")
            return
        
        # Tính delta
        delta = b**2 - 4*a*c
        
        # Tìm nghiệm dựa trên giá trị của delta
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            messagebox.showinfo("Kết quả", f"Phương trình có hai nghiệm:\n x1 = {x1}\n x2 = {x2}")
        elif delta == 0:
            x = -b / (2 * a)
            messagebox.showinfo("Kết quả", f"Phương trình có nghiệm kép: x = {x}")
        else:
            messagebox.showinfo("Kết quả", "Phương trình vô nghiệm (Delta < 0)")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")

# Tạo cửa sổ GUI
root = tk.Tk()
root.title("Giải phương trình bậc 2")

# Label và Entry cho hệ số a
label_a = tk.Label(root, text="Hệ số a:")
label_a.grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

# Label và Entry cho hệ số b
label_b = tk.Label(root, text="Hệ số b:")
label_b.grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

# Label và Entry cho hệ số c
label_c = tk.Label(root, text="Hệ số c:")
label_c.grid(row=2, column=0)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1)

# Nút bấm để giải phương trình
solve_button = tk.Button(root, text="Giải", command=giai_pt_bac_hai)
solve_button.grid(row=3, column=0, columnspan=2)

# Chạy giao diện
root.mainloop()
