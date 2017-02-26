
public class Aef1 extends Aef {

	@Override
	public boolean accepte(String entree) {
		int etat = 1; // etat initial de l'automate
		int index = 0; // rang du premier caractere a traiter
		char carlu; // caractere courant
		
		while(index != entree.length()) {
			// tant qu'il reste des caracteres a traiter
			carlu = entree.charAt(index++); // lecture caractere courant et passage au suivant
			if ((etat==1)&&(carlu=='a')) etat=2;
			else if ((etat == 2) && (carlu=='b')) etat=1;
			else return false;
		}
		
		// il n'ya plus rien a lire : est-on dans un etat terminal ?
		if (etat==2) return true; // entree est acceptee
		else return false; // entree n'est pas acceptee
	}

}
