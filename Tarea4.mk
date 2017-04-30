Resultados_hw4.pdf: Resultados_hw4.tex imagenes.pdf
	pdflatex Resultados_hw4.pdf

imagenes.pdf: Plots_Temperatura.py
	python Plots_Temperatura.py
