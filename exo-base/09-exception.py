##########################
# gestion des exceptions #
##########################
"""
Permet de gérer les erreurs grace à un bloc try catch
"""


class MonException (Exception):
    """
    Exception personnalisée pour le test
    """
    pass


try:
    response = int(input("Entrez un nombre : "))
    if response == 1:
        raise MonException("1 n'est pas valide")
    if response > 10:
        raise Exception("Le nombre est trop grand - c'est un piège")

except MonException as e:
    print(f"[ERROR] C'est une exception pour le test : {e}")
except ZeroDivisionError:
    print(f"[ERROR] Division par zéro impossible {e}")
except ValueError:
    print (f"[ERROR] Valeur incorrecte {e}")
except Exception as e:
    print(f"[ERROR] {e}")
finally:
    response = 0

