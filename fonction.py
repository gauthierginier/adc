import sqlite3
import sys


def competences_apprenant(cursor,apprenant):
    res = []
    cursor.execute("""SELECT Prenom,
    Nom, Compétences
    From Apprenants WHERE Prenom = ?""",
    (apprenant,))

    for row in cursor.fetchall():
        res.append((dict(row)))

    return res


def competences(cursor, num_id):
    res = []
    cursor.execute("""SELECT * From
    Compétences WHERE id= ?""",
    (num_id,))

    for row in cursor.fetchall():
        res.append((dict(row)))

    return res



def main():
    conn = sqlite3.connect('promo_simplon.db')
    c = conn.cursor()
    c.row_factory = sqlite3.Row
    competences_apprenant(c, "Gauthier")
    competences(c,"2")



if __name__ == "__main__":
    sys.exit(main())