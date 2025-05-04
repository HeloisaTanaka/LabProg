#Crie um cadastro de alunos
#3 classe: aluno, curso, turma
#Métodos: adicionar alunos na turma, em cursos, inserir turma no curso

class Aluno:
    def __init__(self, nome, turma, n_matricula, media, serie):
        self.nome_completo = nome
        self.nome, self.sobrenome = self.nome_completo.split()
        self.turma = turma
        self.matricula = n_matricula
        self.media = media
        self.serie = serie

    def infos_aluno(self):
        print('Nome: ', self.nome)
        print('Sobrenome: ', self.sobrenome)
        print('Série: ', self.serie)
        print('Turma: ', self.turma)
        print('Media: ', self.media)
        print('Matrícula: ', self.matricula)
    
    def troca_turma(self, nova_turma):
        self.nova_turma = nova_turma
        self.turma = self.nova_turma
        return print('Turma: ', self.turma)
    
    def atualizacao_media(self, nova_media):
        self.nova_media = nova_media
        self.media = self.nova_media
        return print('Média: ', self.media)

class Curso:
    def __init__(self, curso, duracao, professor, horario, dia):
        self.curso = curso
        self.duracao = duracao
        self.professor = professor
        self.horario = horario
        self.dia = dia
    
    def infos_curso(self):
        print('Curso: ', self.curso)
        print('Duração: ', self.duracao)
        print('Professor: ', self.professor)
        print('Dias: ', self.dia)
        print('Horário: ', self.horario)

    def troca_professor(self, novo_prof):
        self.novo_prof = novo_prof
        self.professor = novo_prof
        return print('Professor:', self.professor)

class Turma:
    def __init__(self, n_turma, alunos, cursos):
        self.n_turma = n_turma
        self.alunos = alunos
        self.cursos = cursos

    def info_turma(self):
        print('Nº da turma: ', self.n_turma)
        print('Alunos: ', self.alunos)
        print('Cursos: ', self.cursos)

    def localizar_aluno(self, aluno_procurado):
        self.procurado = aluno_procurado
        for x in range(len(list(self.alunos))):
            if self.alunos[x] == self.procurado:
                return print (self.procurado, ' pertence à turma ', self.n_turma)           
        print(self.procurado, ' não pertence à turma ', self.n_turma)

    def adicionar_alunos(self, novo_aluno):
        self.novo_aluno = novo_aluno
        self.alunos.append(novo_aluno)
        print('Alunos: ', self.alunos)

    def tirar_aluno(self, aluno_retirado):
        self.aluno_retirado = aluno_retirado
        for x in range(len(list(self.alunos))):
            if self.alunos[x] == self.aluno_retirado:
                self.alunos.remove(self.alunos[x])
                return print ('Alunos: ', self.alunos)
                

    def adicionar_curso(self, novo_curso):
        self.novo_curso = novo_curso
        self.cursos.append(novo_curso)
        print('Cursos: ', self.cursos)

Aluno1 = Aluno('Mateus', 16, 610, 23985432, 7.9) 
Aluno1.infos_aluno()
Aluno1.troca_turma(614)
Aluno1.atualizacao_media(9.2)

Artes1 = Curso('Artes1', '70 horas', 'Nakashato', '13:15 - 14:50', 'Segunda-Feira')
Artes1.infos_curso()
Artes1.troca_professor('Claudete')

Turma1 = Turma(610, ['Ana Júlia', 'Agatha', 'Roberto', 'Felipe'], ['Artes', 'História', 'Geografia'])
Turma1.info_turma()
Turma1.localizar_aluno('Agatha')
Turma1.localizar_aluno('Cristiane')
Turma1.adicionar_alunos('Giovana')
Turma1.tirar_aluno('Felipe')
Turma1.adicionar_curso('Matemática')

