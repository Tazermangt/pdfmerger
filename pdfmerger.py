from pypdf import PdfMerger
import os

merger = PdfMerger()


chemin = input('Entrer le chemin du dossier comprenant les pdf\n')


fichiers = os.listdir(chemin)

merger.append(chemin + "\\" + "export.pdf")

for i in range(len(fichiers) - 1):
    merger.append(chemin + "\\" + "export (%i).pdf" % (i + 1))

chemin_split = chemin.split('\\')
merger.write(chemin_split[len(chemin_split) - 1] + ".pdf")
merger.close()

print("Ficher créer :)")
