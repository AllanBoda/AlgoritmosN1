# Implementação da Subsequência Comum Máxima (LCS) usando recursividade com memoização
def lcs(s1, s2, m, n, memo=None):
    # Inicializa o cache de memoização se for None
    if memo is None:
        memo = {}
    
    # Cria uma chave única para o estado atual (m, n)
    chave = (m, n)
    
    # Verifica se o resultado já está no cache
    if chave in memo:
        return memo[chave]
    
    # Caso base: se uma das strings for vazia, o tamanho da LCS é 0
    if m == 0 or n == 0:
        return 0
    
    # Se os caracteres forem iguais, inclui o caractere e recursiona nas substrings restantes
    if s1[m-1] == s2[n-1]:
        resultado = 1 + lcs(s1, s2, m-1, n-1, memo)
    else:
        # Se os caracteres forem diferentes, tenta excluir um caractere de uma das strings
        resultado = max(lcs(s1, s2, m-1, n, memo), lcs(s1, s2, m, n-1, memo))
    
    # Armazena o resultado no cache antes de retornar
    memo[chave] = resultado
    return resultado

# Função auxiliar para executar a LCS e retornar o tamanho
def maior_subsequencia_comum(s1, s2):
    return lcs(s1, s2, len(s1), len(s2))

# Exemplo de uso
if __name__ == "__main__":
    # Casos de teste
    s1 = "ABCDGH"
    s2 = "AEDFHR"
    print(f"Tamanho da LCS para '{s1}' e '{s2}': {maior_subsequencia_comum(s1, s2)}")  # Esperado: 3 (ADH)
    
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    print(f"Tamanho da LCS para '{s1}' e '{s2}': {maior_subsequencia_comum(s1, s2)}")  # Esperado: 4 (GTAB)