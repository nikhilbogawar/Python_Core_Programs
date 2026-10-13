# PROJECT 1: TRANSACTION DATA PIPELINE
# 1. Read transactions.txt line by line
# 2. Validate each row
# 3. Write valid rows to clean.txt
# 4. Write invalid rows with reason to error.log
# 5. Use flush() for logs
# 6. Generate report.txt with:
#    - Total Records
#    - Valid Records
#    - Invalid Records
#    - Total Revenue
#    - Category-wise Revenue
# 7. Use seek() or tell() somewhere in the program

def validate_row(row):
    """Validate a transaction row and return (is_valid, reason)."""
    parts=row.strip().split(",")
    if len(parts)!=3:
        return False, "Invalid number of fields"
    user_id, amount, category = parts
    if amount=="":
        return False, "Missing amount"
    if not amount.isdigit():
        return False, "Non-numeric amount"
    if int(amount)<0:
        return False, "Negative amount"
    return True, ""

def process_transactions():
    total_records=0
    valid_records=0
    invalid_records=0
    total_revenue=0
    category_revenue={}

    with open("transactions.txt", "r") as infile, \
        open("clean.txt","w") as cleanfile, \
        open("error.log","w") as errorfile:
        header=infile.readline()
        print("Header skipped:",header.strip())

        print("Cursor position after header:",infile.tell())
        for line in infile:
            total_records+=1
            is_valid,reason=validate_row(line)
            if is_valid:
                cleanfile.write(line)
                valid_records+=1
                _, amount, category=line.strip().split(",")
                amount=float(amount)
                total_revenue+=amount
                category_revenue[category]=(category_revenue.get(category,0)+amount)
            else:
                errorfile.write(f"{line.strip()} -> {reason}\n")
                errorfile.flush()
                invalid_records+=1
    with open("report.txt","w") as report:
        report.write(f"Total Records: {total_records}\n")
        report.write(f"Valid Records: {valid_records}\n")
        report.write(f"Invalid Records: {invalid_records}\n")
        report.write(f"Total Revenue: {total_revenue}\n\n")
        report.write("Category-wise Revenue:\n")
        for cat, rev in category_revenue.items():
            report.write(f"{cat}: {rev}\n")
process_transactions()