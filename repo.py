# repo se comporta como backend 

from pathlib import Path
import json, csv 

class LeadRepository:

    def __init__(self):
        self.DATA_DIR = Path(__file__).resolve().parent / 'data'
        self.DATA_DIR.mkdir(exist_ok= True)
        self.DB_PATH = self.DATA_DIR / 'leads.json'

    def _load(self):
        if not self.DB_PATH.exists():
            return []
        try:
            return json.loads(self.DB_PATH.read_text(encoding='utf-8'))
        except json.JSONDecodeError:
            return []
            
    def _save(self, leads):
        self.DB_PATH.write_text(json.dumps(leads, ensure_ascii = False, indent=2), encoding= 'utf-8')
    

    #aq vc criaria sua rota para api
    def create_lead(self, lead_dict):
        leads_loaded = self._load()  #array vazio
        leads_loaded.append(lead_dict)
        self._save(leads_loaded)

    def read_lead(self):
        return self._load()

    def export_csv(self):
        path_csv = self.DATA_DIR/'lead.csv'
        leads = self._load()
        try:
            with path_csv.open('w', newline='', encoding= 'utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['name', 'company', 'email', 'stage', 'created'])
                writer.writeheader()
                for lead in leads:
                    writer.writerow(lead)
            return path_csv
        except PermissionError:
        #caso o arquivo esteja aberto igual o ppt
            return None
                                    