from datetime import date
STAGES = ['novo']
def model_leads(name, company, email):
    '''MOdela/ estruturar um lead como um dict simples'''
    return{
        'name': name,
        'company': company,
        'email': email,
        'stage' : 'novo',
        'created' : date.today().isoformat()
    
    }