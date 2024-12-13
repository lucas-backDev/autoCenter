from django.db.models import TextChoices

class ChoicesCategoriaManutencao(TextChoices):
  TROCAR_VELAS_DO_MOTOR = ("TVM", "troca de velas de ingição do motor")
  TROCAR_OLEO_E_FILTRO = ("TOF", "troca de óleo e filtro")
  MANUTENCAO_FREIO = ("MF", "verificação e substituição de componentes, como pastilhas, discos e fluido de freio.")
  ALINHAMENTO_E_BALANCEAMENTO = ("AB", "alinhamento e balanceamento do carro")
  TROCAR_PNEUS = ("TP", "troca de pneus")
  TROCA_DE_CORREIASDENTADAS = ("TCD", "trocar as correias dentadas e verificar a tensão")
  REPARO_SUSPENSAO = ("RS", "reparo de suspensão")
  TROCAR_BATERIA = ("TB", "troca da bateria")
  AR_CONDICIONADO = ("AC", "manutenção preventiva, limpeza, substituição de filtros e recarga de gás refrigerante")
  TROCAR_SISTEMA_ESCAPE = ("TSE", "verificação e troca do sistema de escape")
  DIAGNÓSTICO = ("D", "diagnosticar e verificar problema de acordo com relato do cliente")
  LAVAGEM_E_SECAGEM_EXTERNA = ("LSE", "lavagem e secagem da parte externa (lataria) do carro")
  HIGIENIZAÇÃO_INTERNA = ("HI", "higienizar parte interna do carro, apirando e limpando painel de controle")
  CRISTALIZAÇÃO_DOS_VIDROS = ("CDV", "cristalização dos vidros")
  VITRIFICAÇÃO_DA_PINTURA = ("VDP", "vitrificação da pintura para maior resistência e brilho")
  