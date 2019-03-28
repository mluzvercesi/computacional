int main (int argc, char *argv[])
{for (i=0; i<27000; i++)
	{ //blabla estadistica
	poblar(red, dim);
	clasificar(red, dim);
	percola(red, dim);
	m=masa(red, dim);
	}
return 0;
}


clasificar(int *red, int dim)
{
//falta i=0 que es el mas facil
for (i=1; i<dim; i++) //empieza en i=1 porque i=0 es aparte
	{
	actualizar(red+i, historial, s, frag)
	//red+i es el elemento actual: red[i] o *(red+i)
	}
for (i=1; i<dim; i++)
	{
	actualizar(red+dim*i, historial, s, frag)
	for (j=1; j<dim; j++)
		{//aca si puede haber conflictos entre vecinos
		if (S1*S2) //hay conflicto
		else
			if S1 actualizar(...S1) //el unico vecino es S1
			else actualizar(...S2) //el unico vecino es S2
		}
	}
}


actualizar:
si S=0 incrementa frag y le pone etiqueta
si S=/=0 copia la etiqueta VERDADERA (seguir el camino de etiquetas falsas)
RECUERDO: para rastrear etiquetas verdaderas:
while (*(historial+S)<0)
	{S=-(*(historial+S));
	}
*local=S;
/* OJO ACA! Si canchereo evaluando actualizar en (red+i)
aca pongo un puntero local, porque ya le estoy diciendo 
a que lugar de la memoria ir */


