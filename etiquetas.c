#include <stdio.h>
#include <stdlib.h>
#include <string.h> /* memset */
#include <math.h>
#include <time.h>
#include <unistd.h> /* close */

#define MAXFILENAME 100

int poblar(int *red, int N, double P);
int imprimir(int *red, int N);
int clasificar(int *red, int N);
int actualizar(int *local, int *historial, int S, int *frag);
int etiqueta_verdadera(int *historial, int S);
int etiqueta_falsa(int *local, int *historial, int S1, int S2);
int percola(int *red, int N);
int ns(int *etiqueta, int *dens_cluster, int N)



//------------MAIN-------------
int main(){ //agregar como argumento la probabilidad y el tamaño de la red
	double P;
	int N=6; //tamaño de la red
	srand(time(NULL));
	int *red;
	int i,j,t,k;
	FILE *fp;
	int *clusters;
	int *etiquetas;
	int *densidad;
	int counter[N*N+1]={0};


	char fn[MAXFILENAME+1];
	sprintf(fn,"prueba.txt"); //para que las probas de cada tamaño de red sean distintos archivos
	fp = fopen(fn, "w");
	fprintf(fp, "C0 la proba; C1 - C(N*N/2) tamaño de cluster de cada número en orden 0 1 2 3...;  C(N*N/2+1) - C(N*N/2+1 + N/2) etiquetas cluster percolante. \n");

	red = (int*)malloc(N*N*sizeof(int));

	P = 0.0;

	// for (P=0.5; P<0.65; P+=0.0001){

		for (k = 0; k<10; k++){ //acá tiene que decir k<27000
			fprintf(fp, "%f \t", P);
			poblar(red,N,P);
			clasificar(red,N);
			clusters = calloc(N*N/2, sizeof(int));
			etiquetas = calloc(N,sizeof(int));
			for (i=0; i<N*N; i++){
				t = *(red+i);
				clusters[t]++;
				if (i<N && *(red+i)!=0){
					for (j=0; j<N; j++){
						if (*(red+N*(N-1)+j) == *(red+i))
							{etiquetas[i] = *(red+i);
						}
					}
				}
			}
			for (i=0; i<N*N; i++){
				densidad = ns(etiquetas, clusters, N); //imprime cluster size para cada etiqueta
			}
			fprintf(fp, "%d \n", densidad);
			//devuelve una tabla donde cada fila corresponde a una proba y cada columna es el tamaño de un cluster, al final agrega las etiquetas de clusters percolantes
		} //end loop iteraciones
	// } //end loop probabilidades
	free(red);
return 0;
}


//----------FUNCIONES----------

//llena la red cuadrada de lado N con prob P
int poblar(int *red, int N, double P){
	int i;
	float random;
	for (i=0; i<N*N; i++)
		{random = (float)rand()/(float)RAND_MAX; //se podria mejorar este random
		if (random < P)
			*(red+i) = 1;
		else
			*(red+i) = 0;
		}
return 0;
} //cierra la función


//para mostrar la red creada
int imprimir(int *red, int N){
	int i,j;
	for (i=0; i<N; i++)
		{
		for (j=0; j<N; j++)
			printf("%d ", *(red+N*i+j));
		printf("\n");
		}
printf("\n");
return 0;
} //cierra la función

// le asigna etiquetas a los lugares de la red con valor 1
int clasificar(int *red, int N){
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
	for (i=1; i<N; i++){
		if (*(red+i))
			{int S = *(red+i-1);
			actualizar(red+i, historial, S, frag);
			}
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
			{int S1 = *(red+N*(i-1)+j); //vecino arriba
			int S2 = *(red+N*i+j-1); //vecino izq
			if (S1*S2) //hay conflicto porque ambos lugares estan ocupados
				etiqueta_falsa(red+N*i+j, historial, S1, S2);
			else //no hay conflicto
				{if (S1) //el unico vecino es S1
					actualizar(red+N*i+j, historial, S1, frag);
				else //el unico vecino es S2
					actualizar(red+N*i+j, historial, S2, frag);
				}
			}
	}

	//corrijo las etiquetas
	for (i=0; i<N*N; i++)
		{j = *(red+i);
		*(red+i) = etiqueta_verdadera(historial, j);
		}

free(frag);
free(historial);

return 0;
} //cierra la función

//les da la etiqueta verdadera a los valores
int actualizar(int *local, int *historial, int S, int *frag){
//si S=0 le pone etiqueta e incrementa frag
//sino copia la etiqueta VERDADERA
//OJO! El puntero es local asi que evaluar actualizar en (red+i)
	if (S==0)
	{*local = *frag;
	(*frag)++;
	}
	else
	{
	*local = etiqueta_verdadera(historial,S);
	}
return 0;
} //cierra la función

//??
int etiqueta_verdadera(int *historial, int S){
	while (*(historial+S)<0)
		S=-(*(historial+S));
return S;
} //cierra la función

//corrige las etiquetas y les pone un - si las tuvo que cambiar
int etiqueta_falsa(int *local, int *historial, int S1, int S2){
	int minimo, maximo;

	S1 = etiqueta_verdadera(historial, S1);
	S2 = etiqueta_verdadera(historial, S2);

//quiero asignar la menor etiqueta verdadera

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
} //cierra la función

//este toma el cluster y me va a devolver el ns ya hecho array. después lo único que hay qye hacer en el main es llamar a este y dividir por 27000 una vez que ya haya corrido todo
int ns(int *etiqueta, int *dens_cluster, int N){
	int size;
	for (int s=0; s<N*N/2; s++){
		if(*(etiqueta+s)){
			size = *etiqueta;
			*(dens_cluster + size) = *(dens_cluster + size)+1;
		}
	}

return 0;
}//cierra la función

// Devuelve 1 si percola, 0 si no percola
int percola(int *red, int N){
	int i,j;
	int p = 0;
	for (i=0; i<N; i++){
		if (*(red+i)!=0)
			for (j=0; j<N; j++)
				if (*(red+N*(N-1)+j) == *(red+i))
					{p = 1;
					break;
					}
		if (p==1)
			break;
		}
return p;
} //cierra la función
