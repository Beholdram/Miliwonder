#Autor: Matias Rodriguez 
#Aliases: @Beholdram @acorariel
#listo para ejecutarse con el comando python3
palindrome_pool = 'afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood'
print('Texto del que se hará la extracción de palíndromos:\n\n"""\n{}\n"""'.format(palindrome_pool))
"""
La estrategia se basa en un barrido de cada letra, uno principal(main) y uno secundario(alt).

Ambos barridos se justifican en el que cada letra dentro de una cadena de texto es un candidato a ser el inicio(>>>>) de un palíndromo en el barrido principal,
mientras que en el secundario es candidato a ser el fin(<<<<) de un palíndromo

por ejemplo,

ANACIICANA

inserto en una cadena de texto, representa 6 palíndromos:

-ANACIICANA
-NACIICAN
-ACIICA
-CIIC
-ANA
-II

Para lograr la solución, La porción de la cadena a la derecha de la letra observada es barrida descendentemente, 
en busca de todas las posibles coincidencias de término del palíndromo, basado en la letra consultada 
como contraparte inicial, conservando en una lista los resultados sin repetirlos.
"""
def candidates(letter_main,emordnilap_pool_alt,palindrome_pool_compare):
   candidate=0
   pool_segment =''
   repeated_pali=0
   for letter_alt in emordnilap_pool_alt:
      if(letter_alt==letter_main):
         alt_main=emordnilap_pool_alt[candidate:]
         pool_segment=letter_main+alt_main[::-1]
         if(len(pool_segment)>2):#filtrar candidatos por largo de palabra
            tail= len(palindrome_pool_compare) - len(pool_segment)
            alt_pali=pool_segment[::-1]
            main_pali=(palindrome_pool_compare if (tail==0) else palindrome_pool_compare[:-tail])
            mirror=alt_pali+main_pali
            left=mirror[(len(mirror)//2):]
            right=mirror[:(len(mirror)//2)]
            if (left in right):
               succ='Para ['+letter_main+'] encontré: '+left
               if (succ not in palindrome_vault):
                  palindrome_vault.append(succ)
                  
      candidate=candidate+1

processed_main=0
processed_alt=len(palindrome_pool)
palindrome_vault=[]
for letter_main in palindrome_pool:
   processed_main=processed_main+1
   palindrome_pool_alt=palindrome_pool[processed_main:]
   emordnilap_pool_alt=palindrome_pool_alt[::-1]
   processed_alt=len(emordnilap_pool_alt)-1
   candidates(letter_main,emordnilap_pool_alt,palindrome_pool[(processed_main-1):])
for element in palindrome_vault:
   print(element)
#El némesis de este desarrollo, actualmente serían las tíldes y las mayúsculas, ya que no las probé jeje