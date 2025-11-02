from fpdf import FPDF

class PDFGenerator:
    def __init__(self):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def add_title_page(self, difficulty):
        self.pdf.add_page()
        self.pdf.set_font('Arial', 'B', 16)  # Titre plus petit
        self.pdf.cell(0, 50, f'{difficulty.capitalize()} Sudoku Puzzles', ln=True, align='C')  # Hauteur réduite

    def add_sudoku_to_pdf(self, sudoku, puzzle_num, difficulty, offset_y, title_suffix="Sudoku Puzzle"):
        self.pdf.set_font('Arial', 'B', 12)  # Titre de puzzle plus petit
        self.pdf.set_xy(0, offset_y - 10)
        self.pdf.cell(210, 8, f'{difficulty.capitalize()} {title_suffix} #{puzzle_num}', ln=True, align='C')
        self.pdf.set_font('Arial', 'B', 14)  # chiffres du sudoku plus grands
        # Taille de cellule de 2 cm = 20 mm
        cell_size = 20
        offset_x = (210 - 9 * cell_size) / 2  # Centrer horizontalement

        for i in range(9):
            for j in range(9):
                self.pdf.set_xy(offset_x + j * cell_size, offset_y + i * cell_size)
                value = str(sudoku[i, j]) if sudoku[i, j] != 0 else ""
                self.pdf.set_line_width(0.2)  # Traits fins
                self.pdf.cell(cell_size, cell_size, value, border=1, align='C')

        # Traits épais pour les blocs de 3x3, plus fins
        self.pdf.set_line_width(0.5)
        for i in range(0, 10, 3):
            self.pdf.line(offset_x + i * cell_size, offset_y, offset_x + i * cell_size, offset_y + 9 * cell_size)
            self.pdf.line(offset_x, offset_y + i * cell_size, offset_x + 9 * cell_size, offset_y + i * cell_size)

    def generate_puzzles_pdf(self, puzzles, difficulty, is_answer=False):
        self.add_title_page(difficulty if not is_answer else difficulty + " Answers")
        total_puzzles = len(puzzles)
        for i in range(total_puzzles):
            self.pdf.add_page()
            # Un puzzle par page pour éviter les débordements
            self.add_sudoku_to_pdf(puzzles[i][1] if is_answer else puzzles[i][0], i + 1, difficulty, offset_y=30, title_suffix="Solution" if is_answer else "Sudoku Puzzle")

    def save_pdf(self, output_file):
        self.pdf.output(output_file)
        print(f"PDF saved as: {output_file}")
