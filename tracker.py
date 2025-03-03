from datetime import datetime

def write_process():
    today = datetime.now().strftime("%d-%m-%Y")
    weight = input("Your Weight (kg): ")
    height = input("Your Height (cm): ")
    filename = "myprocess.txt"
    with open(filename, "a") as f:
        f.write(f"{today} // Weight: {weight} // Height: {height}\n")
        f.write("-" * 55 + "\n")

    print(f"Your height and weight data have been successfully entered to {filename}")
    
write_process()
