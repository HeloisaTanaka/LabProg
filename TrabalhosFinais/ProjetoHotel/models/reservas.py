class Reserva:
    def __init__(self, id, id_hospede, numero_quarto, data_checkin, data_checkout, stt_reserva, valor):
        self._id = id
        self._hospede = id_hospede
        self._numQuarto = numero_quarto
        self._dataCheckin = data_checkin
        self._dataCheckout = data_checkout
        self._sttReserva = stt_reserva
        self._valor = valor

    @property
    def id(self):
        return self._id
    
    @property
    def hospede(self):
        return self._hospede
    
    @property
    def quarto(self):
        return self._numQuarto
    
    @property
    def checkin(self):
        return self._dataCheckin
    
    @property
    def checkout(self):
        return self._dataCheckout
    
    @property
    def status(self):
        return self._sttReserva
    
    @property
    def valor(self):
        return self._valor
    
    @property
    def data(self):
        reserva = {
            'id': self.id,
            'hospede': self.hospede,
            'numero': self._numQuarto,
            'checkin': self.checkin,
            'chackout': self.checkout,
            'status': self.status,
            'valor': self.valor
        }
        return reserva

Reservas_lista = []

def addReserva(novaReserva):
    Reservas_lista.append(novaReserva)

def searchReservaById(id):
    for reserva in Reservas_lista:
        if reserva.id == id:
            return reserva.data
    return False

def deleteReserva(id):
    for reserva in Reservas_lista:
        if reserva.id == id:
            Reservas_lista.remove(reserva)
            return True
    return False

def updateReserva(id, campo, valor):
    for reserva in Reservas_lista:
        if reserva.id == id:
            setattr(reserva, campo, valor)
            return True
    return False

        