from db import c, conn


"""
PK - Primary Key
"""

# The main class of an employee


class Employee(object):
    def __init__(self, name, surname, age, pk=None):
        self.id = pk
        self.name = name
        self.surname = surname
        self.age = age

    def __repr__(self):
        return "<Employee {} {}, {} years old>".format(self.name, self.surname, self.age)

    def __eq__(self, other):
        return self.age == other.age

    @classmethod
    def get(cls, pk):
        result = c.execute("SELECT * FROM employee WHERE id = ?", (pk,))
        values = result.fetchone()
        if values is None:
            return None
        employee = Employee(values["name"], values["surname"], values["age"], values["id"])
        return employee

    @classmethod
    def get_list(cls, **kwargs):
        conditions = []
        values = ()

        for key, value in kwargs.items():
            conditions.append(f"{key} = ?")
            values += (value,)

        base = "SELECT * FROM employee"

        if conditions:
            base += " WHERE " + " AND ".join(conditions)

        result = c.execute(base, values)
        employees = [cls(row["name"], row["surname"], row["age"], row["id"]) for row in result.fetchall()]

        return employees

    def update(self):
        c.execute("UPDATE employee SET name = ?, surname = ?, age = ? WHERE id = ?",
                  (self.name, self.surname, self.age, self.id))

    def create(self):
        c.execute("INSERT INTO employee (name, surname, age) VALUES (?, ?, ?)", (self.name, self.surname, self.age))
        self.id = c.lastrowid

    def delete(self):
        if self.id is None:
            return
        c.execute("DELETE FROM employee WHERE id = ?", (self.id,))
        self.id = None

    def save(self):
        if self.id is not None:
            self.update()
        else:
            self.create()
        return self
