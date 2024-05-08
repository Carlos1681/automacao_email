import PySimpleGUI as sg

sg.theme('reddit')

layout = [
    [sg.Text('Email'), sg.Input(key='email')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.FolderBrowse('Escolher Pasta Anexos', target='pasta_anexos'), sg.Input(key='pasta_anexos')],
    [sg.FolderBrowse('Escolher Pasta Planilhas', target='pasta_planilhas'), sg.Input(key='pasta_planilhas')],
    [sg.Button('Salvar')]
]

janela = sg.Window('Principal', layout=layout)

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Salvar':
        email = values['email']
        senha = values['senha']
        caminho_pasta_anexos = values['pasta_anexos']
        caminho_pasta_planilhas = values['pasta_planilhas']
