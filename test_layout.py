from bright import *


ui = column(
        well('bollinger'),
        row(well('sliders'), well('plot')),
        row(well('p1'), well('p2'), well('p3')),
    )


print(head()+ui)


show(ui)
