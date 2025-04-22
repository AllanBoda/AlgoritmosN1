
Escolha do Problema: Subsequência Comum Máxima (LCS)
 - Escolhemos o problema LCS porque é um exemplo clássico de programação dinâmica, ideal para demonstrar como memoização otimiza recursividade.
 - O objetivo é encontrar o tamanho da maior subsequência comum entre duas strings, onde uma subsequência é formada ao remover caracteres sem alterar a ordem dos restantes.
 - Exemplo: Para "ABCD" e "ACDF", a LCS é "ACD" (tamanho 3).
 - Aplicações incluem alinhamento de sequências de DNA e ferramentas de comparação de texto (como "diff").

Estratégia: Recursividade com Memoização
 - Abordagem Recursiva: A função lcs(s1, s2, m, n, memo) recebe duas strings (s1, s2), seus tamanhos atuais (m, n) e um cache (memo). Ela compara os caracteres nas posições m-1 e n-1:
     - Se forem iguais, inclui o caractere (soma 1 ao resultado) e recursiona nas substrings restantes (m-1, n-1).
     - Se forem diferentes, tenta excluir um caractere de uma das strings e pega o máximo entre as duas chamadas recursivas (m-1, n ou m, n-1).
     - Caso base: Se uma string for vazia (m == 0 ou n == 0), o tamanho da LCS é 0.
 - Memoização: Para evitar cálculos redundantes, usamos um dicionário (memo) que armazena o resultado de cada estado (m, n). Antes de calcular, a função verifica o cache. Se o resultado estiver lá, ele é retornado, reduzindo a complexidade de tempo de O(2^n) para O(m*n).

Implementação do Cache
 - O cache é um dicionário Python (dict), que garante acesso em O(1) no caso médio.
 - A chave é uma tupla (m, n), representando os tamanhos atuais das substrings.
 - O valor é o tamanho da LCS para as substrings s1[0:m] e s2[0:n].
 - O cache é inicializado vazio e preenchido durante as chamadas recursivas, garantindo que cada estado seja calculado apenas uma vez.

Otimização
 - Sem memoização, a recursividade pura tem subproblemas sobrepostos, resultando em complexidade exponencial O(2^n).
 - Com memoização, cada subproblema é resolvido uma vez, reduzindo a complexidade de tempo para O(m*n), onde m e n são os tamanhos das strings.
 - A complexidade de espaço é O(m*n) para o cache, mais O(m+n) para a pilha de recursão.

Dicas para a Apresentação
 - Explique o Problema: Use um exemplo simples, como "ABC" e "AC", para mostrar como a LCS ("AC") é encontrada.
 - Mostre o Código: Destaque a função lcs, explicando o caso base, a comparação de caracteres e o uso do cache.
 - Demonstre a Otimização: Compare a recursividade pura (lenta) com a memoização, mencionando a redução de complexidade.
 - Teste o Código: Execute os casos de teste no código acima para mostrar que ele funciona corretamente.