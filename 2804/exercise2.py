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
    
    def setTurma(self, nova_turma):
        self.turma = nova_turma
    
    def setMedia(self, nova_media):
        self.media = nova_media
    
    def setSerie(self, nova_serie):
        self.serie = nova_serie
    
    def getNome(self):
        return self.nome_completo
    
    def getSobrenome(self):
        return self.sobrenome
    
    def getTurma(self):
        return self.turma
    
    def getN_matricula(self):
        return self.matricula
    
    def getMedia(self):
        return self.media
    
    def getSerie(self):
        return self.serie

class Curso:
    def __init__(self, nome, duracao, professor, horario, dia):
        self.nome = nome
        self.duracao = duracao
        self.professor = professor
        self.horario = horario
        self.dia = dia
    
    def infos_curso(self):
        print('Curso: ', self.nome)
        print('Duração: ', self.duracao)
        print('Professor: ', self.professor)
        print('Dias: ', self.dia)
        print('Horário: ', self.horario)

    def setProfessor(self, novo_prof):
        self.professor = novo_prof

    def setProfessor(self, novo_duracao):
        self.duracao = novo_duracao

    def setProfessor(self, novo_dia):
        self.dia = novo_dia

    def setProfessor(self, novo_horario):
        self.horario = novo_horario

    def getNome(self):
        return self.nome
    
    def getDuracao(self):
        return self.duracao
    
    def getProfessor(self):
        return self.professor
    
    def getHorario(self):
        return self.horario
    
    def getDia(self):
        return self.dia

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
        for x in range(len(list(self.alunos))):
            if self.alunos[x] == aluno_procurado:
                return print (aluno_procurado, ' pertence à turma ', self.n_turma)           
        print(aluno_procurado, ' não pertence à turma ', self.n_turma)

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

Aluno1 = Aluno('Mateus Miranda', 610, 23985432, 7.9, 2) 
Aluno1.infos_aluno()
Aluno1.setTurma(614)
Aluno1.setMedia(9.2)
Aluno1.infos_aluno()

Artes1 = Curso('Artes1', '70 horas', 'Nakashato', '13:15 - 14:50', 'Segunda-Feira')
Artes1.infos_curso()
Artes1.setProfessor('Claudete')

Turma1 = Turma(610, ['Ana Júlia', 'Agatha', 'Roberto', 'Felipe'], ['Artes', 'História', 'Geografia'])
Turma1.info_turma()
Turma1.localizar_aluno('Agatha')
Turma1.localizar_aluno('Cristiane')
Turma1.adicionar_alunos('Giovana')
Turma1.tirar_aluno('Felipe')
Turma1.adicionar_curso('Matemática')

