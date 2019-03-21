int etiquetafalsa(int *red, int *historial, int S1, int S2, int i)
{
	int minimo,maximo;

	while (*(historial+S1) < 0)
		S1 = -(*(historial+S1));

	while (*(historial+S2) < 0)
		S2 = -(*(historial+S2));
//ahora tengo la etiqueta verdadera de mis vecinos
//quiero quedarme con la menor

	if(S1<S2)
	{
	minimo = S1;
	maximo = S2;
	}
	else 
	{
	minimo = S2;
	maximo = S1;
	}

//le asigno la menor de las etiquetas
	*(red+i) = minimo;
	*(historial+maximo) = -minimo; //los que antes eran el valor max ahora son el min pero falso (por eso el -) //este queda mal igual si S1=S2
	*(historial+minimo) = minimo; // esto es por las dudas, ya debería valer mínimo
	// ademas la ultima linea te salva en el caso S1=S2

}

int corregir //tiene que ser un for que corrija las etiquetas al final de todo
