#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>


int poblar(int *red, int N, double P);
int imprimir(int *red, int N);
int clasificar(int *red, int N);
int actualizar(int *local, int *historial, int S, int *frag);
int etiquetafalsa(int *local, int *historial, int S1, int S2);
int corregir(int *red, int N);


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
	clasificar(red,N);
	printf("\n");
	imprimir(red,N);
	
return 0;
}

//----------FUNCIONES----------

int poblar(int *red, int N, double P)
{//llena la red cuadrada de lado N con prob P
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


int clasificar(int *red, int N)
{
	int i,j;
	int *frag; //contador de fragmentos o clusters
	frag = (int*)malloc(sizeof(int));
	*frag = 2;
	int *historial;
	historial = (int*)malloc(N*N/2*sizeof(int));
	for (i=0; i<N*N/2; i++)
		*(historial+i) = i;
	
	//el primer lugar de la red
	if (*red)
	{*(red)=*frag;
	(*frag)++;
	}
	
	//la primera fila, solo miro el vecino a izq
	for (i=1; i<N; i++)
	if (*(red+i))
		{int S = *(red+i-1);
		actualizar(red+i, historial, S, frag);
		}
	
	//la primera columna, solo miro vecino arriba
	for (i=1; i<N; i++)
	{
		if (*(red+N*i))
			{int S = *(red+N*(i-1));
			actualizar(red+N*i, historial, S, frag);
			}
		
		//el resto de la red, donde puede haber conflictos de etiquetas
		for (j=1; j<N; j++)
		if (*(red+N*i+j))
			{int S1 = *(red+N*(i-1)+j);
			int S2 = *(red+N*i+j-1);
			if (S1*S1)
				etiquetafalsa(red+N*i+j, historial, S1, S2);
			//hay conflicto xq ambos lugares tienen elementos COMPLETAR
			else //no hay conflicto porque solo un lugar tiene un elemento
				{if (S1) //el unico vecino es S1
					actualizar(red+N*i+j, historial, S1, frag);
				else //el unico vecino es S2
					actualizar(red+N*i+j, historial, S2, frag);
				}
			}
	}
return 0;
}


int actualizar(int *local, int *historial, int S, int *frag)
{//si S=0 le pone etiqueta e incrementa frag
//sino copia la etiqueta VERDADERA
//OJO! El puntero es local asi que evaluar actualizar en (red+i)
	if (S==0)
	{*local=*frag;
	(*frag)++;
	}
	else
	{
	//para rastrear etiquetas verdaderas
	while (*(historial+S)<0)
		S=-(*(historial+S));
	*local=S;
	}
return 0;
}


int etiquetafalsa(int *local, int *historial, int S1, int S2)
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

	*local = minimo;
	*(historial+maximo) = -minimo;
//los que antes eran el valor max ahora son el min pero falso (por eso el -) 
//este queda mal igual si S1=S2
	*(historial+minimo) = minimo;
// esto es por las dudas, ya debería valer minimo
// ademas la ultima linea salva el caso S1=S2
return 0;
}


int corregir(int *red, int N)
{
	int i;
	for (i=0;i<N*N; i++)
		{
		}
return 0;
}


