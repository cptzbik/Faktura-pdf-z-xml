from reportlab.lib import colors


class Styles:

    align_center = ('ALIGN', (0, 0), (-1, -1), 'CENTER')
    valign_middle = ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')
    align_left = ('ALIGN', (0, 0), (-1, -1), 'LEFT')

    @staticmethod
    def inner_grid(colors):
        return ('INNERGRID', (0, 0), (-1, -1), 0.25, colors)

    @staticmethod
    def box(colors):
        return ('BOX', (0, 0), (-1, -1), 0.25, colors)

    @staticmethod
    def background(colors):
        return ('BACKGROUND', (0, 0), (-1, -1), colors)

    @staticmethod
    def font_size(size):
        return ('FONTSIZE', (0, 0), (-1, -1), size)
