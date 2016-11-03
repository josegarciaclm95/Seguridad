package diffHellman;


public class Main {

	public static void main(String[] args) {
		//System.out.print("Hola mundo\n");
		//System.out.print(Long.MAX_VALUE + "\n");
		//System.out.print(Integer.MAX_VALUE);
		//System.out.println((long)5/(long)2);
		//System.out.println(ExponenciacionModular(33,47,1999));
		System.out.println(Math.pow((double)5,(double)32));
		System.out.println(ExponenciacionModular(5,117,19));
		//System.out.println(new StringBuilder(Long.toBinaryString(117)).reverse().toString());
		
	}

	
	/**
	 * Operación exponencial modular
	 * @param x Exponente
	 * @param n Base
	 * @param p modulo
	 * @return
	 */
	public static long ExponenciacionModular(long n, long x, long p){
		//Se hacen publicos n y p
		//Se elige un x
		long z = 1;
		long arrastre;
		long a = 1;
		long c;
		int i = 0;
		while(x != 0){
			i++;
			c = x % 2;
			x = x/2;
			arrastre = (long) (Math.pow(n,a)%p);
			//System.out.println(arrastre);
			if(c == 1){
				System.out.println((x*2+c) + " - " + arrastre + " - " + z);
				z = (z * arrastre)%p;
				System.out.println("Nueva z  - " + z);
			}
			a*= 2;
		}
		return z;
	}
	
	//ver cuantas veces se puede dividir el exponente por dos hasta llegar a cero
}



