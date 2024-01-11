import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int [] arreglo = new int[5];
		
		//System.out.println("El tamaño del arreglo es: " + arreglo.length);
		
		Scanner sc = new Scanner(System.in);
		
		for (int i = 0; i < arreglo.length; i++) {
			System.out.println("Ingresa un número para la posición " + i  + " del arreglo: ");
			arreglo[i] = sc.nextInt();
		}
		
		
		
		//mostrar arreglo
		
		for (int y = 0; y < arreglo.length; y++) {
			System.out.println("arreglo["+y+"] = " + arreglo[y]);
		}
		
		//suma
		int suma = 0;
		
		for (int u = 0; u < arreglo.length; u++) {
			//suma += arreglo[u];
			if (arreglo[u] < 13) suma += arreglo[u];
		}
		
		System.out.println("La suma del arreglo es = " + suma);
		
		//System.out.println("Digite un número: ");
		//numero = entrada.nextInt();
		
		//System.out.println(numero);

	}

}
