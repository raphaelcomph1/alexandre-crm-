from datetime import date

class lead:
    def __init__(self, name, company, email, stage):
        self.name = name
        self.company = company
        self.email = email
        self.stage = stage
        self.created = date.today().isoformat()


    def model_leads(self):
        '''MOdela/ estruturar um lead como um dict simples'''
        return{
            'name': self.name,
            'company': self.company,
            'email': self.email,
            'stage' : self.stage,
            'created' : self.created
        
        }