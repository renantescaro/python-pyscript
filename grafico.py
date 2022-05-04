from typing import List, Tuple
import matplotlib.pyplot as plt


class Grafico:
    def __init__(self, a:int, b:int, c:int) -> None:
        self.a :int = a
        self.b :int = b
        self.c :int = c


    def _gerar_valores(self) -> Tuple[List[int], List[int]]:
        valores_x = []
        valores_y = []
        for x in range(-5, 5):
            # a.X² + b.X + c
            resultado = (self.a*x**2) + (self.b*x) + (self.c)

            valores_x.append(x)
            valores_y.append(resultado)

        return valores_x, valores_y


    def executar(self):
        valores_x, valores_y = self._gerar_valores()

        fig, ax = plt.subplots()

        ax.plot(valores_x, valores_y, linewidth=2.0)

        print(f'valores_x:{valores_x}')
        print(f'valores_y:{valores_y}')

        ax.set(
            xlim=(0, 8),
            ylim=(0, 8),
            xticks=range(min(valores_x), max(valores_x)),
            yticks=range(min(valores_y), max(valores_y))
        )
        return fig
