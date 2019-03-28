#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>


int poblar(int *red, int N, double P);
int imprimir(int *red, int N);
int clasificar(int *red, int N);
int etiquetafalsa(int *red, int *historial, int S1, int S2, int i);


//------------MAIN-------------
int main() //(int argc, char * argv[])
	{
	int N = 8;
	double P = 0.5;
	//si ingreso argumentos a main uso las dos lineas que siguen
	//int N = atoi(argv[1]); 
	//double P = atof(argv[2]);
	int *red;
	red = (int*)malloc(N*N*sizeof(int));
	
	poblar(red,N,P);	
	imprimir(red,N);

	return 0;
	}

//----------FUNCIONES----------

int poblar(int *red, int N, double P) //llena la red cuadrada de lado N con prob P
	{
	int i;
	float random;
	srand(time(NULL));
	for (i=0; i<N*N; i++)
		{random = (float)rand()/(float)RAND_MAX; //se podria mejorar este random
		if (random < P)
			*(red+i) = 1;
		}
	return 0;
	}

int imprimir(int *red, int N) //para mostrar la red creada
	{
	int i,j;
	for (i=0; i<N; i++)
		{
		for (j=0; j<N; j++)
			printf("%d ", *(red+N*i+j));
		printf("\n");
		}
	return 0;
	}

// HASTA ACA FUNCIONA. A PARTIR DE ACA HAY QUE ESCRIBIR ACTUALIZAR

int clasificar(int *red, int N)
{
	int i,j;
	int frag = 2; //contador de fragmentos o clusters, por que empieza en 2??
	
	//el primer lugar de la red
	if *(red)
	{*(red)=frag;
	frag++;
	}
	
	//la primera fila, solo miro el vecino a izq
	for (i=1; i<N; i++)
	{int S = *(red+i-1);
	actualizar(red+i, historial, S, frag);
	}
	
	//la primera columna, solo miro vecino arriba
	for (i=1; i<N; i++)
	{int S = *(red+N*(i-1));
	actualizar(red+N*i, historial, S, frag);
	
		//el resto de la red, donde puede haber conflictos de etiquetas
		for (j=1; j<N; j++)
			{int S1 = *(red+N*(i-1)+j);
			int S2 = *(red+N*i+j-1);
			if (S1*S2) //hay conflicto porque ambos lugares tienen elementos
			else //no hay conflicto porque solo un lugar tiene un elemento
				{if S1 //el unico vecino es S1
					actualizar(red+N*i+j, historial, S1, frag);
				else //el unico vecino es S2
					actualizar(red+N*i+j, historial, S2, frag);
				}
			}
	}
return 0;
}

/*
actualizar:
si S=0 incrementa frag y le pone etiqueta
si S=/=0 copia la etiqueta VERDADERA (seguir el camino de etiquetas falsas)
RECUERDO: para rastrear etiquetas verdaderas:
while (*(historial+S)<0)
	{S=-(*(historial+S));
	}
*local=S;

OJO ACA! Si canchereo evaluando actualizar en (red+i)
aca pongo un puntero local, porque ya le estoy diciendo 
a que lugar de la memoria ir


int etiquetafalsa(int *red, int *historial, int S1, int S2, int i)
	{
	int minimo, maximo;

	while (*(historial+S1)<0)
		S1 = -(*(historial+S1));

	while (*(historial+S2)<0)
		S2 = -(*(historial+S2));

//ahora tengo la etiqueta verdadera de mis vecinos
//quiero asignarle la menor

	if (S1<S2)
	{
	minimo=S1;
	maximo=S2;
	}
	else
	{
	minimo=S2;
	maximo=S1;
	}

	*(red+i) = minimo;
	*(historial+maximo) = -minimo; 
//los que antes eran el valor max ahora son el min pero falso (por eso el -) 
//este queda mal igual si S1=S2
	*(historial+minimo) = minimo; 
// esto es por las dudas, ya debería valer minimo
// ademas la ultima linea salva el caso S1=S2
	return 0;
	}
*/


