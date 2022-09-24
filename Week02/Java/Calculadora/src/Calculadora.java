
public class Calculadora {
	private int primeiroValor;
	private int segundoValor;
	
	public Calculadora(int primeiro, int segundo) {
		this.primeiroValor = primeiro;
		this.segundoValor = segundo;
	}
	
	public float media() {
		float media = 0;
		media = (float)(this.primeiroValor + this.segundoValor) / 2;
		return media;
	}
	
	public int maximo() {
		if(primeiroValor < segundoValor) {
			return this.segundoValor;
		}
		return this.primeiroValor;
	}
	
	public int minimo() {
		if(primeiroValor < segundoValor) {
			return this.primeiroValor;
		}
		return this.segundoValor;
	}
	
}	
	
