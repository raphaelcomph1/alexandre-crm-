# from stages import model_leads
from model import lead
from stages import default_stage
from repo import LeadRepository

lead_backend = LeadRepository()


def add_lead():
    name = input('Nome:')
    company = input('Empresa:')
    email = input('Email:')
    Lead = lead(name, company, email, default_stage)
    modeled_lead = Lead.model_leads()
    lead_backend.create_lead(modeled_lead)

    print('Lead add')
def list_leads():
    leads = lead_backend.read_lead()
    if not leads:
        print('Nenhum lead ainda')
        return
    
    print(f'\n## | {'Name' :<20} | {'Company':<20} | {'Email' :<20}')
    for i, lead in enumerate(leads):
        print(f'{i:02d} | {lead['name'] :<20} | {lead['company']:<20} | {lead['email'] :<20}')

def search_leads():
    user_search = input('Buscar por: ').strip().lower()
    if not user_search:
        print('Consulta vazia')
        return
    
    leads = lead_backend.read_lead()
    results = []

    for i, lead  in enumerate(leads):
        lead_str = f'{lead['name']},{lead['company']},{lead['email']}'.lower()
        if user_search in lead_str:
            results.append(lead)

    if not results:
        print('Nada encontrado')
        return
    
    print(f'\n## | {'Name' :<20} | {'Company':<20} | {'Email' :<20}')
    for i, lead in enumerate(results):
        print(f'{i:02d} | {lead['name'] :<20} | {lead['company']:<20} | {lead['email'] :<20}')
    
def export_leads():    
    path_csv = lead_backend.export_csv()
    if path_csv is None:
        print('Não foi possivel executar os leads como CSV')
    else:
        print(f'Arquivo exportado como CSV para: {path_csv}')
    
def main():
    while True:
        print_menu()
        op = input('Escolha:')
        if op == '1':
            add_lead()

        elif op == '2':
            list_leads()

        elif op == '3':
            search_leads()
            
        elif op == '4':
            export_leads()

        elif op == '5':
            print('Saindo do programa')
            break
        else:
            print('opcao invalida')
def print_menu():
    print('\n Mini CRM de Leads - (Adicionar/Listar)')
    print('[1] Adicionar lead')
    print('[2] Listar Lead')
    print('[3] Buscar lead por(nome/empresa/email)')
    print('[4] Exportar lead')    
    print('[5] Fechar programa')

#main()

if __name__ == '__main__':                  
    main()
