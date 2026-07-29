# Write a function salary(bonus).
#
# -   The outer function receives the bonus amount.
# -   The inner function receives the employee’s basic salary.
# -   Print the total salary after adding the bonus.
# -   Return the inner function.
def salary(bonus):
    def emp(basic_salary):
        total=bonus+basic_salary
        print(total)
        return total
    return emp
s1=salary(15000)
s1(35000)