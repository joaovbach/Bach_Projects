class Partes:
    def __init__(self, pai, indiceX, indiceY) -> None:
        self.x = pai.x + (indiceX*40)
        self.y = pai.y + (indiceY*40)