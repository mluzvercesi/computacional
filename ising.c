#include <stdio.h>
#include <stdlib.h>
#include <string.h> /* memset */
#include <math.h>
#include <time.h>
#include <unistd.h> /* close */


double aleatorio();

//necesito un programa que me de p* o p* exp(), con una dada probabilidad
//La funcion es f(x) = exp{-x²/2} / sqrt(2pi)


//correr esto para distintos deltas, para hallar el delta critico, donde la correlacion es minima.
int main(){
  //elegimos primero un x_0 random
  //elegimos un x_1 random que esté a una distancia delta de x0
  FILE *fp;
  int N, i, m;
  double xi, xf, delta_x, random, p, delta; //xi es inicial y xf es final
  double *serie;
  N = 10000;
  srand(time(NULL));
  // delta = 5;
  serie = (double*)malloc(N*sizeof(double));

  xi = 2 *aleatorio()-1;
  *serie = xi;


	char fn[100];
	sprintf(fn,"importance_sampling_deltas_0_3.txt"); //para que cada tamaño de red sea un archivo distinto
	fp = fopen(fn, "w");
	fprintf(fp, "delta; serie de %d pasos", N);


  for (delta = 0; delta < 3; delta+=0.1){
    fprintf(fp, "\n%f\t", delta);
    for(m = 1; m < N; m++){
      xf = delta * (2 * aleatorio() -1) + xi; //esto elije el xf de modo tal que sea aleatorio y que quede entre xi-delta y xi+delta

      delta_x = (pow(xf,2) - pow(xi,2)) / 2;
      random = aleatorio();

      //la proba de aceptar x1 viene dada por exp{x0²/2-x1²/2}. Comparamos esta proba con un numero random para ver si lo aceptamos.
      p = exp(-delta_x);
      if (p > random){
        *(serie+m) = xf;
        xi = xf;
      }
      else{
        *(serie+m) = xi;
      }


    } //cierra el loop en la serie
    for (i=0; i<N; i++){
			fprintf(fp, "\t%f", *(serie+i));
		}
  } //cierra el loop en deltas
  free(serie);
  return 0;
}

double aleatorio(){
  double random;

  random = (float)rand()/(float)RAND_MAX;

  return random;
}
