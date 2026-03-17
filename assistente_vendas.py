import json

def carregar_especificacao(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def analisar_interesse(interesse, gatilhos):
    # Lógica simples para classificar baseado em gatilhos
    if 'academia' in interesse.lower():
        return 'AcademiaPerformance', 'High ticket provável'
    elif 'presente' in interesse.lower():
        return 'Presente', 'Misto'
    elif 'confortáveis' in interesse.lower() or 'dia a dia' in interesse.lower():
        return 'ConfortoDiario', 'Low ticket provável'
    else:
        return 'LookCompleto', 'Misto'

def gerar_resposta(interesse, especificacao):
    papel = especificacao['AssistenteDeVendas_Lupo']
    gatilhos = papel['5_GatilhosOportunidade']
    formato = papel['3_FormatoResposta']
    regras = papel['4_RegrasDeOuro']

    gatilho, classificacao = analisar_interesse(interesse, gatilhos)

    # Diagnóstico
    if classificacao == 'High ticket provável':
        motivo = "Academia exige peças de qualidade, duráveis e confortáveis"
        descobrir = ["orçamento", "kit completo ou peças avulsas", "valorização estética"]
    elif classificacao == 'Low ticket provável':
        motivo = "Foco em conforto diário com peças práticas"
        descobrir = ["orçamento", "ocasião", "urgência"]
    else:
        motivo = "Interesse misto, pode evoluir para kit ou presente"
        descobrir = ["orçamento", "ocasião", "estilo"]

    # Perguntas de Qualificação
    if gatilho == 'AcademiaPerformance':
        perguntas = [
            "Você procura peças só para treino ou também para usar no dia a dia?",
            "Prefere kit completo (camiseta + bermuda + meia) ou peças separadas?",
            "Qual faixa de orçamento você tem em mente?",
            "Valoriza mais conforto ou estilo?",
            "Precisa com urgência ou pode esperar promoções?"
        ]
    else:
        perguntas = formato['C_PerguntasQualificacao']

    # Oferta Principal
    if classificacao == 'High ticket provável':
        produto = "Kit esportivo Lupo (camiseta dry fit + bermuda + meia)"
        beneficio = "Conforto para treinar, durabilidade e estilo moderno"
        apresentacao = "Esse kit é perfeito para treinar com conforto e ainda manter um visual moderno na academia."
    else:
        produto = "Produto principal + benefício prático"
        beneficio = "Conforto e praticidade para o dia a dia"
        apresentacao = "Oferecer peças básicas que atendem ao conforto necessário."

    # Oferta Complementar
    if gatilho == 'AcademiaPerformance':
        itens = ["Meias esportivas", "Cueca performance", "Camiseta básica extra"]
        encaixe = ["Desempenho", "Praticidade", "Estética"]
    else:
        itens = formato['E_OfertaComplementar']['itens']
        encaixe = formato['E_OfertaComplementar']['encaixe']

    # Estratégia de Ancoragem
    opcao1 = ["Bom (peças avulsas)", "Ótimo (kit esportivo)", "Premium (linha performance completa)"]
    opcao2 = ["Custo-benefício (kit básico)", "Performance (linha premium com tecnologia dry fit)"]

    # Mensagens
    whatsapp = "Oi! 😊 Vi que você procura roupas confortáveis para academia. Tenho um kit esportivo Lupo que garante conforto, durabilidade e estilo moderno. Além disso, podemos incluir meias e cuecas performance para completar seu treino. Quer que eu te mostre opções dentro da sua faixa de orçamento?"
    instagram = "Oi! ✨ Tenho um kit esportivo Lupo perfeito para treinar com conforto e estilo. Quer ver opções dentro da sua faixa de orçamento?"

    resposta = {
        "AssistenteDeVendas_Lupo": {
            "InteresseCliente": interesse,
            "Diagnostico": {
                "classificacao": classificacao,
                "motivo": motivo,
                "descobrir": descobrir
            },
            "PerguntasQualificacao": perguntas,
            "OfertaPrincipal": {
                "produto": produto,
                "beneficio": beneficio,
                "apresentacao": apresentacao
            },
            "OfertaComplementar": {
                "itens": itens,
                "encaixe": encaixe
            },
            "EstrategiaAncoragem": {
                "opcao1": opcao1,
                "opcao2": opcao2
            },
            "Mensagens": {
                "WhatsApp": whatsapp,
                "Instagram": instagram
            }
        }
    }
    return resposta

def main():
    caminho = 'especificacao_assistente.json'
    especificacao = carregar_especificacao(caminho)
    
    interesse = "Quer roupas confortáveis para academia"
    resposta = gerar_resposta(interesse, especificacao)
    print("\nResposta do Assistente (JSON):")
    print(json.dumps(resposta, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()