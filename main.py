from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from banco import conectar_banco
from funcoes_tempo import calcular_tempo_restante, timedelta_to_str
from consulta import *
from datetime import datetime


class LoginScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class MeuAplicativo(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.editando = False  # Controla se o usuário está editando
        self.permissao = None  # Armazena a permissão do usuário logado
        self.usuario_id = None  # Inicialize o ID do usuário como None

    def build(self):
        return Builder.load_file("tela.kv")

    def on_start(self):
        """Inicia o loop de atualização quando o aplicativo inicia."""
        Clock.schedule_interval(self.atualizar_dados, 5)

    def logar(self, nome, senha):
        """Valida o login do usuário, define a permissão e armazena o ID do usuário."""
        conexao = conectar_banco()
        if conexao:
            try:
                cursor = conexao.cursor()
                query = "SELECT id, permissao FROM usuarios WHERE nome = %s AND senha = %s"
                cursor.execute(query, (nome, senha))
                resultado = cursor.fetchone()
                if resultado:
                    self.usuario_id, self.permissao = resultado
                    print(f"Login bem-sucedido! Usuário: {nome}, Permissão: {self.permissao}")

                    if nome == "convidado":
                        self.permissao = "visualizar_tudo"

                    elif nome == "portaria":
                        self.permissao = "visualizar_dia"

                    self.root.current = "menu"
                    self.carregar_dados()
                else:
                    print("Credenciais inválidas!")
            except Exception as e:
                print(f"Erro ao logar: {e}")
            finally:
                cursor.close()
                conexao.close()

    def carregar_dados(self):
        """Carrega os carros de acordo com a permissão e o usuário logado."""
        if self.editando:
            return  # Não carrega dados enquanto estiver editando

        conexao = conectar_banco()
        if not conexao:
            print("Erro ao conectar ao banco de dados.")
            return

        try:
            main_box = self.root.get_screen("menu").ids.main_box
            main_box.clear_widgets()

            if self.permissao == "visualizar_tudo":
                carros = buscar_carros_por_dia(conexao, "")
                for carro, placa, responsavel, horario_entrada, horario_saida, dia_semana, vaga in carros:
                    self.adicionar_linha_visualizacao(main_box, vaga, carro, placa, responsavel, horario_entrada,
                                                      horario_saida, dia_semana)

            elif self.permissao == "visualizar_dia":
                dia_ingles = datetime.now().strftime("%a")
                dia_atual = DIA_SEMANA_TRADUZIDO.get(dia_ingles, "").lower()
                carros = buscar_carros_por_dia(conexao, dia_atual)
                for carro, placa, responsavel, horario_entrada, horario_saida, dia_semana, vaga in carros:
                    self.adicionar_linha_visualizacao(main_box, vaga, carro, placa, responsavel, horario_entrada,
                                                      horario_saida, dia_semana)
            else:
                vagas_permitidas = buscar_vagas_por_usuario(conexao, self.usuario_id)
                if not vagas_permitidas:
                    print(f"O usuário {self.usuario_id} não possui vagas associadas.")
                    return

                for vaga in vagas_permitidas:
                    carros = buscar_carro_por_vaga(conexao, vaga)
                    if carros:
                        for id, carro, placa, responsavel, horario_entrada, horario_saida, dia_semana in carros:
                            if self.permissao == "editar":
                                self.adicionar_linha_edicao(id, main_box, vaga, carro, placa, responsavel,
                                                            horario_entrada, horario_saida, dia_semana)
                            else:
                                self.adicionar_linha_visualizacao(id, main_box, vaga, carro, placa, responsavel,
                                                                  horario_entrada, horario_saida, dia_semana)
        finally:
            conexao.close()

    def atualizar_dados(self, dt):
        """Atualiza os dados automaticamente em intervalos regulares."""
        if self.editando:
            print("Edição em andamento. Atualização pausada.")
            return
        print("Atualizando os dados...")
        self.carregar_dados()



    def adicionar_linha_visualizacao(self, main_box, vaga, carro, placa, responsavel, horario_entrada, horario_saida,
                                     dia_semana):
        """Adiciona uma linha para visualização."""
        horario_entrada_str = timedelta_to_str(horario_entrada) if horario_entrada else "00:00:00"
        horario_saida_str = timedelta_to_str(horario_saida) if horario_saida else "00:00:00"

        status = "LIBERADO" if horario_entrada_str == "00:00:00" and horario_saida_str == "00:00:00" else calcular_tempo_restante(horario_saida_str)

        linha = BoxLayout(size_hint_y=None, height=40, orientation="horizontal")
        linha.add_widget(Label(text=str(vaga)))
        linha.add_widget(Label(text=carro))
        linha.add_widget(Label(text=placa))
        linha.add_widget(Label(text=responsavel))
        linha.add_widget(Label(text=horario_entrada_str))
        linha.add_widget(Label(text=horario_saida_str))
        linha.add_widget(Label(text=dia_semana))

        label_status = Label(text=status)
        if status == "Expirado":
            label_status.color = (1, 0, 0, 1)
        elif status == "LIBERADO":
            label_status.color = (0, 1, 0, 1)
        linha.add_widget(label_status)

        main_box.add_widget(linha)

    def adicionar_linha_edicao(self, id,  main_box, vaga, carro, placa, responsavel, horario_entrada, horario_saida,
                               dia_semana):
        """Adiciona uma linha editável."""
        self.editando = True  # Pausa atualização
        horario_entrada_str = timedelta_to_str(horario_entrada) if horario_entrada else "00:00:00"
        horario_saida_str = timedelta_to_str(horario_saida) if horario_saida else "00:00:00"

        campos = {
            "vaga": Label(text=str(vaga)),
            "carro": TextInput(text=carro),
            "placa": TextInput(text=placa),
            "responsavel": TextInput(text=responsavel),
            "horario_entrada": TextInput(text=horario_entrada_str),
            "horario_saida": TextInput(text=horario_saida_str),
            "dia_semana": TextInput(text=dia_semana),
        }

        linha = BoxLayout(size_hint_y=None, height=40, orientation="horizontal")
        for key, widget in campos.items():
            linha.add_widget(widget)

        salvar_btn = Button(text="Salvar", size_hint_x=0.2)
        salvar_btn.bind(
            on_release=lambda btn: self.salvar_dados(
                id,
                vaga,
                campos["carro"].text,
                campos["placa"].text,
                campos["responsavel"].text,
                campos["horario_entrada"].text,
                campos["horario_saida"].text,
                campos["dia_semana"].text,
            )
        )
        salvar_btn.bind(on_release=self.retomar_atualizacao)
        linha.add_widget(salvar_btn)

        main_box.add_widget(linha)

    def retomar_atualizacao(self, *args):
        """Retoma a atualização global após salvar."""
        self.editando = False
        print("Edição concluída. Atualização retomada.")

    def salvar_dados(self, id,  vaga, carro, placa, responsavel, entrada, saida, dia):
        """Salva os dados modificados no banco."""
        if not self.validar_horario(entrada) or not self.validar_horario(saida):
            print("Erro: Horário inválido.")
            return

        conexao = conectar_banco()
        if conexao:
            try:
                cursor = conexao.cursor()
                query = """
                UPDATE carros
                SET carro = %s, placa = %s, responsavel = %s, horario_entrada = %s, horario_saida = %s, dia_semana = %s
                WHERE id = %s
                """
                cursor.execute(query, (carro, placa, responsavel, entrada, saida, dia, id))
                conexao.commit()
                print(f"Dados da vaga {vaga} atualizados com sucesso!")
            finally:
                cursor.close()
                conexao.close()
        self.retomar_atualizacao()

    def validar_horario(self, horario):
        """Valida se o horário está no formato HH:MM:SS."""
        try:
            datetime.strptime(horario, "%H:%M:%S")
            return True
        except ValueError:
            return False


MeuAplicativo().run()
