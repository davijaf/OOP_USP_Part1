import java.io.FileReader;

public class LeitorDeArquivo {
        static char [] leArquivo(String nomeArq) {
            char [] conteudo = new char[1024];
            try {
                if(nomeArq.endsWith(".mc"))
                    throw new UglyFileException();
                FileReader fr = new FileReader(nomeArq);
                fr.read(conteudo);
                fr.close();
            }
            catch (Exception e) {
                System.out.println("Não deu certo, mãe :" + e);
            }
            return conteudo;

        }

        public static void main(String[] args) {
            try {
                System.out.println(leArquivo(args[0]));
            }
            catch (Exception e) {
                System.out.println("Não deu certo, pai :" + e);
            }
        }
}
