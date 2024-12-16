
# Dados de Teste
test_data = {
    "email_personal": "mrda@cesar.school",
    "senha_personal": "14051997",
    "nome_aluno": "Bolinha 123",
    "email_aluno": "Testa@gmail.com",
    "modalidade": "Presencial",
    "data_nascimento": "11/12/1995",
    "whatsapp": "81995678900",
    "nome_rotina": "bolinha"
}

# Locators
locators = {
    "entrar_novamente": 'new UiSelector().text("Entrar novamente")',
    "personal_opt": 'new UiSelector().text("Sou personal trainer")',
    "email_personal": 'new UiSelector().className("android.widget.EditText").instance(0)',
    "senha_personal": 'new UiSelector().resourceId("hs-toggle-password")',
    "btn_login": 'new UiSelector().text("Entrar")',
    "add_novo_aluno": f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{"Adicionar alunos"}"))',
    "nome_aluno": 'new UiSelector().className("android.widget.EditText").instance(0)',
    "email_aluno": 'new UiSelector().className("android.widget.EditText").instance(1)',
    "selecionar_grupo": 'new UiSelector().className("android.view.View").instance(13)',
    "modalidade_opt": f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{test_data["modalidade"]}"))',
    "data_nascimento": 'new UiSelector().className("android.widget.EditText").instance(1)',
    "whatsapp": 'new UiSelector().text("+55 ")',
    "selecionar_genero": 'new UiSelector().text("Selecione").instance(0)',
    "genero_opt": 'new UiSelector().text("Feminino")',
    "selecionar_anamnese": 'new UiSelector().text("Selecione").instance(0)',
    "anamnese_opt": 'new UiSelector().text("Não")',
    "selecionar_bloqueio": 'new UiSelector().text("Selecione")',
    "bloqueio_opt": 'new UiSelector().text("Não")',
    "btn_salvar": 'new UiSelector().text("Salvar")',
    "fechar_popup": 'new UiSelector().text("Fechar")',
    "nome_cabecalho": f'new UiSelector().text("{test_data["nome_aluno"]}")',
    "modalidade_cabecalho": f'new UiSelector().text("{test_data["modalidade"]}")',
    "alunos_cadastrados": f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{"Alunos"}"))',
    "aluno_inserido": f'new UiSelector().text("{test_data["nome_aluno"]}")',
    "btn_opcoes": 'new UiSelector().text("Opções")',
    "btn_excluir_aluno": 'new UiSelector().text("Excluir aluno")',
    "msg_aluno_excluido": 'new UiSelector().text("Esse aluno foi excluído.")',

    # locators nova rotina
    "biblioteca_treino": f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{"Biblioteca de treinos"}"))',
    "adicionar_button": 'new UiSelector().className("android.widget.Button").text("Adicionar")',
    "nova_rotina_button": 'new UiSelector().description("Nova Rotina")',
    "comece_agora":'new UiSelector().text("Comece agora")',
    "adicionar_novo_treino": 'new UiSelector().text("Adicionar novo treino")',
    "nome_rotina_input": "new UiSelector().className(\"android.widget.EditText\").instance(0)",
    "tipo_treino": "new UiSelector().text(\"Dia da Semana - Ex: Segunda, Terça ...\")",
    "tipo_treino_popup": "new UiSelector().text(\"Dia da Semana - Ex: Segunda, Terça ...\")",
    "objetivo": "new UiSelector().className(\"android.view.View\").instance(30)",
    "hipertrofia_option": "new UiSelector().text(\"Hipertrofia\")",
    "dificuldade": "new UiSelector().className(\"android.view.View\").instance(32)",
    "adaptacao_option": "new UiSelector().text(\"Adaptação\")",
    "salvar_button": f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{"Salvar"}"))',
    "rotina_criada": f'new UiSelector().text("{test_data["nome_rotina"]}")',
    "voltar_button": 'new UiSelector().text("Voltar")',
    "opcoes_button": 'new UiSelector().text("").instance(0)',
    "excluir_button": 'new UiSelector().text("Excluir")',
    "pop_up_confirmacao": 'new UiSelector().text("Sim, excluir")'
}
