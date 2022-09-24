
public interface ObjetoEspacial {
	int k = 42;
	
	int getPosicaoX();
	int getPosicaoY();
	
	void setPosicaoX();
	void setPosicaoY();
	
	void exploda(int intensidadeDaExplosao);
	
	boolean colideCom (ObjetoEspacial oe);
	
	byte [] suaMusica();
		
	String nome();
	String descricao();

}
