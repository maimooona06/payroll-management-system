from tkinter import *

class EmployeeSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1350x750+100+50")
        self.root.config(bg="white")

        title = Label(self.root, text="Employee Payroll Management System", font=("times new roman", 30, "bold"),
                      bg="#262626", fg="white", anchor="w", padx=10)
        title.place(x=0, y=0, relwidth=1)

        #============== Frame1: Employee Details ==============================
        Frame1 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame1.place(x=10, y=70, width=750, height=660)

        title2 = Label(Frame1, text="Employee Details", font=("times new roman", 20, "bold"),
                       bg="lightgray", fg="black", anchor="w", padx=10)
        title2.place(x=0, y=0, relwidth=1)

        y_base = 50
        y_gap = 50

        # Employee Information
        labels = ["Employee ID", "Employee Code", "Designation", "Name", "Contact", "Location",
                  "Per Hour", "Per Day", "Hours Worked", "Bonus", "Deduction"]
        self.entries = {}

        for i, label in enumerate(labels):
            lbl = Label(Frame1, text=label, font=("times new roman", 20), bg="white", fg="black")
            lbl.place(x=10, y=y_base + y_gap * i)
            entry = Entry(Frame1, font=("times new roman", 15), bg="lightyellow", fg="black")
            entry.place(x=200, y=y_base + y_gap * i + 5, width=200)
            self.entries[label] = entry

        #============== Frame2: Salary Details =====================
        Frame2 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame2.place(x=770, y=70, width=580, height=300)

        lbl_total_payment = Label(Frame2, text="Total Payment", font=("times new roman", 20), bg="white", fg="black")
        lbl_total_payment.place(x=10, y=30)
        self.txt_total_display = Entry(Frame2, font=("times new roman", 15), bg="lightyellow", fg="black", state='readonly')
        self.txt_total_display.place(x=200, y=35, width=200)

        btn_calculate = Button(Frame2, text="Calculate", font=("times new roman", 15), bg="#4caf50", fg="white", command=self.calculate_total_payment)
        btn_calculate.place(x=420, y=35, width=120)

        btn_clear = Button(Frame2, text="Clear", font=("times new roman", 15), bg="#f44336", fg="white", command=self.clear_fields)
        btn_clear.place(x=420, y=85, width=120)

        #============== Frame3: Placeholder for Payslip or Summary =============
        Frame3 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame3.place(x=770, y=380, width=580, height=300)

    def calculate_total_payment(self):
        try:
            hours = float(self.entries["Hours Worked"].get())
        except ValueError:
            hours = 0.0

        try:
            per_hour = float(self.entries["Per Hour"].get())
        except ValueError:
            per_hour = 0.0

        try:
            bonus = float(self.entries["Bonus"].get())
        except ValueError:
            bonus = 0.0

        try:
            deduction = float(self.entries["Deduction"].get())
        except ValueError:
            deduction = 0.0

        total = (hours * per_hour) + bonus - deduction
        self.txt_total_display.config(state='normal')
        self.txt_total_display.delete(0, END)
        self.txt_total_display.insert(0, f"{total:.2f}")
        self.txt_total_display.config(state='readonly')

    def clear_fields(self):
        for entry in self.entries.values():
            entry.delete(0, END)
        self.txt_total_display.config(state='normal')
        self.txt_total_display.delete(0, END)
        self.txt_total_display.config(state='readonly')

# Create and run the app
if __name__ == "__main__":
    root = Tk()
    app = EmployeeSystem(root)
    root.mainloop()
