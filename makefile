all:
	python picmaker.py
	convert output.ppm output.png

clean:
	rm *.ppm *.png