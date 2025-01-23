#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int minimumLength(string s) {
        int finalLength = s.size();
        bool borrado_flag_atras = false, borrado_flag_adelante = false;
        int T_adelante_Final = 0, T_atras_Final = 0;

        cout << "Inicial: " << s << endl;

        for (int i = 0; i < s.size(); i++) {
            if (i > 0 && i < s.size() - 1) {
                cout << "Buscado:  " << s[i] << endl;

                // Búsqueda hacia atrás
                for (int T_atras = i - 1; T_atras >= 0; T_atras--) {
                    borrado_flag_atras = false;
                    if (s[i] == s[T_atras]) {
                        borrado_flag_atras = true;
                        T_atras_Final = T_atras; // Guardar el índice final hacia atrás
                        break;
                    }
                }

                // Búsqueda hacia adelante
                for (int T_adelante = i + 1; T_adelante < s.size(); T_adelante++) {
                    borrado_flag_adelante = false;
                    if (s[i] == s[T_adelante]) {
                        borrado_flag_adelante = true;
                        T_adelante_Final = T_adelante; // Guardar el índice final hacia adelante
                        break;
                    }
                }

                // Borrar los caracteres si se encontraron coincidencias
                if (borrado_flag_adelante && borrado_flag_atras) {
                    cout << "BOOORRADOOOO PERRAS" << endl;
                    cout << "Borrado Trasero: " << s[T_atras_Final] << " en índice " << T_atras_Final << endl;
                    cout << "Borrado Delantero: " << s[T_adelante_Final] << " en índice " << T_adelante_Final << endl;

                    // Eliminar en el orden correcto para evitar errores
                    if (T_adelante_Final > T_atras_Final) {
                        s.erase(T_adelante_Final, 1); // Borrar hacia adelante
                        s.erase(T_atras_Final, 1);   // Borrar hacia atrás
                    } else {
                        s.erase(T_atras_Final, 1);   // Borrar hacia atrás
                        s.erase(T_adelante_Final, 1); // Borrar hacia adelante
                    }

                    // Actualizar el índice `i` para reflejar el string modificado
                    i = max(0, i - 2); // Retroceder un paso para procesar el string correctamente
                }
                cout << "Cadena actualizada: " << s << endl;
                cout << "--------------------------------------" << endl;
            }
        }

        cout << "Final: " << s << endl;
        return s.size(); // Retornar la longitud mínima final
    }
};

int main() {
    Solution solution;

    // Caso de prueba
    //abaacbcbb
    //aa
    string s = "rbibmq";

    // Ejecutar la función
    int result = solution.minimumLength(s);

    // Mostrar el resultado
    cout << "La longitud mínima de la cadena es: " << result << endl;

    return 0;
}
