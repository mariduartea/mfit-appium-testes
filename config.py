
# Dados de Teste
test_data = {
    "email_personal": "abas@cesar.school",
    "senha_personal": "14051993",
    "nome_aluno": "ETA 2024",
    "email_aluno": "Testa@gmail.com",
    "modalidade": "Presencial",
    "data_nascimento": "11/12/1995",
    "whatsapp": "81995678900"}

# Locators
locators = {
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


}
