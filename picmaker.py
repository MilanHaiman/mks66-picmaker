file = open('output.ppm','w')

file.write('P3\n')
file.write('500  500\n')
file.write('255\n')

maxd=250*(2**0.5)

for row in range(500):
	for col in range(500):
		d = ((row-250)**2+(col-250)**2)**0.5
		R = int(d*255/maxd)
		B = int(col / 500. * 255)
		G = int(row / 500. * 255)
		file.write(str(R) + " " + str(G) + " " + str(B) + " ")
	file.write('\n')
file.close()
