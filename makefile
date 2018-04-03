graficamona.pdf: resalbum.txt graficamonas.py
	python graficamonas.py
resalbum.txt: album
	./album > resalbum.txt
album: album.cpp
	c++ album.cpp -o album
