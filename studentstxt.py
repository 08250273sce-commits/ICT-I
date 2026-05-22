filename = "student.txt"

try:
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    if not lines:
        print("No student records found in the file.")
    else:
        print("Student IDs:")
        for line in lines:
            parts = [part.strip() for part in line.replace(";", ",").split(",") if part.strip()]
            student_id = None
            for part in parts:
                if part.isdigit():
                    student_id = part
                    break
            if student_id is None and parts:
                student_id = parts[0]
            if student_id:
                print(student_id)
            else:
                print("Unable to determine student ID for line:", line)

except FileNotFoundError:
    print(f"File not found: {filename}")
except Exception as error:
    print("Unexpected error:", error)
finally:
    print("Completed.")
