class usuario:

    def __init__(self, idUsuario, nombre, apellido, correo, telefono, fechaRegistro):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono
        self.fechaRegistro = fechaRegistro

    def to_json(self):
        return self.__dict__

class infraccion:

    def __init__(self, idInfraccion, tipoInfraccion, descripcion, multa, ):
        self.idInfraccion = idInfraccion
        self.tipoInfraccion = tipoInfraccion
        self.descripcion = descripcion
        self.multa = multa
    
    def to_json(self):
        return self.__dict__
    
class comparendo:
    def __init__(self, numComparendo, idUsuario, idInfraccion, fecha, hora, lugar):
        self.numComparendo = numComparendo
        self.idUsuario = idUsuario
        self.idInfraccion = idInfraccion  
        self.fecha = fecha
        self.hora = hora
        self.lugar = lugar

    def to_json(self):
        return self.__dict__
