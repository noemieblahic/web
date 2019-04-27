#include <iostream> // Inclut la bibliothèque iostream (affichage de texte)
#include <cmath>

using namespace std; // Indique quel espace de noms on va utiliser

/*
Fonction principale "main"
Tous les programmes commencent par la fonction main
*/
int main()
{
    /*cout << "Hello world!" << endl; // Affiche un message
    int ageNoemie(23);
    int& ageUtilisateur(ageNoemie); // referenece
    cout << "Votre age est : " << ageNoemie << endl;
    string nomUtilisateur("Albert Einstein");

    int nombreAmis(432);      //Le nombre d'amis de l'utilisateur

    double pi(3.14159);

    bool estMonAmi(true);    //Cet utilisateur est-il mon ami ?

    char lettre('a'); */
    int nombre1, nombre2, nombre3, resultat;

    cout << "Valeur du nombre 1 ?" << endl;
    cin >> nombre1; //On crée une case mémoire pour contenirune chaine de caractères

    cout << "Valeur du nombre 2 ?" << endl;
    cin >> nombre2;

    cout << "Valeur du nombre 3 ?" << endl;
    cin >> nombre3;

    resultat = pow(nombre1,nombre2) - nombre3 ;

    cout << nombre1 << "^" << nombre2 << "-" << nombre3 << "=" << resultat << endl;

    return 0; // Termine la fonction main et donc le programme
}


########################################################


#include <iostream>
using namespace std;

void dessineRectangle(int l, int h)
{
    for(int ligne(0); ligne < h; ligne++)
    {
        for(int colonne(0); colonne < l; colonne++)
        {
            cout << "*";
        }
        cout << endl;
    }
}

int main()
{
    int largeur, hauteur;
    cout << "Largeur du rectangle : ";
    cin >> largeur;
    cout << "Hauteur du rectangle : ";
    cin >> hauteur;

    dessineRectangle(largeur, hauteur);
    return 0;
}


########################################################

#include <iostream>

using namespace std;

// Prototype de la fonction
int nombreDeSecondes(int heures, int minutes, int secondes);

// Main
int main()
{
    cout << nombreDeSecondes(1, 10, 25) << endl;

    return 0;
}

// Définition de la fonction
int nombreDeSecondes(int heures, int minutes, int secondes)
{
    int total = 0;

    total = heures * 60 * 60;
    total += minutes * 60;
    total += secondes;

    return total;
}

########################################################
