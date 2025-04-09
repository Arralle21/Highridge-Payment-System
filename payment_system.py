#Submitted by: Abdullahi Mohamed Jibri
#Submitted Date 04-09-2025
import random
import csv
from datetime import datetime

class PaymentSystem:
    def __init__(self):
        self.workers = []
        self.payment_slips = []

    def generate_workers(self, num_workers=400):
        """Generate a dynamic list of workers with random attributes"""
        first_names = ["James", "John", "Robert", "Michael", "William",
                      "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
                     "Miller", "Davis", "Garcia", "Rodriguez", "Wilson"]
        genders = ["Male", "Female"]
        departments = ["Carpentry", "Masonry", "Plumbing", "Electrical", "Landscaping"]

        for i in range(num_workers):
            worker = {
                "id": f"EMP{1000 + i}",
                "first_name": random.choice(first_names),
                "last_name": random.choice(last_names),
                "gender": random.choice(genders),
                "department": random.choice(departments),
                "hours_worked": random.randint(30, 60),
                "hourly_rate": round(random.uniform(15.0, 50.0), 2
            )}
            self.workers.append(worker)

    def calculate_salary(self, hours, rate):
        """Calculate weekly salary with overtime pay"""
        regular_hours = min(hours, 40)
        overtime_hours = max(hours - 40, 0)
        return (regular_hours * rate) + (overtime_hours * rate * 1.5)

    def determine_employee_level(self, salary, gender):
        """Determine employee level based on salary and gender"""
        if 10000 < salary < 20000:
            return "A1"
        elif 7500 < salary < 30000 and gender == "Female":
            return "A5-F"
        return "B2"  # Default level

    def generate_payment_slips(self):
        """Generate payment slips for all workers"""
        try:
            for worker in self.workers:
                salary = self.calculate_salary(worker["hours_worked"], worker["hourly_rate"])
                level = self.determine_employee_level(salary, worker["gender"])

                payment_slip = {
                    "employee_id": worker["id"],
                    "name": f"{worker['first_name']} {worker['last_name']}",
                    "gender": worker["gender"],
                    "department": worker["department"],
                    "hours_worked": worker["hours_worked"],
                    "hourly_rate": worker["hourly_rate"],
                    "weekly_salary": round(salary, 2),
                    "employee_level": level,
                    "payment_date": datetime.now().strftime("%Y-%m-%d")
                }
                self.payment_slips.append(payment_slip)

        except Exception as e:
            print(f"Error generating payment slips: {str(e)}")

    def export_to_csv(self, filename="payment_slips.csv"):
        """Export payment slips to CSV file"""
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.payment_slips[0].keys())
                writer.writeheader()
                writer.writerows(self.payment_slips)
            print(f"Payment slips exported to {filename}")
        except Exception as e:
            print(f"Error exporting to CSV: {str(e)}")

    def run(self):
        """Run the entire payment system"""
        self.generate_workers()
        self.generate_payment_slips()
        self.export_to_csv()

if __name__ == "__main__":
    try:
        payment_system = PaymentSystem()
        payment_system.run()
        print("Payment slip generation completed successfully!")
    except Exception as e:
        print(f"An error occurred in the payment system: {str(e)}")

