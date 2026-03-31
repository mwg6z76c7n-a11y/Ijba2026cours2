import csv
from collections import Counter

def analyser_csv(file_path):
    service_counts = Counter()
    skill_counts = Counter()
    total_lieux = 0

    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                total_lieux += 1
                
                # 1. Analyse des services physiques/logistiques (colonne 'services')
                services = [s.strip() for s in row['services'].split(',') if s.strip()]
                for s in services:
                    service_counts[s] += 1
                
                # 2. Analyse des compétences et démarches (colonne 'niveau_service')
                niveaux = [n.strip() for n in row['niveau_service'].split(',') if n.strip()]
                for n in niveaux:
                    if '/' in n:
                        parts = n.split('/')
                        skill = parts[0]
                        level = parts[1] if len(parts) > 1 else ''
                        if level.lower() != 'non':
                            skill_counts[skill] += 1

        # Préparation des données pour le CSV
        resultats_csv = []
        
        print(f"--- ANALYSE DE L'INCLUSION NUMÉRIQUE (Total lieux : {total_lieux}) ---\n")
        
        print('--- SERVICES PHYSIQUES ET LOGISTIQUES ---')
        for s, count in service_counts.most_common():
            pourcentage = round(count/total_lieux*100)
            print(f'{s:<50} | {count} ({pourcentage}%)')
            resultats_csv.append(['Service Physique', s, count, f"{pourcentage}%"])

        print('\n--- COMPÉTENCES ET DÉMARCHES ACCOMPAGNÉES ---')
        for s, count in skill_counts.most_common():
            pourcentage = round(count/total_lieux*100)
            print(f'{s:<50} | {count} ({pourcentage}%)')
            resultats_csv.append(['Compétence/Démarche', s, count, f"{pourcentage}%"])

        # Écriture du fichier CSV
        output_file = 'frequences_inclusion.csv'
        with open(output_file, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Type', 'Service/Compétence', 'Nombre de lieux', 'Pourcentage'])
            writer.writerows(resultats_csv)
        
        print(f"\n[OK] Les résultats ont été enregistrés dans : {output_file}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_path}' est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    csv_filename = 'RAW_met_lieux_inclusion_numerique - RAW_met_lieux_inclusion_numerique.csv'
    analyser_csv(csv_filename)
