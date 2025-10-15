from stages import model_leads
import repo 
def add_lead():
    name = input('Nome:')
    company = input('Empresa:')
    email = input('Email:')
    repo.create_lead(model_leads(name, company, email))
    print('Lead add')
def list_leads():
    print('Lista Lead')




def main():
    while True:
        print_menu()
        op = input('Escolha:')
        if op == '1':
            add_lead()

        elif op == '2':
            list_leads()

        elif op == '3':
            print('Saindo do programa')
            break
        else:
            print('opcao invalida')
def print_menu():
    print('\n Mini CRM de Leads - (Adicionar/Listar)')
    print('[1] Adicionar lead')
    print('[2] Listar lead')
    print('[3] Sair do programa')

#main()

if __name__ == '__main__':                  
    main()
