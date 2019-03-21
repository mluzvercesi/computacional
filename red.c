# include <stdio.h>
# include <stdlib.h>
# include <math.h>
# include <time.h>

#define A 16807
#define M 2147483647
#define Q 127773
#define R 2836

//int clasificar (int *red, int N);
//int percolar(int *red);
//double random(int *semilla);
int poblar(int *red, double P, int N);
int imprimir(int *red, int N);

// MAIN
// Primero creamos la red
int main(int argc, char *argv[])
	{
	int *red;
	int N;
	double P;
	N = argv[0];
	P = argv[1];
	red = (int*)malloc(N*N*sizeof(int));
	poblar(int *red, double P, int N);
	imprimir(int *red, int N);
	return 0;
	}

// FUNCIONES
/*double random(int *semilla)
	{
	int K;
	double x;

	K = (*semilla) / Q;
	*semilla =  A *(*semilla) - K *Q - K*R;

	if (*semilla < 0.0)
		*semilla = (*semilla)+M;

	x = (*semilla) * (1.0/M);
	return x;
	}*/

int poblar(int *red, double P, int N) //función que puebla la red
	{
	int i;
	int *semilla;
	semilla = srand(time(NULL)); //???????????
	for (i=0; i<N*N; i++)
		{
		if (1 < P) //(random(*semilla) < P)
		*(red+i) = 1;
		}
	return = 0;
	}

int imprimir(int *red, int N)
	{
	int i,j;
	for (i=0; i < N; i++)
		{
		for (j=0; j < N; j++)
		printf("%d ", *(red+N+i+j));
		printf("/n");
		}
	return 0;
	}


