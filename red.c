#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>


int poblar(int *red, int N, double P);
int imprimir(int *red, int N);
int clasificar(int *red, int N);
int etiquetafalsa(int *red, int *historial, int S1, int S2, int i);


// MAIN
int main(int argc, char * argv[])
	{
	int N = atoi(argv[1]);
	double P = atof(argv[2]);
	int *red;
	printf("%s %s \n", "Lado", argv[1]);
        printf("%s %s \n", "Prob", argv[2]);
	red = (int*)malloc(N*N*sizeof(int));
	
	poblar(red,N,P);	
	imprimir(red,N);

	return 0;
	}


int poblar(int *red, int N, double P) //función que puebla la red
	{
	int i;
	float random;
	srand(time(NULL));
	for (i=0; i<N*N; i++)
		{random = (float)rand()/(float)RAND_MAX;
		if (random < P)
			*(red+i) = 1;
		}
	return 0;
	}

int imprimir(int *red, int N)
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

/*int clasificar(int *red, int N)
	{
	int i;
	int frag; //etiqueta
	frag = 2; //por que empezaba en 2??
	for (i=0; i<N; i++) //recorro la primera fila
	{if (*(red+i))
		{*(red+i)=frag;
		frag++;
		}
		
	}
	
	return 0;
	}

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


