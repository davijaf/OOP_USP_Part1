
public class Calcular {
	public static void main(String []args) {
		Calculadora calc = new Calculadora(3,4);
		
		float resultado = calc.media();
		
		System.out.println("A média é igal a: "+ resultado);
	}
}
